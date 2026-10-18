"""Cartoon pigs and paddock scenes for the pig example (illustrations, nothing to license). Same look as example_art.py:
800 x 600, supersampled, with a small SAMPLE IMAGE tag. Used by make_pig_example.py."""
import math, random
from PIL import Image, ImageDraw
import example_art as A
from example_art import S, W, H, E, P, L, R, shade, canvas, finish

PIG = {  # body, belly/ear shade, optional white belt
    'ginger': dict(body=(214, 142, 74), dark=(170, 100, 48), belt=False),
    'black': dict(body=(46, 46, 52), dark=(24, 24, 30), belt=False),
    'bw': dict(body=(44, 44, 50), dark=(24, 24, 30), belt=True),
    'cream': dict(body=(238, 214, 170), dark=(200, 170, 120), belt=False),
    'spotted': dict(body=(232, 200, 160), dark=(120, 80, 54), belt=False, spots=True),
}
PINK = (240, 168, 160)

def _mask_paste(im, mask_fn, color):
    m = Image.new('L', im.size, 0); md = ImageDraw.Draw(m); mask_fn(md); im.paste(color, (0, 0), m)

def pig(im, d, cx, cy, k, pal='ginger', facing=1, young=False, tassels=True, seed=0):
    """A Kunekune: round, short-legged, short upturned snout, ears flopped forward, tassels under the chin."""
    f = facing; c = PIG[pal]; body, dark = c['body'], c['dark']
    if young: k *= 0.52
    rnd = random.Random(seed)
    E(d, cx, cy + 112 * k, 112 * k, 14 * k, (70, 100, 50))   # ground shadow
    for dx in (-62, -22, 40, 80):                                                              # legs
        far = dx in (-22, 80); col = shade(body, 0.8) if far else body
        R(d, cx + dx * k - 14 * k, cy + 36 * k, cx + dx * k + 14 * k, cy + 104 * k, col, r=10 * k)
        R(d, cx + dx * k - 15 * k, cy + 94 * k, cx + dx * k + 15 * k, cy + 108 * k, (52, 40, 34), r=6 * k)
    # curly tail
    tx, ty = cx - f * 104 * k, cy - 14 * k
    L(d, [(tx, ty), (tx - f * 14 * k, ty - 18 * k), (tx - f * 4 * k, ty - 34 * k), (tx - f * 18 * k, ty - 38 * k)], dark, 7 * k)
    E(d, cx, cy, 108 * k, 70 * k, body)
    if c.get('belt'):
        band = Image.new('L', im.size, 0); bd = ImageDraw.Draw(band)
        bd.ellipse(((cx - 108 * k) * S, (cy - 70 * k) * S, (cx + 108 * k) * S, (cy + 70 * k) * S), fill=255)
        cut = Image.new('L', im.size, 0); cd = ImageDraw.Draw(cut)
        cd.rectangle(((cx + f * 22 * k - 26 * k) * S, 0, (cx + f * 22 * k + 26 * k) * S, H * S), fill=255)
        from PIL import ImageChops
        im.paste((246, 244, 238), (0, 0), ImageChops.multiply(band, cut))
    if c.get('spots'):
        for _ in range(7):
            a = rnd.random() * 6.28; r = rnd.random() * 0.7
            E(d, cx + math.cos(a) * 80 * k * r, cy + math.sin(a) * 40 * k * r, rnd.randint(12, 22) * k, rnd.randint(10, 18) * k, dark)
    E(d, cx - f * 8 * k, cy - 22 * k, 80 * k, 28 * k, shade(body, 1.12))
    # head
    hx, hy = cx + f * 96 * k, cy - 4 * k
    E(d, hx, hy, 50 * k, 46 * k, body)
    E(d, hx + f * 40 * k, hy + 14 * k, 22 * k, 20 * k, PINK)                                    # short snout
    E(d, hx + f * 46 * k, hy + 12 * k, 4 * k, 6 * k, (150, 80, 84)); E(d, hx + f * 36 * k, hy + 14 * k, 4 * k, 6 * k, (150, 80, 84))
    P(d, [(hx - f * 6 * k, hy - 38 * k), (hx + f * 36 * k, hy - 22 * k), (hx + f * 30 * k, hy + 6 * k), (hx - f * 18 * k, hy - 8 * k)], dark)   # flopped ear
    E(d, hx + f * 22 * k, hy - 12 * k, 6 * k, 7 * k, (22, 22, 22)); E(d, hx + f * 24 * k, hy - 14 * k, 2 * k, 2 * k, (255, 255, 255))
    if tassels:
        for dx in (14, 28):
            E(d, hx + f * dx * k, hy + 46 * k, 6 * k, 13 * k, (214, 150, 150) if pal != 'black' else (190, 120, 120))
    return im

