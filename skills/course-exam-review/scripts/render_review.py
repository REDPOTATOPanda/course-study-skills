#!/usr/bin/env python3
"""Render single-column JSON content using the bundled review style.
Requires reportlab, svglib; math requires Node and mathjax-full (3.x).
See references/style-examples.md. No network access or system-font assumptions.
"""
import argparse,json,subprocess,tempfile
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate,PageTemplate,Frame,Paragraph,Spacer,PageBreak,Table,TableStyle,KeepTogether
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from svglib.svglib import svg2rlg

def build(source,output,fonts,style,node='node',mathjax=None):
    for name in ['regular','bold','heading','western','western_italic']:
        cfg=fonts[name]
        pdfmetrics.registerFont(TTFont(name,cfg['path'],subfontIndex=cfg.get('index',0)))
    pdfmetrics.registerFontFamily('regular',normal='regular',bold='bold',italic='regular',boldItalic='bold')
    C=HexColor(style['text_color']);W,H=A4;m=style['margin_mm']*72/25.4;width=W-2*m
    body=ParagraphStyle('body',fontName='regular',fontSize=style['body_size'],leading=style['body_leading'],firstLineIndent=22,spaceAfter=style['paragraph_after'],wordWrap='CJK',textColor=C,splitLongWords=False,allowWidows=0,allowOrphans=0)
    title=ParagraphStyle('title',parent=body,fontName='heading',fontSize=style['title_size'],leading=28,firstLineIndent=0,spaceAfter=14)
    hs={}
    for lv,key in enumerate(['module_size','section_size','subsection_size'],1):
        hs[lv]=ParagraphStyle(f'h{lv}',parent=body,fontName='heading',fontSize=style[key],leading=style[key]*1.4,firstLineIndent=0,spaceBefore=style['heading_before'],spaceAfter=style['heading_after'],keepWithNext=True)
    caption=ParagraphStyle('caption',parent=body,firstLineIndent=0,fontSize=style['caption_size'],leading=14,spaceAfter=5)
    cell=ParagraphStyle('cell',parent=body,firstLineIndent=0,fontSize=style['table_size'],leading=15,spaceAfter=0)
    story=[]
    class Doc(BaseDocTemplate):
        def afterFlowable(self,f):
            if isinstance(f,Paragraph) and getattr(f,'toc_level',None) is not None:
                level=f.toc_level;key=f.toc_key
                self.canv.bookmarkPage(key);self.canv.addOutlineEntry(f.getPlainText(),key,level,False)
                self.notify('TOCEntry',(level,f.getPlainText(),self.page,key))
    def page(c,d):
        c.setStrokeColor(HexColor(style['rule_color']));c.setLineWidth(.35);c.line(m,H-36,W-m,H-36)
        c.setFillColor(C);c.setFont('regular',style['header_size']);c.drawString(m,H-27,source.get('running_title',source['title']))
        # Intentionally no right-hand question-range running header.
        c.setFont('western',style['header_size']);c.drawCentredString(W/2,27,str(d.page))
    doc=Doc(str(output),pagesize=A4,title=source['title'],author='',leftMargin=m,rightMargin=m,topMargin=53,bottomMargin=43)
    doc.addPageTemplates(PageTemplate(id='review',frames=[Frame(m,43,width,H-96,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=page))
    story.extend([Paragraph(source['title'],title),Paragraph('目录',hs[2])])
    toc=TableOfContents();toc.dotsMinLevel=0;toc.levelStyles=[ParagraphStyle('toc0',parent=body,fontName='heading',firstLineIndent=0,leading=23,spaceBefore=7),ParagraphStyle('toc1',parent=body,firstLineIndent=0,leftIndent=16,leading=21,spaceBefore=0)]
    story.extend([toc,PageBreak()])
    formulas=[b['tex'] for b in source['blocks'] if b['type']=='math']
    with tempfile.TemporaryDirectory(prefix='review-math-') as tmp:
        tmp=Path(tmp)
        if formulas:
            if not mathjax:raise ValueError('Formula blocks require --mathjax: path to installed mathjax-full package')
            js=tmp/'render.cjs';(tmp/'input.json').write_text(json.dumps(formulas))
            js.write_text(r'''
const fs=require('fs'),path=require('path');const root=process.argv[2],dest=process.argv[3];
const {mathjax}=require(path.join(root,'js/mathjax.js'));
const {TeX}=require(path.join(root,'js/input/tex.js'));
require(path.join(root,'js/input/tex/ams/AmsConfiguration.js'));
const {SVG}=require(path.join(root,'js/output/svg.js'));
const {liteAdaptor}=require(path.join(root,'js/adaptors/liteAdaptor.js'));
const {RegisterHTMLHandler}=require(path.join(root,'js/handlers/html.js'));
const a=liteAdaptor();RegisterHTMLHandler(a);
const doc=mathjax.document('',{InputJax:new TeX({packages:['base','ams']}),OutputJax:new SVG({fontCache:'none'})});
JSON.parse(fs.readFileSync(path.join(dest,'input.json'),'utf8')).forEach((tex,i)=>{
let s=a.outerHTML(doc.convert(tex,{display:true}));s=s.slice(s.indexOf('<svg'),s.lastIndexOf('</svg>')+6);
if(s.includes('data-mjx-error'))throw Error('MathJax error: '+tex);
const v=s.match(/viewBox="([^"]+)"/)[1].split(' ').map(Number),pt=Number(process.argv[4]);
s=s.replace(/width="[^"]+"/,`width="${v[2]*pt/1000}pt"`).replace(/height="[^"]+"/,`height="${v[3]*pt/1000}pt"`).replaceAll('currentColor','#111111');
fs.writeFileSync(path.join(dest,`f${i}.svg`),s);
});''')
            subprocess.run([node,str(js),str(Path(mathjax).resolve()),str(tmp),str(style['formula_size'])],check=True)
        mi=0;hi=0
        for b in source['blocks']:
            kind=b['type']
            if kind=='heading':
                lv=b['level'];p=Paragraph(b['text'],hs[lv]);hi+=1
                if lv<=2:p.toc_level=lv-1;p.toc_key=f'h{hi}'
                story.append(p)
            elif kind=='p':story.append(Paragraph(b['text'],body))
            elif kind=='label':story.append(Paragraph(b['text'],ParagraphStyle('label',parent=caption,fontName='heading',keepWithNext=True)))
            elif kind=='math':
                d=svg2rlg(str(tmp/f'f{mi}.svg'));mi+=1
                if d.width>width:raise ValueError('Formula wider than column: break or rearrange formula, do not squash it')
                d.hAlign='CENTER';story.append(KeepTogether([Spacer(1,style['formula_space_before']),d,Spacer(1,style['formula_space_after'])]))
            elif kind=='table':
                ratios=b.get('widths',[1]*len(b['rows'][0]));ws=[width*x/sum(ratios) for x in ratios]
                t=Table([[Paragraph(c,cell) for c in row] for row in b['rows']],colWidths=ws,repeatRows=1,hAlign='LEFT')
                t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor(style['table_header_color'])),('LINEABOVE',(0,0),(-1,0),.6,C),('LINEBELOW',(0,0),(-1,0),.4,C),('LINEBELOW',(0,-1),(-1,-1),.6,C),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]));story.extend([t,Spacer(1,6)])
            else:raise ValueError('Unknown block '+kind)
        doc.multiBuild(story)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('source',type=Path);p.add_argument('output',type=Path);p.add_argument('--fonts',required=True,type=Path);p.add_argument('--style',type=Path,default=Path(__file__).resolve().parents[1]/'assets/templates/compact-review.json');p.add_argument('--node',default='node');p.add_argument('--mathjax',type=Path)
    a=p.parse_args();a.output.parent.mkdir(parents=True,exist_ok=True)
    build(json.loads(a.source.read_text()),a.output,json.loads(a.fonts.read_text()),json.loads(a.style.read_text()),a.node,a.mathjax)
