"""Simple illustrated pictures for the built-in examples (no real photos, so nothing to license).
Every picture carries a small SAMPLE tag so nobody mistakes it for a real record.
All functions return an RGB PIL image, 800 x 600."""
import math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, S = 800, 600, 2          # output size, supersample factor
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FR = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FS = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
def font(p, n): return ImageFont.truetype(p, int(n * S))

def canvas(top, bottom):
    im = Image.new('RGB', (W * S, H * S)); d = ImageDraw.Draw(im)
    for y in range(H * S):
        t = y / (H * S); d.line([(0, y), (W * S, y)], fill=tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)))
    return im, d

def finish(im, tag=True):
    im = im.resize((W, H), Image.LANCZOS)
    if tag:
        d = ImageDraw.Draw(im, 'RGBA'); f = ImageFont.truetype(FB, 13)
        tw = d.textlength('SAMPLE IMAGE', font=f)
        d.rounded_rectangle((W - tw - 30, H - 34, W - 10, H - 10), radius=6, fill=(31, 53, 87, 190))
        d.text((W - tw - 20, H - 31), 'SAMPLE IMAGE', font=f, fill=(255, 255, 255, 235))
    return im

def E(d, cx, cy, rx, ry, fill, outline=None, w=0):
    d.ellipse(((cx - rx) * S, (cy - ry) * S, (cx + rx) * S, (cy + ry) * S), fill=fill, outline=outline, width=int(w * S))
def P(d, pts, fill, outline=None):
    d.polygon([(x * S, y * S) for x, y in pts], fill=fill, outline=outline)
def L(d, pts, fill, w):
    d.line([(x * S, y * S) for x, y in pts], fill=fill, width=int(w * S), joint='curve')
def R(d, x0, y0, x1, y1, fill, r=0, outline=None, w=0):
    d.rounded_rectangle((x0 * S, y0 * S, x1 * S, y1 * S), radius=r * S, fill=fill, outline=outline, width=int(w * S))
def shade(c, k): return tuple(max(0, min(255, int(v * k))) for v in c)
def text(d, xy, s, f, fill, anchor='la'): d.text((xy[0] * S, xy[1] * S), s, font=f, fill=fill, anchor=anchor)

# ------------------------------------------------------------------ backgrounds
def wood(im, d, y0=360):
    for y in range(int(y0 * S), H * S):
        t = (y - y0 * S) / (H * S - y0 * S); c = (int(150 - 40 * t), int(108 - 30 * t), int(70 - 20 * t)); d.line([(0, y), (W * S, y)], fill=c)
    rnd = random.Random(4)
    for _ in range(60):
        y = rnd.randint(int(y0 * S) + 10, H * S - 4); x = rnd.randint(0, W * S); d.line([(x, y), (x + rnd.randint(200, 800), y + rnd.randint(-3, 3))], fill=(110, 78, 50), width=2)

def grass(im, d, y0=330):
    for y in range(int(y0 * S), H * S):
        t = (y - y0 * S) / (H * S - y0 * S); d.line([(0, y), (W * S, y)], fill=(int(120 - 50 * t), int(170 - 50 * t), int(80 - 30 * t)))
    rnd = random.Random(8)
    for _ in range(420):
        x = rnd.randint(0, W * S); y = rnd.randint(int(y0 * S), H * S); h = rnd.randint(14, 36)
        d.line([(x, y), (x + rnd.randint(-8, 8), y - h)], fill=(70 + rnd.randint(0, 40), 130 + rnd.randint(0, 50), 50), width=3)

# ------------------------------------------------------------------ plants
def leaf(d, x, y, ang, size, col=(60, 130, 60)):
    pts = []
    for t in range(0, 21):
        a = t / 20 * math.pi; r = math.sin(a) * size * 0.45
        pts.append((t / 20 * size, r))
    for t in range(20, -1, -1):
        a = t / 20 * math.pi; r = math.sin(a) * size * 0.45
        pts.append((t / 20 * size, -r))
    ca, sa = math.cos(ang), math.sin(ang)
    P(d, [(x + px * ca - py * sa, y + px * sa + py * ca) for px, py in pts], col)
    L(d, [(x, y), (x + size * ca, y + size * sa)], shade(col, 0.7), 2)

