def mae(expected_val, actual_val):
    return abs(expected_val - actual_val)


def mse(expected_val, actual_val):
    return (expected_val - actual_val) ** 2
