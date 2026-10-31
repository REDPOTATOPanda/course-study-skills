#!/usr/bin/env python3
"""Read-only checks for common course-note Markdown. No rendering or semantic validation."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


def check(path):
    issues = []
    def add(line, kind, detail):
        issues.append(dict(line=line, kind=kind, detail=detail))
    try:
        lines = path.read_text(encoding='utf-8-sig').splitlines()
    except (OSError, UnicodeError) as exc:
        return [dict(line=0, kind='read_error', detail=str(exc))]
    body = []
    fence = None
    previous = 0
    for n, line in enumerate(lines, 1):
        marker = re.match(r'^\s{0,3}(`{3,}|~{3,})(.*)$', line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = (marker[1][0], len(marker[1]), n)
            continue
        body.append((n, line))
        heading = re.match(r'^\s{0,3}(#{1,6})\s+', line)
        if heading:
            level = len(heading[1])
            if level > previous + 1:
                add(n, 'heading_jump', f'{previous} -> {level}; review hierarchy')
            previous = level
        if re.search(r'\b(?:TODO|FIXME|TBD)\b|待核对|待核实|待补充|答案暂缺|\ufffd', line):
            add(n, 'review_marker', 'Review placeholder or replacement character in context')
    if fence:
        add(fence[2], 'unclosed_fence', 'Code fence is not closed')
    definitions = {}
    def destination(s):
        s = s.strip()
        if s.startswith('<') and '>' in s:
            return s[1:s.index('>')]
        return re.split(r'\s+[\"\']', s, maxsplit=1)[0].strip()
    def label(s):
        return ' '.join(s.lower().split())
    for n, line in body:
        m = re.match(r'^\s{0,3}\[([^]]+)\]:\s*(.+)$', line)
        if m:
            definitions[label(m[1])] = destination(m[2])
    names = {}
    for n, line in body:
        targets = []
        # Balanced parentheses in bare URLs are outside this small checker's scope.
        inline = r'!\[[^]]*\]\(\s*(<[^>]*>|[^)]*)\)'
        for m in re.finditer(inline, line):
            targets.append(destination(m[1]))
        rest = re.sub(inline, '', line)
        for m in re.finditer(r'!\[([^]]*)\](?:\[([^]]*)\])?', rest):
            key = label(m[2] or m[1])
            if key in definitions:
                targets.append(definitions[key])
            else:
                add(n, 'unresolved_image_reference', key)
        for m in re.finditer(r'<img\b[^>]*\bsrc\s*=\s*[\"\']([^\"\']+)[\"\']', line, re.I):
            targets.append(m[1])
        for target in targets:
            parts = urlsplit(target)
            if parts.scheme or parts.netloc:
                add(n, 'external_image_unchecked', target)
                continue
            local = unquote(parts.path)
            if not local:
                add(n, 'empty_image_path', target)
                continue
            p = (path.parent / local).resolve()
            if not p.is_file():
                add(n, 'missing_image', local)
            names.setdefault(p.name, set()).add(str(p))
    for name, paths in names.items():
        if len(paths) > 1:
            add(0, 'duplicate_basename', f'{name}: distinct paths; review, not necessarily an error')
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('notes', nargs='+', type=Path)
    args = parser.parse_args()
    results = [dict(file=str(p), issues=check(p)) for p in args.notes]
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return int(any(r['issues'] for r in results))


if __name__ == '__main__':
    raise SystemExit(main())
