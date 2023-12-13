from pyparsing import Any

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    numeric_values = [value for value in args if isinstance(value, (int, float))]
    
    # mean
    mean = sum(args) / len(args) if args else None
    print(f"mean : {mean}")

    # median
    sorted_num_values = sorted(numeric_values)
    length = len(sorted_num_values)

    median = 0
    if length % 2 == 0:
        middle_right = sorted_num_values[length // 2]
        middle_left = sorted_num_values[length // 2 - 1]
        median = (middle_left + middle_right) / 2
    else:
        median = sorted_num_values[length // 2]
    print(f"median : {median}")

    # quartiles
    # q1_index = (length - 1) // 4
    # q2_index = (length - 2) // 2
    # q3_index = q2_index + q1_index