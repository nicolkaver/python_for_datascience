import sys
from ft_filter import ft_filter

def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        argv1 = sys.argv[1]
        assert type(argv1) == str, "The first argument must be a string"
        argv2 = sys.argv[2]
        assert argv2.isdigit(), "The second argument must be an integer"
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
        sys.exit(1)

    list_to_filter = argv1.split(" ")
    filtered_list = ft_filter(lambda str: len(str) > int(argv2), list_to_filter)
    print(list(filtered_list))

if __name__ == "__main__":
    main()