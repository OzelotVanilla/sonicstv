from sonicstv import (
    bake, Sheet, SingleFreqNote,
    coverRandomly, stampWindowed, nudgeAll, nudgeAllAdaptively, biasAll,
)


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
    "./examples/game_pic/tunnel.png",
    sheet,
    line_process_algo=coverRandomly
)

if bake_result__coverRandomly is not None:
    bake_result__coverRandomly.save(
        "./examples/game_pic/outputs/tunnel__result_coverRandomly.png",
        should_overwrite_if_existed=True
    )

bake_result__stampWindowed = bake(
    "./examples/game_pic/tunnel.png",
    sheet,
    line_process_algo=stampWindowed
)

if bake_result__stampWindowed is not None:
    bake_result__stampWindowed.save(
        "./examples/game_pic/outputs/tunnel__result_stampWindowed.png",
        should_overwrite_if_existed=True
    )

bake_result__nudgeAll = bake(
    "./examples/game_pic/tunnel.png",
    sheet,
    line_process_algo=nudgeAll
)

if bake_result__nudgeAll is not None:
    bake_result__nudgeAll.save(
        "./examples/game_pic/outputs/tunnel__result_nudgeAll.png",
        should_overwrite_if_existed=True
    )

bake_result__nudgeAllAdaptively = bake(
    "./examples/game_pic/tunnel.png",
    sheet,
    line_process_algo=nudgeAllAdaptively
)

if bake_result__nudgeAllAdaptively is not None:
    bake_result__nudgeAllAdaptively.save(
        "./examples/game_pic/outputs/tunnel__result_nudgeAllAdaptively.png",
        should_overwrite_if_existed=True
    )

bake_result__biasAll = bake(
    "./examples/game_pic/tunnel.png",
    sheet,
    line_process_algo=biasAll
)

if bake_result__biasAll is not None:
    bake_result__biasAll.save(
        "./examples/game_pic/outputs/tunnel__result_biasAll.png",
        should_overwrite_if_existed=True
    )
