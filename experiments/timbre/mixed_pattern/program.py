from experiments.utils import convertImageToMartinM1Audio


# Verticle Stripes

convertImageToMartinM1Audio(
    "experiments/timbre/mixed_pattern/vertical_stripes_16px_multicolour.png",
    "experiments/timbre/mixed_pattern/output/vertical_stripes_16px_multicolour.wav",
    should_overwrite_if_existed=True
)

# Generated Image

image_names = [
    "square_wave", "sine_wave", "triangle_wave", "sawtooth_wave",
    "dual_sine", "y_sweep", "smooth_noise", "rgb_combo"
]
for image_name in image_names:
    convertImageToMartinM1Audio(
        f"experiments/timbre/mixed_pattern/{image_name}.png",
        f"experiments/timbre/mixed_pattern/output/{image_name}.wav",
        should_overwrite_if_existed=True
    )
