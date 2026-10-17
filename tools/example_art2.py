"""More sample illustrations for the built-in examples: one picture for each bird and each plant, so lists and cards are never blank.
Original cartoon art drawn here (no photos, no licensed images). Every picture carries the SAMPLE IMAGE tag, like the rest.
Uses the helpers in example_art.py."""
import math, random
from PIL import Image, ImageDraw
import example_art as A
from example_art import E, P, L, R, shade, canvas, finish, S, W, H

# ------------------------------------------------------------------ palettes: body, sheen, hackle (neck feathers), tail
PAL = {
    'black':   dict(body=(34, 36, 40),    sheen=(66, 78, 86),    hackle=(44, 54, 60),   tail=(30, 52, 48)),
    'blue':    dict(body=(108, 120, 140), sheen=(150, 162, 180), hackle=(88, 100, 122), tail=(70, 82, 104)),
    'splash':  dict(body=(232, 230, 226), sheen=(250, 248, 244), hackle=(214, 216, 220), tail=(190, 196, 208), blotch=(132, 146, 170)),
    'welsummer': dict(body=(168, 96, 50), sheen=(200, 132, 72), hackle=(226, 156, 62), tail=(38, 70, 58)),
    'maran':   dict(body=(40, 36, 36),    sheen=(70, 64, 62),    hackle=(204, 116, 52), tail=(30, 52, 48)),
    'araucana': dict(body=(122, 128, 142), sheen=(164, 170, 184), hackle=(196, 170, 120), tail=(80, 86, 104)),
    'oliveW':  dict(body=(138, 110, 76),  sheen=(172, 142, 100), hackle=(196, 150, 84), tail=(52, 64, 52)),
    'oliveM':  dict(body=(78, 64, 56),    sheen=(108, 94, 82),   hackle=(150, 98, 58),  tail=(40, 50, 46)),
    'backcross': dict(body=(52, 46, 44),  sheen=(82, 74, 70),    hackle=(176, 104, 54), tail=(34, 50, 46)),
}

def tufts(d, cx, cy, k, f):
    for s in (-1, 1):
        for a in (-0.5, 0, 0.5):
            P(d, [(cx + f * 62 * k, cy - 46 * k), (cx + f * 50 * k + s * 4 * k + a * 34 * k, cy - 78 * k - abs(a) * 8 * k), (cx + f * 70 * k, cy - 54 * k)], (200, 190, 160))

