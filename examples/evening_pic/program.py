from sonicstv import (
    bake, Sheet, SingleFreqNote,
    coverRandomly, stampWindowed, nudgeAll, nudgeAllAdaptively, biasAll,
)
from functools import partial


freq_list = [1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250]
note_count = 300
sheet = Sheet([
    SingleFreqNote(freq)
    for freq in [
        1800, 1900, 2000,
        1800, 1900, 2000,
        1800, 1900, 2000,
        1800, 1900, 2000,
        1800, 2000, 2000, 2000, 2000, 2000,
        2000, 1850, 1850, 1850, 1850, 1850
    ]
] * 70)

bake_result__coverRandomly = bake(
    "./examples/evening_pic/evening.png",
    sheet,
    line_process_algo=coverRandomly
)

if bake_result__coverRandomly is not None:
    bake_result__coverRandomly.save(
        "./examples/evening_pic/outputs/evening__result_coverRandomly.png",
        should_overwrite_if_existed=True
    )

bake_result__stampWindowed = bake(
    "./examples/evening_pic/evening.png",
    sheet,
    line_process_algo=stampWindowed
)

if bake_result__stampWindowed is not None:
    bake_result__stampWindowed.save(
        "./examples/evening_pic/outputs/evening__result_stampWindowed.png",
        should_overwrite_if_existed=True
    )

bake_result__nudgeAll = bake(
    "./examples/evening_pic/evening.png",
    sheet,
    line_process_algo=partial(nudgeAll, strength=0.25)
)

if bake_result__nudgeAll is not None:
    bake_result__nudgeAll.save(
        "./examples/evening_pic/outputs/evening__result_nudgeAll_25.png",
        should_overwrite_if_existed=True
    )

bake_result__nudgeAll = bake(
    "./examples/evening_pic/evening.png",
    sheet,
    line_process_algo=partial(nudgeAll, strength=0.50)
)

if bake_result__nudgeAll is not None:
    bake_result__nudgeAll.save(
        "./examples/evening_pic/outputs/evening__result_nudgeAll_50.png",
        should_overwrite_if_existed=True
    )

bake_result__nudgeAll = bake(
    "./examples/evening_pic/evening.png",
    sheet,
    line_process_algo=partial(nudgeAll, strength=0.75)
)

if bake_result__nudgeAll is not None:
    bake_result__nudgeAll.save(
        "./examples/evening_pic/outputs/evening__result_nudgeAll_75.png",
        should_overwrite_if_existed=True
    )

bake_result__nudgeAllAdaptively = bake(
    "./examples/evening_pic/evening.png",
    sheet,
    line_process_algo=partial(nudgeAllAdaptively)
)

if bake_result__nudgeAllAdaptively is not None:
    bake_result__nudgeAllAdaptively.save(
        "./examples/evening_pic/outputs/evening__result_nudgeAllAdaptively.png",
        should_overwrite_if_existed=True
    )

bake_result__biasAll = bake(
    "./examples/evening_pic/evening.png",
    sheet,
    line_process_algo=partial(biasAll, strength=0.25)
)

if bake_result__biasAll is not None:
    bake_result__biasAll.save(
        "./examples/evening_pic/outputs/evening__result_biasAll_25.png",
        should_overwrite_if_existed=True
    )

bake_result__biasAll = bake(
    "./examples/evening_pic/evening.png",
    sheet,
    line_process_algo=partial(biasAll, strength=0.50)
)

if bake_result__biasAll is not None:
    bake_result__biasAll.save(
        "./examples/evening_pic/outputs/evening__result_biasAll_50.png",
        should_overwrite_if_existed=True
    )

bake_result__biasAll = bake(
    "./examples/evening_pic/evening.png",
    sheet,
    line_process_algo=partial(biasAll, strength=0.75)
)

if bake_result__biasAll is not None:
    bake_result__biasAll.save(
        "./examples/evening_pic/outputs/evening__result_biasAll_75.png",
        should_overwrite_if_existed=True
    )
