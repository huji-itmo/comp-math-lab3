# function.py
import numpy as np

function_dict = {
    "sin": {
        "function": lambda x: np.sin(x),
        "antiderivative": lambda x: -np.cos(x),
        "description": "sin(x)",
    },
    "quadratic": {
        "function": lambda x: x**2,
        "antiderivative": lambda x: x**3 / 3,
        "description": "x²",
    },
    "exponential": {
        "function": lambda x: np.exp(x),
        "antiderivative": lambda x: np.exp(x),
        "description": "e^x",
    },
    "lab": {
        "function": lambda x: -np.pow(x, 3) - np.pow(x, 2) + x + 3,
        "antiderivative": lambda x: -(np.pow(x, 4) / 4)
        - (np.pow(x, 3) / 3)
        + (np.pow(x, 2) / 2)
        + 3 * x,
        "description": "-x³-x²+x+3",
    },
}
