import sys
from typing import List
import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        assert len(height) == len(weight), "The lists are not the same size"
        for value in height:
            assert isinstance(value, (int, float)), "List should only contain int or float values"
        for value in weight:
            assert isinstance(value, (int, float)), "List should only contain int or float values"
    except AssertionError as e:
        print(f"{type(e).__name__} : {e}")
        sys.exit(1)

    result = []

    for x, y in zip(height, weight):
        new_bmi = y / (x ** 2)
        result.append(new_bmi)
    return result

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        for value in bmi:
            assert isinstance(value, (int, float)), "List should only contain int or float values"
        assert isinstance(limit, int), "Limit must be an integer"
    except AssertionError as e:
        print(f"{type(e).__name__} : {e}")
        sys.exit(1)
    
    # bool_array: List[bool] = []
    # for value in bmi:
    #     bool_value = False
    #     if value > limit:
    #         bool_value = True
    #     bool_array.append(bool_value)

    result = np.array(bmi)
        
    return result > limit