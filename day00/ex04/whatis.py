import sys

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
except AssertionError as e:
    print(f"{type(e).__name__}: {e}")
    sys.exit(1)

try:
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        assert argument.lstrip("-").isdigit(), "argument is not an integer"
        argument_as_int = int(argument)
        if argument_as_int % 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")
except AssertionError as e:
    print(f"{type(e).__name__}: {e}")
    sys.exit(1)