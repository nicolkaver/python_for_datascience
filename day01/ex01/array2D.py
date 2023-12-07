import numpy as np
import sys

def slice_me(family: list, start: int, end: int) -> list:
    np_array = np.array(family)
    try:
        assert isinstance(family, list), "Family argument must be a list"
        same_length = (np.diff(np_array.shape[:-1]) == 0).all()
        assert same_length == True, "All rows do not have the same length"
    except AssertionError as e:
        print(f"{type(e).__name__} : {e}")
        sys.exit(1)

    print(f"My shape is : {np_array.shape}")

    truncated_array = np_array[start : end]
    print("My new shape is : ")

    return truncated_array.tolist()
