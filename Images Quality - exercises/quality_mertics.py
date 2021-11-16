from typing import Dict, Union
import math
import numpy as np


def max_error(og_image: np.ndarray, mod_image: np.ndarray) -> int:
    res = 0
    for og_line, mod_line in zip(og_image, mod_image):
        for og_pixel, mod_pixel in zip(og_line, mod_line):
            error = abs(int(og_pixel) - int(mod_pixel))
            if error > res:
                res = error
    return res


def mean_absolute_error(og_image: np.ndarray, mod_image: np.ndarray) -> float:
    res = 0
    for og_line, mod_line in zip(og_image, mod_image):
        for og_pixel, mod_pixel in zip(og_line, mod_line):
            res += abs(int(og_pixel) - int(mod_pixel))
    return res / og_image.shape[0] * og_image.shape[1]


def squares_difference_acc(og_image: np.ndarray, mod_image: np.ndarray) -> int:
    res = 0
    for og_line, mod_line in zip(og_image, mod_image):
        for og_pixel, mod_pixel in zip(og_line, mod_line):
            res += (int(og_pixel) - int(mod_pixel)) ** 2
    return res


def mean_square_error(og_image: np.ndarray, mod_image: np.ndarray) -> float:
    return squares_difference_acc(og_image, mod_image) / og_image.shape[0] * og_image.shape[1]


def root_mean_square_error(og_image: np.ndarray, mod_image: np.ndarray) -> float:
    return math.sqrt(mean_square_error(og_image, mod_image))


def square_acc(og_image: np.ndarray) -> int:
    res = 0
    for og_line in og_image:
        for og_pixel in og_line:
            res += og_pixel ** 2
    return res


def normalized_mean_square_error(og_image: np.ndarray, mod_image: np.ndarray) -> float:
    return mean_square_error(og_image, mod_image) / square_acc(og_image)


def peak_signal_to_noise_ratio(og_image: np.ndarray, mod_image: np.ndarray, max_L: int) -> float:
    return 10 * math.log10((og_image.shape[0] * og_image.shape[1] * max_L * max_L) / squares_difference_acc(og_image, mod_image))


def signal_to_noise_ratio(og_image: np.ndarray, mod_image: np.ndarray) -> float:
    return 10 * math.log10(square_acc(og_image) / squares_difference_acc(og_image, mod_image))


def covariance_aux(og_image: np.ndarray, mod_image: np.ndarray) -> float:
    mi_og = og_image.mean()
    mi_mod = mod_image.mean()
    res = 0
    for og_line, mod_line in zip(og_image, mod_image):
        for og_pixel, mod_pixel in zip(og_line, mod_line):
            res += (int(og_pixel) - mi_og) * (int(mod_pixel) - mi_mod)
    return res


def covariance(og_image: np.ndarray, mod_image: np.ndarray) -> float:
    return covariance_aux(og_image, mod_image) / og_image.shape[0] * og_image.shape[1]


def correlation_coeficient(og_image: np.ndarray, mod_image: np.ndarray) -> float:
    mi_og = og_image.mean()
    mi_mod = mod_image.mean()
    res_og = 0
    res_mod = 0
    for og_line, mod_line in zip(og_image, mod_image):
        for og_pixel, mod_pixel in zip(og_line, mod_line):
            res_og += (int(og_pixel) - mi_og) ** 2
            res_mod += (int(mod_pixel) - mi_mod) ** 2
    return covariance_aux(og_image, mod_image) / math.sqrt(res_og * res_mod)


def similar(a: int, b: int, tolerance: float = 0) -> bool:
    return (abs(a) >= abs(b) - tolerance) and (abs(a) <= abs(b) + tolerance)


def jaccard_coeficient(og_image: np.ndarray, mod_image: np.ndarray, tolerance: float = 0) -> float:
    res = 0
    for og_line, mod_line in zip(og_image, mod_image):
        for og_pixel, mod_pixel in zip(og_line, mod_line):
            res += int(similar(og_pixel, mod_pixel, tolerance))
    return res / og_image.shape[0] * og_image.shape[1]


def quality_metrics(og_image: np.ndarray, mod_image: np.ndarray) -> Dict[str, Union[int, float]]:
    return dict({
        "max_error": max_error(og_image, mod_image),
        "mean_absolute_error": mean_absolute_error(og_image, mod_image),
        "mean_square_error": mean_square_error(og_image, mod_image),
        "root_mean_square_error": root_mean_square_error(og_image, mod_image),
        "normalized_mean_square_error": normalized_mean_square_error(og_image, mod_image),
        "peak_signal_to_noise_ratio": peak_signal_to_noise_ratio(og_image, mod_image, 255),
        "signal_to_noise_ratio": signal_to_noise_ratio(og_image, mod_image),
        "covariance": covariance(og_image, mod_image),
        "correlation_coeficient": correlation_coeficient(og_image, mod_image),
        "jaccard_coeficient": jaccard_coeficient(og_image, mod_image, 0)
    })