def squash(d, cx, cy, kind, k=1.0):
    """Draw one fruit centred on (cx, cy). kinds: butternut, cheese, tromboncino, buttercup."""
    if kind == 'butternut':
        c = (226, 178, 110)
        R(d, cx - 36 * k, cy - 120 * k, cx + 36 * k, cy + 10 * k, c, r=34 * k)
        E(d, cx, cy + 40 * k, 74 * k, 66 * k, c)
        E(d, cx - 26 * k, cy + 26 * k, 26 * k, 40 * k, shade(c, 1.12))
        R(d, cx - 7 * k, cy - 138 * k, cx + 7 * k, cy - 112 * k, (110, 90, 50), r=4 * k)
    elif kind == 'cheese':
        c = (222, 176, 120)
        E(d, cx, cy + 20 * k, 128 * k, 78 * k, c)
        for i in range(-5, 6):
            L(d, [(cx + i * 22 * k * 0.9, cy - 50 * k + abs(i) * 1.5), (cx + i * 25 * k, cy + 20 * k), (cx + i * 21 * k * 0.9, cy + 90 * k - abs(i) * 2)], shade(c, 0.82), 3)
        E(d, cx - 40 * k, cy - 8 * k, 56 * k, 26 * k, shade(c, 1.1))
        R(d, cx - 10 * k, cy - 74 * k, cx + 10 * k, cy - 52 * k, (110, 90, 50), r=5 * k)
    elif kind == 'tromboncino':
        c = (186, 196, 120)
        pts = [(cx - 120 * k + t * 7 * k, cy - 90 * k + 150 * k * (1 - math.cos(t / 28 * math.pi / 2)) + 14 * math.sin(t / 3)) for t in range(0, 29)]
        L(d, pts, c, 46 * k)
        for (x, y) in pts[::2]: E(d, x, y, 24 * k, 24 * k, c)
        E(d, pts[-1][0] + 20 * k, pts[-1][1] + 6 * k, 56 * k, 52 * k, shade(c, 1.04))
        E(d, pts[-1][0] + 6 * k, pts[-1][1] - 6 * k, 20 * k, 20 * k, shade(c, 1.15))
        R(d, pts[0][0] - 8 * k, pts[0][1] - 26 * k, pts[0][0] + 8 * k, pts[0][1] + 2 * k, (110, 90, 50), r=4 * k)
    else:   # buttercup (C. maxima, turban)
        c = (62, 100, 76)
        E(d, cx, cy + 30 * k, 100 * k, 78 * k, c)
        E(d, cx, cy - 36 * k, 54 * k, 32 * k, (150, 168, 140))
        E(d, cx - 36 * k, cy + 4 * k, 36 * k, 26 * k, shade(c, 1.25))
        for i in range(-4, 5): L(d, [(cx + i * 20 * k, cy - 30 * k), (cx + i * 25 * k, cy + 100 * k)], shade(c, 0.8), 2)

SQUASH_NAMES = {'butternut': 'butternut', 'cheese': 'cheese', 'tromboncino': 'tromboncino', 'buttercup': 'buttercup'}

def img_fruit(kind='butternut', n=1):
    im, d = canvas((244, 233, 214), (225, 210, 186)); wood(im, d)
    E(d, 400, 470, 190, 24, (60, 40, 30, 90))
    if n == 1: squash(d, 400, 330, kind, 1.25)
    else:
        for i, x in enumerate(np_x(n)): squash(d, x, 330 + (i % 2) * 20, kind, 0.8)
    return finish(im)
def np_x(n): return [220 + i * (360 / max(1, n - 1)) for i in range(n)]

def img_harvest(kinds=('butternut', 'cheese', 'butternut', 'cheese', 'butternut')):
    im, d = canvas((236, 228, 206), (205, 190, 160)); wood(im, d, 330)
    R(d, 60, 300, 740, 520, (150, 108, 70), r=14, outline=(100, 70, 44), w=6)
    for i in range(1, 5): L(d, [(60, 300 + i * 44), (740, 300 + i * 44)], (120, 86, 56), 3)
    for x, y, kd in [(180, 340, kinds[0]), (360, 330, kinds[1]), (550, 340, kinds[2]), (270, 380, kinds[3]), (470, 390, kinds[4])]: squash(d, x, y, kd, 0.62)
    return finish(im)

