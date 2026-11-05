"""Build Infina Sans 1.006 from Infina Sans 1.004 and Lexend.

Usage: python build_1006.py <InfinaSans-1.004.ttf> <Lexend[wght].ttf> <out.ttf>

Changes from 1.004:
1. Letter spacing back to Lexend's original. 1.004 took 20 units off each
   letter's advance and moved its outline 10 units left. This script copies
   Lexend's metrics, outline offsets, and component offsets back.
2. The word space (space, U+00A0) keeps the 1.004 width: Lexend minus 20
   units, so word spacing stays at -0.02 em.
3. The logo glyph f_i.infina gets the same restore: the f part moves 10 units,
   the i part moves 30 units, and the crossbar stretches to join them.
4. The comma is 30% smaller (scale 0.7) around its baseline center, at every
   weight. Its advance width stays the same, so number rhythm does not change.
   semicolon and quotesinglbase use comma as a component, so they follow.
5. Regular (wght 400) renders the old wght 320 design. Thin (100) and
   Black (900) do not change; the weights between them move linearly.
"""
import sys

from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.varLib.instancer import AxisTriple

REGULAR_DESIGN = 320
COMMA_SCALE = 0.7
WORD_SPACES = ("space", "uni00A0")
VERSION = 1.006

src, lexend_path, dst = sys.argv[1], sys.argv[2], sys.argv[3]
font = TTFont(src)
lex = TTFont(lexend_path)
glyf, gvar, hmtx = font["glyf"], font["gvar"], font["hmtx"]
lglyf, lhmtx = lex["glyf"], lex["hmtx"]


def full_deltas(name):
    """Return default coords (with phantoms), end points, and gvar variations
    with every inferred (None) delta filled in."""
    coords, ctrl = glyf._getCoordinatesAndControls(name, hmtx.metrics)
    variations = gvar.variations.get(name, [])
    for var in variations:
        var.calcInferredDeltas(coords, ctrl.endPts)
    return coords, ctrl, variations


# 1 + 2. Restore Lexend metrics and offsets for every shared glyph.
restored = 0
for name in lex.getGlyphOrder():
    if name not in hmtx.metrics or name in WORD_SPACES:
        continue
    adv, lsb = hmtx[name]
    ladv, llsb = lhmtx[name]
    g, lg = glyf[name], lglyf[name]
    if g.isComposite():
        for c, lc in zip(g.components, lg.components):
            c.x, c.y = lc.x, lc.y
    elif g.numberOfContours > 0:
        g.expand(glyf)
        shift = llsb - lsb
        if shift:
            g.coordinates.translate((shift, 0))
            g.recalcBounds(glyf)  # keep xMin in sync for phantom points
    if (adv, lsb) != (ladv, llsb):
        restored += 1
    hmtx[name] = (ladv, llsb)
print(f"restored metrics on {restored} glyphs")

# 3. Logo glyph f_i.infina: contour 0 = f body, 1 = crossbar, 2 = i stem.
name = "f_i.infina"
coords, ctrl, variations = full_deltas(name)
g = glyf[name]
g.expand(glyf)
f_adv_1004 = 373  # width of f in 1.004; points right of it belong to the i
start = 0
for ci, end in enumerate(g.endPtsOfContours):
    for i in range(start, end + 1):
        x, y = g.coordinates[i]
        if ci == 0:
            dx = 10
        elif ci == 2:
            dx = 30
        else:
            dx = 30 if x > f_adv_1004 else 10
        g.coordinates[i] = (x + dx, y)
    start = end + 1
g.recalcBounds(glyf)
adv, lsb = hmtx[name]
hmtx[name] = (adv + 40, lsb + 10)

# 4. Comma: scale 0.7 around (advance center, baseline) at every master.
name = "comma"
coords, ctrl, variations = full_deltas(name)
g = glyf[name]
g.expand(glyf)
n = len(g.coordinates)
adv, _ = hmtx[name]
cx0 = adv / 2
k = COMMA_SCALE
for i in range(n):
    x, y = g.coordinates[i]
    g.coordinates[i] = (round(cx0 + k * (x - cx0)), round(k * y))
for var in variations:
    d = var.coordinates
    # phantom points: n = origin, n+1 = advance; center moves by their mean
    dcx = (d[n][0] + d[n + 1][0]) / 2
    for i in range(n):
        dx, dy = d[i]
        d[i] = (k * dx + (1 - k) * dcx, k * dy)
g.recalcBounds(glyf)
hmtx[name] = (adv, g.xMin)

# 5. Regular = old REGULAR_DESIGN: move the default, then relabel it 400.
font = instancer.instantiateVariableFont(
    font, {"wght": AxisTriple(100, REGULAR_DESIGN, 900)})
for a in font["fvar"].axes:
    if a.axisTag == "wght":
        a.defaultValue = 400.0
font["OS/2"].usWeightClass = 400

# Version and description.
font["head"].fontRevision = VERSION
for rec in font["name"].names:
    s = rec.toUnicode()
    if "1.004" in s:
        s = s.replace("1.004", f"{VERSION:.3f}")
        s = s.replace(
            "letter spacing -0.02 em on letters, numbers unchanged, logo fi in infina",
            f"Lexend letter spacing, word space -0.02 em, comma 70%, "
            f"Regular = {REGULAR_DESIGN} design, logo fi in infina")
        rec.string = s
font.save(dst)
print("saved", dst)
