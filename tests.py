import numpy as np

import matplotlib.pyplot as plt

from errors import mse, mae


import numpy as np
import matplotlib.pyplot as plt
from errors import mse, mae


def compare_integration_methods(
    func, interval, exact_integral, methods, test_partitions, title_suffix=""
):

    # Initialize error storage
    errors = {
        "MSE": {method["name"]: [] for method in methods},
        "MAE": {method["name"]: [] for method in methods},
    }

    for n in test_partitions:
        # Generate partition points
        x = np.linspace(interval[0], interval[1], n + 1)
        for method in methods:
            # Compute approximate integral
            approx = method["method"](func, x)
            # Compute errors
            errors["MSE"][method["name"]].append(mse(exact_integral, approx))
            errors["MAE"][method["name"]].append(mae(exact_integral, approx))

    # Plotting
    for metric in ["MSE", "MAE"]:
        plt.figure()
        for method in methods:
            name = method["name"]
            color = method.get("color", None)  # Default color if not specified
            plt.plot(
                test_partitions,
                errors[metric][name],
                label=name,
                color=color,
                marker="o",
            )
        plt.legend()
        plt.xlabel("Number of partitions")
        plt.ylabel(metric)
        title = f"{metric} Errors"
        if title_suffix:
            title += f", {title_suffix}"
        plt.title(title)
        plt.grid(True)
        plt.savefig(f"output_{metric}.pdf")


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

    # Calculate exact integral using antiderivative
    F = selected_function["antiderivative"]
    exact_integral = F(b) - F(a)
    print(f"\nExact integral value: {exact_integral:.6f}")

    # Define the integration methods to compare
    methods = [
        {"name": "Trapezoid", "method": trapezoid_method, "color": "red"},
        {"name": "Simpsons", "method": simpsons_method, "color": "green"},
        {
            "name": "Right rectangles",
            "method": right_rectangles_method,
            "color": "blue",
        },
        {
            "name": "Left rectangles",
            "method": left_rectangles_method,
            "color": "yellow",
        },
        {
            "name": "Middle rectangles",
            "method": middle_rectangles_method,
            "color": "purple",
        },
    ]

    # Define test parameters
    test_partitions = [16, 32, 64, 128]
    title_suffix = f"{selected_function['description']} on [{a:.2f}, {b:.2f}]"

    # Run comparison
    compare_integration_methods(
        func=selected_function["function"],
        interval=[a, b],
        exact_integral=exact_integral,
        methods=methods,
        test_partitions=test_partitions,
        title_suffix=title_suffix,
    )