def img_cutopen():
    im, d = canvas((236, 228, 206), (205, 190, 160)); wood(im, d, 340)
    E(d, 400, 330, 250, 190, (214, 120, 40)); E(d, 400, 330, 232, 172, (236, 150, 52)); E(d, 400, 340, 140, 108, (250, 220, 170))
    rnd = random.Random(2)
    for i in range(46):
        a = rnd.random() * 2 * math.pi; r = rnd.random() ** 0.5 * 100
        x, y = 400 + math.cos(a) * r * 1.2, 340 + math.sin(a) * r * 0.9
        E(d, x, y, 12, 7, (252, 244, 220), (205, 190, 150), 1)
    return finish(im)

def img_seedlings():
    im, d = canvas((240, 234, 222), (215, 205, 188)); wood(im, d, 300)
    R(d, 90, 170, 710, 500, (40, 44, 48), r=12)
    cols, rows = 6, 4; cw, ch = 96, 74
    for r in range(rows):
        for c in range(cols):
            x0, y0 = 108 + c * (cw + 3), 188 + r * (ch + 3)
            R(d, x0, y0, x0 + cw, y0 + ch, (86, 62, 46), r=8)
            if (r + c) % 7 != 3:
                sx, sy = x0 + cw / 2, y0 + 20
                L(d, [(sx, y0 + ch - 12), (sx, sy)], (110, 170, 80), 4)
                leaf(d, sx, sy, math.radians(200), 36, (96, 170, 80)); leaf(d, sx, sy, math.radians(-20), 36, (96, 170, 80))
    R(d, 200, 520, 600, 560, (240, 232, 205), r=4); text(d, (400, 528), 'PK-X  tray 1', font(FB, 24), (60, 50, 40), 'ma')
    return finish(im)

def img_flower():
    im, d = canvas((190, 220, 240), (120, 170, 100)); grass(im, d, 380)
    for a in (190, 160, 20, 340): leaf(d, 400, 470, math.radians(a), 220, (56, 120, 56))
    L(d, [(400, 540), (400, 330)], (70, 130, 60), 14)
    for i in range(6):
        a = i / 6 * 2 * math.pi
        P(d, [(400, 300), (400 + math.cos(a - .3) * 120, 300 + math.sin(a - .3) * 110), (400 + math.cos(a) * 150, 300 + math.sin(a) * 140), (400 + math.cos(a + .3) * 120, 300 + math.sin(a + .3) * 110)], (250, 190, 40))
    E(d, 400, 300, 56, 56, (232, 150, 30)); E(d, 400, 300, 26, 26, (180, 100, 20))
    return finish(im)

def img_bed(fruit=True):
    im, d = canvas((200, 224, 240), (140, 180, 110)); grass(im, d, 300)
    R(d, 60, 340, 740, 540, (92, 66, 44), r=6); R(d, 80, 360, 720, 520, (70, 50, 38), r=4)
    rnd = random.Random(3)
    for i in range(14): leaf(d, rnd.randint(110, 690), rnd.randint(400, 490), rnd.random() * 6.28, rnd.randint(110, 170), (60 + rnd.randint(0, 30), 130 + rnd.randint(0, 30), 60))
    if fruit:
        for x, y in [(240, 470), (430, 480), (600, 460)]: squash(d, x, y - 20, 'butternut', 0.32)
    return finish(im)

