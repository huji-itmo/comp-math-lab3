from typing import Callable
import numpy as np


def right_rectangles_method(func: Callable, deltaX_i: np.ndarray):
    sm = 0
    values = func(deltaX_i)

    for i in range(0, deltaX_i.size - 1):
        delta_x = deltaX_i[i + 1] - deltaX_i[i]

        sm += values[i] * delta_x

    return sm
