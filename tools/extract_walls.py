"""Measure wall positions from the plumbing-plan PDF.

Renders the PDF at 200 dpi, keeps the wall fill colour (RGB 185,185,185),
and prints wall rectangles in metres. Origin is the outer corner of the two
balcony-facing walls (top-left on the drawing); x runs right, z runs toward
the back of the flat.

Scale: 135.5 px per metre at 200 dpi, checked against the drawing's own room
areas (the kitchen comes out at 11.38 m², as labelled).

Usage:
    pdftoppm -r 200 -png source/drawings/plumbing-plan-ydravliki.pdf /tmp/p200
    python3 tools/extract_walls.py /tmp/p200-1.png
"""
import sys

import numpy as np
from PIL import Image

PX_PER_M = 135.5
ORIGIN_PX = (276, 552)  # outer wall corner on the 200 dpi render
CELL = 4                # px per grid cell (~3 cm)


def wall_mask(path):
    a = np.array(Image.open(path).convert("RGB")).astype(int)
    m = (abs(a[..., 0] - 185) < 4) & (abs(a[..., 1] - 185) < 4) & (abs(a[..., 2] - 185) < 4)
    m[:500, :] = False   # title block
    m[:, 1830:] = False  # legend
    return m


def rectangles(mask):
    h, w = mask.shape[0] // CELL, mask.shape[1] // CELL
    g = mask[: h * CELL, : w * CELL].reshape(h, CELL, w, CELL).mean(axis=(1, 3)) > 0.5
    used = np.zeros_like(g)
    out = []
    for i in range(h):
        for j in range(w):
            if not g[i, j] or used[i, j]:
                continue
            rw = 0
            while j + rw < w and g[i, j + rw] and not used[i, j + rw]:
                rw += 1
            rh = 1
            while i + rh < h and g[i + rh, j:j + rw].all() and not used[i + rh, j:j + rw].any():
                rh += 1
            used[i:i + rh, j:j + rw] = True
            if rw * rh >= 6:
                out.append(((j * CELL - ORIGIN_PX[0]) / PX_PER_M, (i * CELL - ORIGIN_PX[1]) / PX_PER_M,
                            rw * CELL / PX_PER_M, rh * CELL / PX_PER_M))
    return out


if __name__ == "__main__":
    for x, z, w, d in rectangles(wall_mask(sys.argv[1])):
        print(f"x={x:5.2f} z={z:5.2f} w={w:4.2f} d={d:4.2f}")
