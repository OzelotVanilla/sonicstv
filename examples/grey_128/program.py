from sonicstv import bake, Sheet, SingleFreqNote, coverRandomly
from functools import partial


# Assuming cwd is project root.

bake_result = bake(
    "./examples/grey_128/grey_128.png",
    Sheet([
        SingleFreqNote(1800), SingleFreqNote(1900), SingleFreqNote(2000)
    ] * 100),
    line_process_algo=partial(coverRandomly, strength=0.25)
)
if bake_result is not None:
    bake_result.save("./examples/grey_128/outputs/grey_128__result.png")
