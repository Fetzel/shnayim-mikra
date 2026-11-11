"""Assemble the Android web bundle: wrap the page in a full HTML document and copy data + fonts."""
import shutil, os, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = root / 'src'
out = root / 'dist'
shutil.rmtree(out, ignore_errors=True); out.mkdir()
body = (src / 'index.html').read_text(encoding='utf-8')
head = ('<!doctype html><html lang="he"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,user-scalable=no">'
        '<meta name="theme-color" content="#f6f5f1">'
        '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style></head><body>')
(out / 'index.html').write_text(head + body + '</body></html>', encoding='utf-8')
for d in ('data', 'fonts'):
    shutil.copytree(src / d, out / d)
print('built', out)
