# Ascend training terms page. Turns legal/training-terms.md into terms.html
# (served at /terms, vercel.json has cleanUrls). The text is published exactly
# as written in the markdown; edit the markdown, never the HTML.
# Run: python3 build/terms.py → terms.html
#
# The look comes from the landing page: the stylesheet (LANDING_CSS) and the
# site URL (SITE) are read out of build/landing.py so there is one place to
# change them, and the logo mark is the same lib.mark(). Standard library only.
import sys, os, re, html as H
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(here, '..')
sys.path.insert(0, here)
from lib import mark

landing_src = open(os.path.join(here, 'landing.py'), encoding='utf-8').read()
LANDING_CSS = re.search(r'LANDING_CSS = r"""(.*?)"""', landing_src, re.S).group(1)
SITE = re.search(r'^SITE = "([^"]+)"', landing_src, re.M).group(1)

TERMS_CSS = r"""
.lg{display:block;width:100%;height:auto}
.top .brand{color:inherit;text-decoration:none}
.terms{max-width:720px;padding-block:28px 64px}
.terms h1{font-size:clamp(30px,4.4vw,44px);margin:0 0 16px}
.terms h2{font-size:22px;margin:34px 0 8px}
.terms p{margin-top:10px;font-size:16px;line-height:1.6}
.terms p.meta{font-size:14px;color:var(--muted)}
.terms ul{margin:10px 0 0 20px;display:grid;gap:8px;font-size:16px;line-height:1.6;max-width:65ch}
.terms li::marker{color:var(--accent)}
"""

def md_to_html(md):
    """The small subset of markdown the terms use: # and ## headings, paragraphs,
    '- ' lists. Lines that follow each other inside a paragraph keep their line break."""
    out, para, items = [], [], []
    first_para = [True]
    def flush():
        if para:
            cls = ' class="meta"' if first_para[0] else ''
            first_para[0] = False
            out.append(f'<p{cls}>' + '<br>\n'.join(H.escape(l, quote=False) for l in para) + '</p>')
            para.clear()
        if items:
            out.append('<ul>\n' + '\n'.join(f'<li>{H.escape(i, quote=False)}</li>' for i in items) + '\n</ul>')
            items.clear()
    for line in md.splitlines():
        line = line.strip()
        if not line: flush()
        elif line.startswith('## '): flush(); out.append(f'<h2>{H.escape(line[3:], quote=False)}</h2>')
        elif line.startswith('# '): flush(); out.append(f'<h1>{H.escape(line[2:], quote=False)}</h1>')
        elif line.startswith('- '):
            if para: flush()
            items.append(line[2:])
        else:
            if items: flush()
            para.append(line)
    flush()
    return '\n'.join(out)

md = open(os.path.join(root, 'legal', 'training-terms.md'), encoding='utf-8').read()
title = re.search(r'^# (.+)$', md, re.M).group(1).strip()
DESC = "The training terms and risk acknowledgement for Ascend, a strength coaching app."

doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
  '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
  f'<title>{H.escape(title)} | Ascend</title>'
  f'<meta name="description" content="{H.escape(DESC)}">'
  '<meta name="theme-color" content="#F4EFE4">'
  '<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">'
  '<link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">'
  f'<link rel="canonical" href="{SITE}/terms"><meta name="robots" content="index,follow">'
  '<link rel="preconnect" href="https://fonts.googleapis.com">'
  '<link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@500;600;700&display=swap" rel="stylesheet">'
  f'<style>{LANDING_CSS}{TERMS_CSS}</style></head><body>\n'
  '<div class="wrap">\n'
  f'<div class="top"><a class="brand" href="/">{mark(30)}Ascend</a><a class="cta" href="/#apply">Ask for a founding place →</a></div>\n'
  f'<main class="terms">\n{md_to_html(md)}\n</main>\n'
  '<footer>\n'
  f'  <div class="brand" style="font-family:var(--display);font-weight:700;letter-spacing:.14em;text-transform:uppercase;display:flex;align-items:center;gap:10px">{mark(22)}Ascend</div>\n'
  '  <p class="legal">© 2026 Full Canvas Digital s.r.o., Prague · <a href="/terms">Terms</a> · Privacy · Contact</p>\n'
  '</footer>\n'
  '</div>\n</body></html>\n')
open(os.path.join(root, 'terms.html'), 'w', encoding='utf-8').write(doc)
print(len(doc), 'bytes terms.html')
