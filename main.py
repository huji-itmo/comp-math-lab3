import numpy as np

import matplotlib.pyplot as plt

from errors import mse, mae


import numpy as np
import matplotlib.pyplot as plt
from errors import mse, mae

MAX_ITERATIONS = 100


def runge_rule(prev_integral, approx, k):
    return abs((prev_integral - approx) / (2**k - 1))


def compare_integration_methods(func, interval, exact_integral, methods, epsilon):

    for method in methods:
        print("----", method["name"], "-----")
        prev_integral = None

        number_of_divisions = 4

        iteration = 0

        while iteration < MAX_ITERATIONS:
            iteration += 1
            x = np.linspace(interval[0], interval[1], number_of_divisions + 1)
            approx = method["method"](func, x)
            k = method["degree"]
            print("-- Iteration", iteration)
            print("number of intervals:", number_of_divisions)
            print("value:", approx)
            print("diff between analitical:", approx - exact_integral)
            if exact_integral != 0:
                print(
                    "percent:",
                    abs(((approx - exact_integral) / exact_integral) * 100),
                    "%",
                )
            else:
                print("percent:", 0, "%")
            if prev_integral is not None:
                k = method["degree"]
                runge = runge_rule(prev_integral, approx, k)
                print("runge", runge)

                if runge < epsilon:
                    print("-- Условие Рунге выполнено")
                    print("found value after", iteration, "iterations")
                    print("final value:", approx)

                    print()
                    break
            prev_integral = approx
            number_of_divisions *= 2

        if iteration == MAX_ITERATIONS:
            print("!!! MAX ITERATIONS !!!")


# Example usage
if __name__ == "__main__":
    # Import necessary components
    from function import function_dict
    from simpsons_method import simpsons_method
    from trapezoid_method import trapezoid_method
    from right_rectangles_method import right_rectangles_method
    from left_rectangles_method import left_rectangles_method
    from middle_rectangles_method import middle_rectangles_method

    # Let user select a function
    print("Available functions:")
    for key in function_dict:
        print(f"- {key}: {function_dict[key]['description']}")

    while True:
        selected_key = input("Enter function name to integrate: ").strip()
        if selected_key in function_dict:
            break
        print("Invalid function name. Try again.")

    selected_function = function_dict[selected_key]

    # Get interval from user
    while True:
        try:
            a = float(input("Enter lower bound a: "))
            b = float(input("Enter upper bound b: "))
            if a == b:
                print("Bounds cannot be equal. Try again.")
                continue
            if a > b:
                print("Upper bound must be greater than lower bound. Swapping them.")
                a, b = b, a
            break
        except ValueError:
            print("Please enter valid numbers.")

    while True:
        try:
            epsilon = float(input("Enter epsilon: "))
            if epsilon <= 0:
                print("Should be positive")
                continue
            break
        except ValueError:
            print("Please enter valid numbers.")

    # Calculate exact integral using antiderivative
    F = selected_function["antiderivative"]
    exact_integral = F(b) - F(a)
    print(f"\nExact integral value: {exact_integral:.6f}")

    methods = [
        {"name": "Trapezoid", "method": trapezoid_method, "color": "red", "degree": 2},
        {"name": "Simpsons", "method": simpsons_method, "color": "green", "degree": 4},
        {
            "name": "Right rectangles",
            "method": right_rectangles_method,
            "color": "blue",
            "degree": 2,
        },
        {
            "name": "Left rectangles",
            "method": left_rectangles_method,
            "color": "yellow",
            "degree": 2,
        },
        {
            "name": "Middle rectangles",
            "method": middle_rectangles_method,
            "color": "purple",
            "degree": 2,
        },
    ]

    title_suffix = f"{selected_function['description']} on [{a:.2f}, {b:.2f}]"

    compare_integration_methods(
        func=selected_function["function"],
        interval=[a, b],
        exact_integral=exact_integral,
        methods=methods,
        epsilon=epsilon,
    )
