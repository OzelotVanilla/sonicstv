from sonicstv import (
    bake, Sheet, SingleFreqNote as s,
    nudgeAll, biasAll, coverRandomly
)
from functools import partial

"""
Description for the picture:

* around upper 1/3 of the picture: sound is dark and unclear
* around middle 1/3: sound starts trembling, offset is negative, and melogy shape become hard to be controlled.
* around lower 1/3: sound becomes clearer and clearer, offset is positive.

Theme possible for the changing of the picture:
* upper 1/3: Introduce the motif A. A -> A' (variation) -> A.
* middle 1/3: Use extreme high/low sound to show a conflicting feeling.
* lower 1/3: Use the A' first, then a new A'', then come back to A.
"""

f0 = 1500
f1 = 1554.3935082111
f2 = 1610.759452245874
f3 = 1669.1693572404358
f4 = 1729.6973419996184
f5 = 1792.4202130494677
f6 = 1857.4175621002996
f7 = 1924.7718670439954
f8 = 1994.5685966136964
f9 = 2066.8963188387024
f10 = 2141.8468134321993
f11 = 2219.515188254428
f12 = 2300

sheet = Sheet([
    # line 1
    s(f, duration_frame=3)
    for f in [
        f0, f4, f4, f3, f4, f0,
        f3, f7, f4, f3, f4, f0,
        f4, f7, f10, f8, f10, f4,
        f2, f1, f2, f4, f7, f10
    ]
])

bake_result__nudgeAll = bake(
    "./examples/game_pic/tunnel.png",
    sheet,
    line_process_algo=partial(nudgeAll, strength=0.75)
)

if bake_result__nudgeAll is not None:
    bake_result__nudgeAll.save(
        "./examples/game_pic/outputs/tunnel__designated_nudgeAll.png",
        should_overwrite_if_existed=True
    )

bake_result__biasAll = bake(
    "./examples/game_pic/tunnel.png",
    sheet,
    line_process_algo=partial(biasAll, strength=0.75)
)

if bake_result__biasAll is not None:
    bake_result__biasAll.save(
        "./examples/game_pic/outputs/tunnel__designated_biasAll.png",
        should_overwrite_if_existed=True
    )

bake_result__coverRandomly = bake(
    "./examples/game_pic/tunnel.png",
    sheet,
    line_process_algo=partial(coverRandomly, strength=0.75)
)

if bake_result__coverRandomly is not None:
    bake_result__coverRandomly.save(
        "./examples/game_pic/outputs/tunnel__designated_coverRandomly.png",
        should_overwrite_if_existed=True
    )