def fowl(d, cx, cy, k, sex, pal, facing=1, young=False, band=None, tuft=False, seed=0):
    """A hen or a rooster. sex: 'F' or 'M'. young: smaller, shorter comb and tail (pullet or cockerel)."""
    f = facing; rnd = random.Random(seed); p = PAL[pal]; body, sheen, hackle, tail = p['body'], p['sheen'], p['hackle'], p['tail']
    k = k * (0.8 if young else 1.0)
    male = sex == 'M'
    # tail
    if male:
        n = 3 if young else 5
        for i in range(n):
            a = -70 + i * (-14 if not young else -10)
            pts = []
            for t in range(0, 12):
                u = t / 11; r = (60 + 90 * u) * k
                ang = math.radians(a - 28 * u * u * 1.0)
                x = cx - f * (54 * k) + f * (-math.cos(ang) * r) * -1 * -1
                pts.append((cx - f * 52 * k - f * math.cos(math.radians(a * 0.5)) * r * 0.55 - f * u * 28 * k, cy - 20 * k + math.sin(math.radians(a)) * r * 0.95 + u * u * 36 * k))
            L(d, pts, tail if i % 2 == 0 else shade(tail, 1.25), 16 * k)
            L(d, pts, shade(tail, 1.6), 3 * k)
    else:
        for a, ln in [(-62, 84), (-40, 94), (-20, 88), (-78, 66)]:
            ang = math.radians(a if f == 1 else 180 - a)
            P(d, [(cx - f * 60 * k, cy - 20 * k), (cx - f * 60 * k + math.cos(ang) * ln * k - 16 * k, cy - 20 * k + math.sin(ang) * ln * k), (cx - f * 60 * k + math.cos(ang) * ln * k + 16 * k, cy - 20 * k + math.sin(ang) * ln * k)], shade(body, 0.85))
    # body, wing, breast
    E(d, cx, cy, 96 * k, 66 * k, body)
    E(d, cx - f * 10 * k, cy - 14 * k, 62 * k, 30 * k, sheen)
    E(d, cx - f * 24 * k, cy + 4 * k, 52 * k, 34 * k, shade(body, 0.8))
    if 'blotch' in p:
        for _ in range(9):
            E(d, cx + rnd.randint(-70, 60) * k, cy + rnd.randint(-40, 40) * k, rnd.randint(8, 18) * k, rnd.randint(6, 12) * k, p['blotch'])
    if male: E(d, cx + f * 52 * k, cy - 30 * k, 40 * k, 32 * k, hackle)         # saddle of neck feathers
    # neck and head
    E(d, cx + f * 70 * k, cy - 52 * k, 34 * k if not male else 36 * k, 38 * k, hackle if male else body)
    E(d, cx + f * 78 * k, cy - 60 * k, 28 * k, 30 * k, shade(hackle, 1.05) if male else body)
    # comb
    cn = (5 if male and not young else 3 if male else 3)
    combc = (214, 44, 44)
    for i in range(cn):
        dx = 62 + i * (9 if male else 12); dy = -(86 if male else 80) - (6 if (male and not young) else 0) + (abs(i - cn // 2) * 4)
        E(d, cx + f * dx * k, cy + dy * k, 9 * k if male else 8 * k, (17 if male and not young else 12) * k, combc)
    # beak, wattle, eye
    P(d, [(cx + f * 104 * k, cy - 62 * k), (cx + f * 128 * k, cy - 52 * k), (cx + f * 104 * k, cy - 46 * k)], (236, 170, 50))
    E(d, cx + f * 96 * k, cy - 36 * k, 8 * k, (18 if male else 12) * k, (200, 56, 56))
    E(d, cx + f * 86 * k, cy - 64 * k, 5 * k, 5 * k, (20, 20, 20)); E(d, cx + f * 88 * k, cy - 66 * k, 1.6 * k, 1.6 * k, (255, 255, 255))
    if tuft: tufts(d, cx, cy, k, f)
    # legs and leg band
    for i, dx in enumerate((-12, 20)):
        L(d, [(cx + dx * k, cy + 60 * k), (cx + dx * k, cy + 110 * k)], (214, 150, 60), 6 * k)
        L(d, [(cx + dx * k, cy + 110 * k), (cx + (dx + 22 * f) * k, cy + 112 * k)], (214, 150, 60), 5 * k)
        if band and i == 1: R(d, cx + dx * k - 5 * k, cy + 78 * k, cx + dx * k + 5 * k, cy + 92 * k, band, r=2 * k)

BANDS = {'P': (230, 60, 60), 'F1': (60, 130, 220), 'F2': (240, 200, 50), 'F3': (60, 170, 90), 'BC': (170, 90, 200), 'X': (240, 130, 40)}

def backdrop(kind, seed):
    rnd = random.Random(seed)
    if kind == 'run':      # bare earth run
        im, d = canvas((206, 226, 240), (214, 196, 150)); y0 = 380
        for y in range(y0 * S, H * S):
            t = (y - y0 * S) / (H * S - y0 * S); d.line([(0, y), (W * S, y)], fill=(int(196 - 40 * t), int(166 - 40 * t), int(116 - 30 * t)))
        for _ in range(60): x, y = rnd.randint(0, W * S), rnd.randint(y0 * S, H * S); d.ellipse((x, y, x + rnd.randint(6, 22), y + rnd.randint(4, 10)), fill=(150, 120, 84))
        return im, d, y0
    if kind == 'fence':
        im, d = canvas((196, 222, 238), (130, 178, 100)); A.grass(im, d, 380)
        for x in range(30, 800, 70): L(d, [(x, 250), (x, 400)], (160, 130, 90), 9)
        L(d, [(0, 290), (800, 290)], (150, 120, 84), 8); L(d, [(0, 350), (800, 350)], (150, 120, 84), 8)
        return im, d, 400
    if kind == 'evening':
        im, d = canvas((246, 206, 156), (168, 184, 120)); A.grass(im, d, 390)
        E(d, 640, 150, 60, 60, (255, 236, 190))
        return im, d, 400
    im, d = canvas((196, 222, 238), (130, 178, 100)); A.grass(im, d, 380)
    return im, d, 400

def img_bird(pal='black', sex='F', role='adult', seed=1, gen='P', facing=None, scene=None, tuft=False):
    """One bird, standing on its own. role: adult or young (pullet/cockerel)."""
    rnd = random.Random(seed)
    sc = scene or rnd.choice(['yard', 'yard', 'run', 'fence', 'evening'])
    im, d, gy = backdrop(sc, seed)
    f = facing or rnd.choice([1, -1]); k = 1.3
    cy = 322 + rnd.randint(-8, 8); x = 400 + rnd.randint(-40, 40); kk = k * (0.8 if role != 'adult' else 1.0)
    E(d, x, cy + 112 * kk + 8, 150 * (0.85 if role != 'adult' else 1), 18, (50, 60, 40, 110))
    fowl(d, x, cy, k, sex, pal, f, young=(role != 'adult'), band=BANDS.get(gen), tuft=tuft, seed=seed)
    return finish(im)

def chick_at(d, x, y, k, col, seed=0):
    rnd = random.Random(seed)
    E(d, x, y + 56 * k, 46 * k, 8 * k, (90, 70, 40, 90))
    E(d, x, y, 44 * k, 38 * k, col); E(d, x + 20 * k, y - 28 * k, 26 * k, 25 * k, col)
    P(d, [(x + 40 * k, y - 32 * k), (x + 56 * k, y - 26 * k), (x + 40 * k, y - 20 * k)], (240, 150, 50))
    E(d, x + 28 * k, y - 34 * k, 3.4 * k, 3.6 * k, (20, 20, 20))
    E(d, x - 8 * k, y + 2 * k, 20 * k, 14 * k, shade(col, 0.88))
    for dx in (-8, 10): L(d, [(x + dx * k, y + 34 * k), (x + dx * k, y + 54 * k)], (230, 150, 60), 3 * k)

def img_chicks(n=3, pal='black', seed=1):
    """A few young chicks in a brooder box."""
    cols = {'black': (62, 62, 66), 'blue': (150, 156, 170), 'splash': (236, 234, 226), 'olive': (216, 184, 100), 'yellow': (250, 214, 80)}
    rnd = random.Random(seed)
    im, d = canvas((246, 232, 200), (226, 204, 160))
    R(d, 70, 130, 730, 550, (205, 176, 128), r=20, outline=(160, 130, 90), w=6)
    R(d, 90, 150, 710, 530, (232, 214, 168), r=12)
    for i in range(n):
        x = 160 + (i + 0.5) * (480 / max(n, 1)) + rnd.randint(-20, 20); y = 330 + rnd.randint(-40, 60)
        chick_at(d, x, y, 1.7 if n <= 4 else 1.25, cols.get(pal, cols['yellow']) if pal != 'mixed' else rnd.choice(list(cols.values())), seed + i)
    return finish(im)

def img_group(pal_list, sexes, seed=1, scene='yard'):
    im, d, gy = backdrop(scene, seed); rnd = random.Random(seed)
    n = len(pal_list); xs = [130 + i * (540 / max(n - 1, 1)) for i in range(n)]
    order = sorted(range(n), key=lambda i: rnd.random())
    for j, i in enumerate(order):
        y = 350 + (j % 3) * 30
        fowl(d, xs[i], y, 0.62 + 0.03 * (j % 3), sexes[i], pal_list[i], 1 if i % 2 == 0 else -1, young=(j % 4 == 3), seed=seed + i)
    return finish(im)

# ------------------------------------------------------------------ plants: a squash plant in the garden
FRUIT = {'butternut': 'butternut', 'cheese': 'cheese', 'tromboncino': 'tromboncino', 'buttercup': 'buttercup'}

def hybrid_fruit(d, cx, cy, k):
    c = (196, 190, 120)
    E(d, cx, cy + 24 * k, 118 * k, 70 * k, c)
    for i in range(-4, 5): L(d, [(cx + i * 24 * k * 0.9, cy - 36 * k), (cx + i * 26 * k, cy + 24 * k), (cx + i * 22 * k * 0.9, cy + 84 * k)], shade(c, 0.84), 3)
    E(d, cx - 36 * k, cy - 4 * k, 50 * k, 22 * k, shade(c, 1.12))
    R(d, cx - 10 * k, cy - 66 * k, cx + 10 * k, cy - 44 * k, (110, 90, 50), r=5 * k)

def fruit_at(d, x, y, kind, k):
    if kind == 'hybrid': hybrid_fruit(d, x, y, k)
    else: A.squash(d, x, y, kind, k)

TAGS = {'selected': (240, 196, 50), 'culled': (210, 60, 54), 'kept': (240, 196, 50), 'plain': (240, 238, 228)}

def img_plant(kind='cheese', stage='fruit', seed=1, code='', tag='plain', n_fruit=2):
    """stage: seedling, growing, flower, fruit, weak."""
    rnd = random.Random(seed)
    im, d = canvas((200, 226, 242), (150, 190, 120)); A.grass(im, d, 210)
    R(d, 30, 290, 770, 570, (88, 62, 42), r=8); R(d, 46, 306, 754, 556, (112, 80, 54), r=6)
    for _ in range(160):
        x, y = rnd.randint(60, 740), rnd.randint(314, 548); L(d, [(x, y), (x + rnd.randint(8, 26), y + rnd.randint(-4, 4))], (176, 148, 84), 3)
    weak = stage == 'weak'
    green = (60, 134, 62) if not weak else (150, 150, 70)
    green2 = (74, 150, 70) if not weak else (176, 166, 84)
    cx = 400 + rnd.randint(-40, 40); by = 405; sc = 0.8 if weak else 1.0
    if stage == 'seedling':
        for dx in (-210, -70, 70, 210):
            x = cx + dx; L(d, [(x, by + 40), (x, by - 20)], (110, 170, 80), 8)
            A.leaf(d, x, by - 20, math.radians(205), 80, (100, 176, 84)); A.leaf(d, x, by - 20, math.radians(-25), 80, (100, 176, 84))
    else:
        reach = {'growing': 0.75, 'flower': 0.9, 'fruit': 1.0, 'weak': 0.6}[stage]
        for side in (-1, 1):
            pts = [(cx + side * t * 340 * reach, by - 8 * math.sin(t * 5 + seed) - t * 10) for t in [i / 10 for i in range(11)]]
            L(d, pts, (84, 120, 56), 10)
            for i, (x, y) in enumerate(pts[1:], 1):
                A.leaf(d, x, y, math.radians(-95 + side * rnd.randint(10, 60)), rnd.randint(120, 175) * sc, green if i % 2 else green2)
        for a_ in (-150, -100, -60, -30, -170):
            A.leaf(d, cx, by, math.radians(a_), rnd.randint(170, 230) * sc, green2)
        L(d, [(cx, by + 20), (cx, by - 30)], (70, 120, 56), 14)
        if stage == 'flower':
            for dx in (-170, 40, 190, -30):
                x, y = cx + dx, by - 60 - rnd.randint(0, 60)
                for i in range(6):
                    a_ = i / 6 * 2 * math.pi
                    P(d, [(x, y), (x + math.cos(a_ - .35) * 40, y + math.sin(a_ - .35) * 36), (x + math.cos(a_) * 54, y + math.sin(a_) * 50), (x + math.cos(a_ + .35) * 40, y + math.sin(a_ + .35) * 36)], (250, 196, 50))
                E(d, x, y, 16, 16, (226, 150, 30))
        if stage in ('fruit', 'weak'):
            spots = [(cx - 230, by + 50), (cx + 210, by + 58), (cx + 10, by + 70)][:max(0, n_fruit)]
            for (x, y) in spots:
                kk = {'butternut': 0.5, 'cheese': 0.48, 'tromboncino': 0.48, 'buttercup': 0.5, 'hybrid': 0.48}[kind] * (0.7 if weak else 1.0)
                fruit_at(d, x, y - 24, kind, kk)
        if stage == 'growing':
            E(d, cx + 170, by + 60, 24, 18, (120, 180, 90))
    sx = 150 + rnd.randint(-8, 8)
    L(d, [(sx, 570), (sx, 360)], (176, 150, 100), 8)
    R(d, sx - 66, 322, sx + 66, 366, TAGS.get(tag, TAGS['plain']), r=6, outline=(90, 70, 50), w=2)
    if code: A.text(d, (sx, 332), code, A.font(A.FB, 20), (50, 40, 30), 'ma')
    return finish(im.crop((30 * S, 100 * S, 698 * S, 600 * S)))

def img_mix_border(seed=1):
    """A border planted with several squash kinds."""
    rnd = random.Random(seed)
    im, d = canvas((200, 226, 242), (150, 190, 120)); A.grass(im, d, 210)
    R(d, 30, 290, 770, 570, (92, 66, 44), r=8)
    for i in range(16): A.leaf(d, rnd.randint(70, 740), rnd.randint(350, 520), rnd.random() * 6.28, rnd.randint(130, 190), (60 + rnd.randint(0, 30), 130 + rnd.randint(0, 30), 60))
    for (x, y, kd) in [(160, 490, 'cheese'), (330, 510, 'butternut'), (500, 495, 'buttercup'), (660, 505, 'tromboncino')]: A.squash(d, x, y - 24, kd, 0.42)
    return finish(im.crop((30 * S, 100 * S, 698 * S, 600 * S)))

def small(im, size=(560, 420)): return im.resize(size, Image.LANCZOS)

def save_small(im, q=54):
    import io, base64
    im = small(im)
    def b64(i, qq):
        buf = io.BytesIO(); i.save(buf, 'JPEG', quality=qq, optimize=True); return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
    th = im.copy(); th.thumbnail((220, 220)); return b64(im, q), b64(th, 62)