def img_packet(front=True, name='Waltham Butternut', species='Cucurbita moschata', kind='butternut', brand='EXAMPLE SEEDS CO', col=(214, 130, 54), batch='ES-4471'):
    im, d = canvas((92, 78, 66), (60, 48, 42))
    R(d, 190, 40, 610, 560, (246, 240, 226), r=6)
    P(d, [(190, 40), (230, 62), (270, 40), (310, 62), (350, 40), (390, 62), (430, 40), (470, 62), (510, 40), (550, 62), (590, 40), (610, 40), (610, 80), (190, 80)], shade((246, 240, 226), 0.95))
    R(d, 190, 84, 610, 150, col)
    text(d, (400, 100), brand, font(FB, 24), (255, 255, 255), 'ma')
    if front:
        text(d, (400, 176), name.upper(), font(FS, 31 if len(name) < 17 else 24), (50, 40, 30), 'ma')
        text(d, (400, 224), species, font(FR, 19), (110, 90, 70), 'ma')
        R(d, 220, 262, 580, 470, shade(col, 1.45), r=10); squash(d, 400, 398, kind, 0.7)
        text(d, (400, 494), 'Open pollinated  |  10 seeds', font(FB, 19), (60, 50, 40), 'ma')
        text(d, (400, 524), 'Sow Sep to Dec', font(FR, 18), (110, 90, 70), 'ma')
    else:
        text(d, (400, 170), 'GROWING GUIDE', font(FB, 22), (50, 40, 30), 'ma')
        for i, s in enumerate(['Sow 2 cm deep after frost.', 'Space plants 1.5 m apart.', 'Needs full sun and rich soil.', 'Harvest 100 to 120 days.', 'Cure fruit 2 weeks before storing.']):
            text(d, (226, 214 + i * 40), s, font(FR, 19), (80, 66, 52))
        rnd = random.Random(5)
        for i in range(48): R(d, 226 + i * 7, 440, 226 + i * 7 + rnd.choice([2, 3, 4]), 500, (40, 34, 30))
        text(d, (226, 510), f'Batch {batch}   Packed 2023', font(FR, 16), (110, 90, 70))
    return finish(im)

# ------------------------------------------------------------------ animals
def hen(d, cx, cy, k, body=(40, 40, 46), sheen=(70, 76, 90), comb=(200, 40, 40), face=(190, 50, 50), facing=1, tail=True):
    f = facing
    if tail:
        for a, ln in [(-60, 90), (-40, 100), (-20, 92), (-75, 70)]:
            ang = math.radians(a if f == 1 else 180 - a)
            P(d, [(cx - f * 60 * k, cy - 20 * k), (cx - f * 60 * k + math.cos(ang) * ln * k - 16 * k, cy - 20 * k + math.sin(ang) * ln * k), (cx - f * 60 * k + math.cos(ang) * ln * k + 16 * k, cy - 20 * k + math.sin(ang) * ln * k + 8 * k)], shade(body, 0.85))
    E(d, cx, cy, 96 * k, 66 * k, body)
    E(d, cx - f * 10 * k, cy - 14 * k, 62 * k, 30 * k, sheen)
    E(d, cx - f * 24 * k, cy + 4 * k, 52 * k, 34 * k, shade(body, 0.8))
    E(d, cx + f * 74 * k, cy - 52 * k, 36 * k, 38 * k, body)
    for i, (dx, dy) in enumerate([(66, -88), (78, -94), (90, -86)]): E(d, cx + f * dx * k, cy + dy * k, 10 * k, 14 * k, comb)
    P(d, [(cx + f * 104 * k, cy - 56 * k), (cx + f * 128 * k, cy - 48 * k), (cx + f * 104 * k, cy - 42 * k)], (236, 170, 50))
    E(d, cx + f * 96 * k, cy - 34 * k, 8 * k, 14 * k, face)
    E(d, cx + f * 84 * k, cy - 58 * k, 5 * k, 5 * k, (20, 20, 20))
    for dx in (-12, 20): L(d, [(cx + dx * k, cy + 60 * k), (cx + dx * k, cy + 110 * k)], (214, 150, 60), 6 * k); L(d, [(cx + dx * k, cy + 110 * k), (cx + (dx + 22 * f) * k, cy + 112 * k)], (214, 150, 60), 5 * k)

HEN_COLS = {'black': ((34, 36, 40), (66, 78, 86)), 'blue': ((108, 120, 140), (150, 162, 180)), 'brown': ((170, 96, 50), (200, 130, 70)), 'white': ((236, 232, 224), (250, 248, 242))}

