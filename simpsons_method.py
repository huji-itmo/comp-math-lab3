from typing import Callable
import numpy as np


def simpsons_method(func: Callable, deltaX_i: np.ndarray):
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
    values = func(deltaX_i)

    sm = 0

    for i in range(0, deltaX_i.size - 1):
        sm += (values[i] + 4 * values_in_between[i] + values[i + 1]) / 6 * delta_x

    return sm
