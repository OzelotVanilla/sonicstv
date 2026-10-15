from experiments.utils import convertImageToMartinM1Audio


# Verticle Stripes

convertImageToMartinM1Audio(
    "experiments/timbre/simple_pattern/vertical_stripes_16px.png",
    "experiments/timbre/simple_pattern/output/vertical_stripes_16px.wav",
    should_overwrite_if_existed=True
)

convertImageToMartinM1Audio(
    "experiments/timbre/simple_pattern/vertical_stripes_32px.png",
    "experiments/timbre/simple_pattern/output/vertical_stripes_32px.wav",
    should_overwrite_if_existed=True
)

convertImageToMartinM1Audio(
    "experiments/timbre/simple_pattern/vertical_stripes_64px.png",
    "experiments/timbre/simple_pattern/output/vertical_stripes_64px.wav",
    should_overwrite_if_existed=True
)

convertImageToMartinM1Audio(
    "experiments/timbre/simple_pattern/vertical_stripes_160px.png",
    "experiments/timbre/simple_pattern/output/vertical_stripes_160px.wav",
    should_overwrite_if_existed=True
)

# Gradient

convertImageToMartinM1Audio(
    "experiments/timbre/simple_pattern/gradient_black_to_white.png",
    "experiments/timbre/simple_pattern/output/gradient_black_to_white.wav",
    should_overwrite_if_existed=True
)

convertImageToMartinM1Audio(
    "experiments/timbre/simple_pattern/gradient_green_to_purple.png",
    "experiments/timbre/simple_pattern/output/gradient_green_to_purple.wav",
    should_overwrite_if_existed=True
)
