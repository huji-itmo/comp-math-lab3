from typing import Callable
import numpy as np


def trapezoid_method(func: Callable, deltaX_i: np.ndarray) -> float:
    sm = 0
    values = func(deltaX_i)

    for i in range(0, deltaX_i.size - 1):
        delta_x = deltaX_i[i + 1] - deltaX_i[i]

        sm += ((values[i] + values[i + 1]) / 2) * delta_x

    return sm
