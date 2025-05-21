from typing import Callable
import numpy as np


def middle_rectangles_method(func: Callable, deltaX_i: np.ndarray):
    function_range = [0, 0]

    function_range[0] = deltaX_i[0]
    function_range[1] = deltaX_i[deltaX_i.size - 1]

    # only fixed delta_x works here
    delta_x = deltaX_i[1] - deltaX_i[0]

    delta_x_i_in_between = np.linspace(
        function_range[0] + delta_x / 2,
        function_range[1] - delta_x / 2,
        deltaX_i.size - 1,
    )

    values_in_between = func(delta_x_i_in_between)

    sm = 0

    for i in range(0, deltaX_i.size - 1):
        sm += values_in_between[i] * delta_x

    return sm
