# Ροδοδάφνης 13: renovation notes

Everything collected for the renovation and what was read out of it while building the 3D model (`model/rododafnis-13-3d.html`).

Confidence tags: **[Certain]** read directly from a drawing, **[Likely]** measured or inferred with a cross-check, **[Guessing]** an assumption made to fill a gap.

## Sources

| File | What it is |
|---|---|
| `source/drawings/plumbing-plan-ydravliki.pdf` | New layout, plumbing (Εγκατάσταση: Υδραυλική). Room names, areas, furniture layout, water and drain points. Main source for the walls. |
| `source/drawings/electrical-plan-ilektrologiki.pdf` | Same layout, electrical (Εγκατάσταση: Ηλεκτρολογική). Sockets, switches, lights, A/C, data and TV points, mounting heights. |
| `source/drawings/old-floor-plan-photo.jpg` | Photo of the original permit drawing, before the renovation (photographed rotated). Includes the Ν.4178/13 legalisation notes. |
| `source/kitchen/kitchen-cabinet-plan-xhtas2.png` | Cabinet maker's plan view of the kitchen (ΧΗΤΑΣ2), dimensions in mm. |
| `source/kitchen/kitchen-cabinet-render-xhtas1.png` | Cabinet maker's 3D render (ΧΗΤΑΣ1). |
| `source/kitchen/kitchen-moodboard.png` | Kitchen moodboard with the four chosen finishes. |
| `source/renders/living-room-target-render.png` | Target look for the living room. |
| `source/photos-before/` | Rooms before work started: kitchen (3), bathroom, bedroom, living room, the two rooms before the wall came out. |
| `source/photos-demolition/` | Living room during demolition: wall removed (beam left), window openings widened into doors. |
| `docs/derived/` | Previews of both PDFs and the wall mask used for measuring. |
| `tools/extract_walls.py` | Script that measures the walls from the plumbing PDF. |

## Rooms (new layout) [Certain]

| Room | Greek | Area | Perimeter |
|---|---|---|---|
| Living / dining | Σαλοτραπεζαρία | 21.19 m² | 19.65 m |
| Office | Γραφείο | 12.33 m² | 14.16 m |
| Kitchen | Κουζίνα | 11.38 m² | 13.50 m |
| Bedroom | Δωμάτιο 1 | 10.50 m² | 13.49 m |
| Bathroom | Μπάνιο | 4.23 m² | 8.61 m |
| Hall | Διάδρομος–Χωλ | 4.13 m² | 9.28 m |
| **Interior total** | | **63.76 m²** | |
| Balcony | Μπαλκόνι 1 | 24.50 m² | 40.97 m |

- Ceiling height 2.95 m (old permit drawing, `h=2.95m`) [Certain].
- The office and living/dining are one open space; the old partition was removed and its beam stays [Certain, photos + plan].
- The balcony wraps two sides: 1.25 m deep along the front, 1.32 m along the left side, 12.72 m long overall [Certain].

## Measured geometry [Likely, ±3–5 cm]

Origin: outer corner of the two balcony-facing walls. x runs along the front (balcony) wall, z runs toward the back. Scale 135.5 px/m at 200 dpi, cross-checked against the labelled kitchen area.

- Outer footprint: 11.37 m × 6.56 m (living side); the hall/bath side ends at 5.70 m, where the stairwell is.
- Exterior walls 18 cm, partitions 9–12 cm.

Openings onto the balcony (width × height):

| Room | Opening | Position |
|---|---|---|
| Office | 1.27 × 2.10 balcony door | front wall, x 1.48–2.75 |
| Bedroom | 1.24 × 2.12 balcony door | front wall, x 5.29–6.52 |
| Kitchen | 1.27 × 2.12 balcony door | front wall, x 8.74–10.01 |
| Office | 2.00 × 2.10 opening | left wall, z 0.56–2.57 |
| Living | 2.00 × 2.10 opening | left wall, z 3.75–5.73 |

Interior doors: entrance 1.01 × 2.18; living→hall 0.97 × 2.17; bedroom 0.82 × 2.19; kitchen 0.83 × 2.18; bathroom 0.68 × 1.91. Concrete columns sit at the front-left corner, mid-front wall (x ≈ 4.1–4.5), front-right corner, the left wall between the two big openings (z ≈ 2.9–3.25) and the back-left corner.

Approximate room rectangles (x, z, width, depth in m):

- Office + living: 0.18, 0.18, 3.95, 6.23, plus 4.13, 3.22, 2.60, 3.19
- Bedroom: 4.22, 0.18, 3.46, 2.95
- Kitchen: 7.77, 0.18, 3.42, 3.27
- Hall: 6.73, 3.22, 2.36, 2.30
- Bathroom: 9.18, 3.54, 2.01, 1.98

## Kitchen

### Cabinet plan (ΧΗΤΑΣ2), mm [Certain for the numbers, Likely for the wall assignment]