def img_hen(kind='black', facing=1):
    im, d = canvas((196, 222, 238), (130, 178, 100)); grass(im, d, 400)
    E(d, 400, 520, 170, 20, (50, 80, 40, 120)); b, s = HEN_COLS[kind]
    hen(d, 400, 380, 1.5, b, s, facing=facing)
    return finish(im)

def img_flock(kinds=('black', 'blue', 'blue', 'black', 'blue')):
    im, d = canvas((196, 222, 238), (130, 178, 100)); grass(im, d, 340)
    spots = [(170, 430, 0.8, 1), (330, 400, 0.7, -1), (500, 440, 0.85, 1), (650, 410, 0.65, -1), (410, 500, 0.9, 1)]
    for (x, y, k, f), kd in zip(sorted(spots, key=lambda s: s[1]), kinds):
        b, s = HEN_COLS[kd]; hen(d, x, y, k, b, s, facing=f)
    return finish(im)

def img_chick(col=(250, 214, 80)):
    im, d = canvas((246, 232, 200), (226, 204, 160))
    R(d, 90, 150, 710, 540, (200, 170, 120), r=20, outline=(160, 130, 90), w=6)
    E(d, 400, 500, 140, 18, (130, 100, 70, 120))
    E(d, 400, 380, 120, 100, col); E(d, 400, 250, 74, 70, col)
    E(d, 330, 372, 40, 60, shade(col, 0.9)); E(d, 470, 372, 40, 60, shade(col, 0.9))
    P(d, [(386, 262), (414, 262), (400, 286)], (240, 150, 50))
    E(d, 372, 236, 8, 9, (20, 20, 20)); E(d, 428, 236, 8, 9, (20, 20, 20))
    for dx in (-30, 30): L(d, [(400 + dx, 470), (400 + dx, 520)], (230, 150, 60), 6)
    return finish(im)

def img_eggs(cols=((120, 190, 190),) * 6, tray=True):
    im, d = canvas((240, 232, 214), (210, 196, 170)); wood(im, d, 320)
    R(d, 90, 200, 710, 480, (214, 200, 170), r=14, outline=(170, 150, 120), w=4)
    k = 0
    for r in range(2):
        for c in range(3):
            x, y = 220 + c * 180, 290 + r * 120; col = cols[k % len(cols)]; k += 1
            E(d, x, y + 8, 56, 66, shade(col, 0.82)); E(d, x, y, 54, 66, col); E(d, x - 18, y - 22, 16, 24, shade(col, 1.18))
    return finish(im)

def img_coop(name='Coop A'):
    im, d = canvas((196, 222, 238), (130, 178, 100)); grass(im, d, 360)
    R(d, 120, 210, 420, 440, (176, 70, 50), r=6); P(d, [(100, 220), (270, 120), (440, 220)], (110, 60, 50))
    R(d, 230, 330, 310, 440, (60, 40, 30), r=6); R(d, 160, 260, 210, 310, (240, 224, 150), r=4)
    for x in range(430, 740, 34): L(d, [(x, 330), (x, 450)], (140, 110, 70), 5)
    L(d, [(430, 340), (740, 340)], (140, 110, 70), 5); L(d, [(430, 440), (740, 440)], (140, 110, 70), 5)
    b, s = HEN_COLS['blue']; hen(d, 590, 440, 0.55, b, s, facing=-1)
    return finish(im)

def img_pen():
    im, d = canvas((196, 222, 238), (130, 178, 100)); grass(im, d, 340)
    for x in range(60, 760, 40): L(d, [(x, 330), (x, 470)], (150, 120, 80), 6)
    L(d, [(60, 350), (760, 350)], (150, 120, 80), 6); L(d, [(60, 450), (760, 450)], (150, 120, 80), 6)
    b, s = HEN_COLS['black']; hen(d, 260, 480, 0.7, b, s, facing=1); b2, s2 = HEN_COLS['blue']; hen(d, 520, 490, 0.62, b2, s2, facing=-1)
    return finish(im)

def save_pair(im, full_q=68):
    import io, base64
    def b64(i, q):
        buf = io.BytesIO(); i.save(buf, 'JPEG', quality=q, optimize=True); return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
    th = im.copy(); th.thumbnail((220, 220)); return b64(im, full_q), b64(th, 62)
