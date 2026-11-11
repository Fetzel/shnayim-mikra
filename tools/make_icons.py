from PIL import Image, ImageDraw, ImageFont
import pathlib
res = pathlib.Path('android/app/src/main/res')
BG = (44, 74, 124); FG = (251, 246, 233)
font_path = 'src/fonts/ShlomoStam.ttf'
def glyph_img(size, scale):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(font_path, int(size * scale))
    t = 'ש'
    bb = d.textbbox((0, 0), t, font=f)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    d.text(((size - w) / 2 - bb[0], (size - h) / 2 - bb[1]), t, font=f, fill=FG)
    return img
dens = {'mdpi': 1, 'hdpi': 1.5, 'xhdpi': 2, 'xxhdpi': 3, 'xxxhdpi': 4}
for k, m in dens.items():
    fg = int(108 * m); glyph_img(fg, 0.42).save(res / f'mipmap-{k}' / 'ic_launcher_foreground.png')
    L = int(48 * m)
    sq = Image.new('RGBA', (L, L), (0, 0, 0, 0)); d = ImageDraw.Draw(sq)
    d.rounded_rectangle([0, 0, L - 1, L - 1], radius=int(L * 0.22), fill=BG)
    sq.alpha_composite(glyph_img(L, 0.62)); sq.save(res / f'mipmap-{k}' / 'ic_launcher.png')
    rd = Image.new('RGBA', (L, L), (0, 0, 0, 0)); d = ImageDraw.Draw(rd)
    d.ellipse([0, 0, L - 1, L - 1], fill=BG); rd.alpha_composite(glyph_img(L, 0.58)); rd.save(res / f'mipmap-{k}' / 'ic_launcher_round.png')
(res / 'values' / 'ic_launcher_background.xml').write_text('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#2C4A7C</color>\n</resources>\n')
big = Image.new('RGBA', (512, 512), BG); big.alpha_composite(glyph_img(512, 0.62)); big.save('icon-512.png')
print('icons done')