- **Run (2), 3290, right wall, from the balcony end:** filler 40 · pull-out 150 · hob unit 600 (drawers) · base 600 · sink unit 800 · base 450 · corner 630/650 + 20.
- **Wall units on run (2):** 15 · 60 · 60 · 80 · 45 · corner 63/27.
- **Run (3), 2530, back wall (kitchen/bath wall), from the corner:** corner base 1050 · washing machine 600 · fridge column 856 (fridge 700), ending 130 short. This brings it to the kitchen door, so it fits the room.
- **Return (1), 1065:** end panel at the balcony wall.
- The hood sits on the right wall near the balcony end (plumbing plan), so the hob is at that end and the sink in the middle.

### Finishes (moodboard) [Certain]

| Item | Finish |
|---|---|
| Floor | 60×60 cream onyx-look tile, gloss (Πλακάκι δαπέδου 60×60) |
| Worktop and splashback | Beech brown (Πάγκος & πλάτη) |
| Cabinets | Cream matt (Χρώμα ντουλαπιών) |
| Kitchen walls | Olive green matt (Χρώμα τοίχου) |
| Extras in the render | LED strip under the wall units, stainless fridge in a cream tall housing |

## Living room (target render) [Certain]

Sage green walls, white crown moulding, glossy cream marble-look floor tiles, white PVC sliding doors with roller-shutter boxes, the beam painted the wall colour.

## Bathroom (plumbing plan) [Certain for fixtures]

Walk-in shower in the back-right corner, wall-hung WC with concealed cistern (κaζανάκι εντοιχισμού) on the right wall, basin on the back wall, extractor fan, hot and cold supplies, floor drain. No tile or finish selection in the files.

## Plumbing and gas (plumbing plan) [Certain]

- **New water line from the meter to the flat**, "as shown to us" (Θα γίνει νέα γραμμή από το υδρόμετρο μέχρι το διαμέρισμα).
- Manifold (συλλέκτης 6) in the kitchen.
- Wall-hung gas boiler (λέβητας αερίου επιτοίχιος) on the balcony, front wall, by the kitchen.
- Kitchen: hot and cold supply plus drain on the right wall for the sink; washing machine and dishwasher points (Πλ. ρούχων, Πλ. πιάτων) next to them.
- Balcony tap near the downpipe (βρύση κοντά σε λούκι), front-left.
- Radiators: T22-900-500, T22-900-600 (several), T22-900-700, T22-900-800.

## Electrical (electrical plan) [Certain]

Mounting heights, measured to the centre from the finished floor:

1. Sockets 0.55 m.
2. Kitchen worktop sockets 1.20 m.
3. Bathroom socket 1.20 m.
4. Switches 1.25 m.
5. Bathroom light 1.85 m.
6. Bedroom socket and TV 1.60 m.
7. Where there is a washing machine and dishwasher in the kitchen, leave a 3×2.5 cable (NYM) 1 m long with a plug at the end.
8. Check for a central TV aerial.

Other points:

- Kitchen supply with an oven point at 1.00 m and a microwave point at 1.60 m.
- Reinforced 3×2.5 sockets for the hob and the hood.
- A/C supplies, one on a 3×1.5 line with its own breaker.
- Fibre: the line enters at the hall ("Αρχή οπτικής ίνας"), with an empty conduit for fibre and the router position in the living room. TEL/DATA/TV points in the living room and office.
- Room thermostat, door entry phone (Θ/Τ), doorbell, two-row distribution board.
- Spots and LED lights.

## Conflicts between the drawings: resolve before the trades start

1. **Oven and microwave [Certain].** The electrical plan has oven (1.00 m) and microwave (1.60 m) supplies on the kitchen's left wall by the balcony door. The cabinet plan has no tall oven unit, and the plumbing plan puts the kitchen table there.
2. **Dishwasher [Certain].** The plumbing plan has a dishwasher point; the cabinet plan has no dishwasher.
3. **Washing machine position [Likely].** Plumbing puts its supply and drain on the right wall near the sink. The cabinet plan puts the machine on the back wall next to the fridge, about 1–1.5 m away.
4. **Bathroom finishes [Certain].** Not specified anywhere.

## Assumptions in the 3D model [Guessing]

- Bathroom tiles: neutral light 30×60 walls and grey floor as placeholders.
- Bedroom and hall walls: warm white.
- Furniture follows the layout drawn on the plumbing plan; sizes are generic.
- A/C indoor units placed approximately (left-wall pier in the living area, bedroom front wall).
- The 0.45 m gap in the front wall between bedroom and kitchen is modelled as solid wall.
- Interior doors are shown open; their swing directions are not taken from the drawings.

## Old layout (permit drawing photo) [Certain]

Before the renovation: living room (Καθιστικό) 6.56 × 3.13, two rooms (Δωμάτιο) 2.99 wide (3.94 and 3.43 long), kitchen (Κουζίνα) 3.40 × 3.31, bathroom (Λουτρό) 2.02 × 1.95, ceiling 2.95. Three Ν.4178/13 legalisations are noted: 2.10 m², 2.17 m² and 2.65 m² of unauthorised extension.
