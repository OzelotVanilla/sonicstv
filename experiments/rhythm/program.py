from experiments.utils import convertImageToMartinM1Audio
from concurrent.futures import ProcessPoolExecutor
from functools import partial


if __name__ == "__main__":
    image_names = [
        "rect_10px_gap_10px", "rect_30px_gap_10px", "rect_60px_gap_10px",
        "rect_10px_gap_20px"
    ]

    with ProcessPoolExecutor() as executor:
        executor.map(
            partial(convertImageToMartinM1Audio, should_overwrite_if_existed=True),
            map(lambda image_name: f"experiments/rhythm/{image_name}.png", image_names),
            map(lambda image_name: f"experiments/rhythm/output/{image_name}.wav", image_names),
        )