def ground(kind, seed=1):
    rnd = random.Random(seed)
    if kind == 'orchard':
        im, d = canvas((190, 220, 240), (126, 176, 96)); A.grass(im, d, 360)
        for x, y in [(110, 190), (700, 170)]:
            R(d, x - 12, y, x + 12, y + 210, (96, 70, 48)); E(d, x, y - 10, 90, 78, (70, 130, 64)); E(d, x - 30, y - 30, 50, 44, (86, 150, 74))
            for _ in range(8): E(d, x + rnd.randint(-60, 60), y + rnd.randint(-50, 40), 7, 7, (214, 60, 50))
        return im, d, 400
    if kind == 'mud':
        im, d = canvas((206, 222, 236), (150, 130, 96)); A.grass(im, d, 330)
        E(d, 400, 500, 360, 70, (112, 84, 60)); E(d, 400, 496, 320, 56, (126, 96, 70))
        return im, d, 460
    if kind == 'evening':
        im, d = canvas((248, 212, 160), (150, 176, 112)); A.grass(im, d, 380); E(d, 650, 150, 58, 58, (255, 238, 196))
        return im, d, 430
    im, d = canvas((190, 220, 240), (126, 176, 96)); A.grass(im, d, 360)
    return im, d, 420

def img_pig(pal='ginger', seed=1, facing=1, scene='paddock', young=False, tassels=True):
    im, d, y = ground(scene, seed)
    pig(im, d, 400, 380 if not young else 420, 1.35 if not young else 1.9, pal, facing, young, tassels, seed)
    return finish(im)

def img_litter(pals=('ginger', 'ginger', 'bw', 'ginger', 'black', 'ginger'), seed=1, scene='paddock'):
    im, d, y = ground(scene, seed)
    spots = [(150, 400, 1), (300, 440, -1), (450, 410, 1), (600, 450, -1), (230, 500, 1), (520, 510, -1), (690, 410, 1), (380, 520, 1)]
    for (x, yy, f), p in zip(sorted(spots[:len(pals)], key=lambda s: s[1]), pals):
        pig(im, d, x, yy - 20, 1.0, p, f, True, True, seed + x)
    return finish(im)

def img_sow_litter(sow='ginger', kids=('ginger', 'ginger', 'bw', 'ginger'), seed=1):
    im, d, y = ground('paddock', seed)
    pig(im, d, 270, 360, 1.25, sow, 1, False, True, seed)
    for i, p in enumerate(kids):
        pig(im, d, 530 + (i % 2) * 120 - 20, 440 + (i // 2) * 60 - 20, 0.95, p, -1 if i % 2 else 1, True, True, seed + i)
    return finish(im)

def hut(d, x, y, k=1.0):
    P(d, [(x - 130 * k, y), (x, y - 90 * k), (x + 130 * k, y)], (96, 100, 108)); P(d, [(x - 130 * k, y), (x + 130 * k, y), (x + 130 * k, y + 14 * k), (x - 130 * k, y + 14 * k)], (70, 74, 80))
    R(d, x - 110 * k, y + 14 * k, x + 110 * k, y + 120 * k, (150, 98, 60), r=4); R(d, x - 36 * k, y + 40 * k, x + 36 * k, y + 120 * k, (40, 30, 26), r=18 * k)

def img_hut(name='Farrowing hut'):
    im, d, y = ground('paddock', 3)
    hut(d, 330, 250, 1.5)
    for x in range(560, 780, 34): L(d, [(x, 330), (x, 450)], (140, 110, 70), 5)
    L(d, [(560, 345), (780, 345)], (140, 110, 70), 5); L(d, [(560, 430), (780, 430)], (140, 110, 70), 5)
    pig(im, d, 640, 440, 0.5, 'ginger', -1, False, True, 5)
    return finish(im)

def img_paddock(pal=('ginger', 'black'), scene='paddock'):
    im, d, y = ground(scene, 6)
    for x in range(30, 790, 56): L(d, [(x, 300), (x, 420)], (150, 120, 80), 7)
    L(d, [(20, 320), (790, 320)], (150, 120, 80), 6); L(d, [(20, 380), (790, 380)], (150, 120, 80), 6)
    pig(im, d, 250, 470, 0.9, pal[0], 1, False, True, 7); pig(im, d, 560, 490, 0.8, pal[1], -1, False, True, 8)
    return finish(im)

def img_feed():
    im, d = canvas((240, 232, 214), (210, 196, 170)); A.wood(im, d, 320)
    R(d, 230, 190, 570, 470, (226, 206, 160), r=20, outline=(170, 140, 96), w=5)
    R(d, 260, 250, 540, 360, (78, 118, 72), r=8)
    A.text(d, (400, 290), 'PIG GROWER', A.font(A.FB, 38), (255, 255, 255), 'mm'); A.text(d, (400, 336), 'EXAMPLE FEEDS CO', A.font(A.FR, 22), (230, 240, 224), 'mm')
    A.text(d, (400, 420), '20 kg', A.font(A.FB, 30), (96, 70, 44), 'mm')
    return finish(im)

def img_scales():
    im, d, y = ground('paddock', 9)
    R(d, 230, 330, 570, 500, (120, 124, 130), r=12); R(d, 270, 410, 530, 450, (50, 56, 62), r=6)
    A.text(d, (400, 430), '86.5 kg', A.font(A.FB, 22), (150, 250, 160), 'mm')
    pig(im, d, 400, 296, 0.75, 'bw', 1, False, True, 10)
    return finish(im)

if __name__ == '__main__':
    import sys, os
    out = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
    for n, im in [('pig_ginger', img_pig('ginger')), ('pig_bw', img_pig('bw', scene='orchard')), ('pig_black', img_pig('black', scene='mud', facing=-1)), ('litter', img_litter()), ('sowlitter', img_sow_litter()),
                  ('hut', img_hut()), ('paddock', img_paddock()), ('feed', img_feed()), ('scales', img_scales())]:
        im.save(os.path.join(out, n + '.png'))
