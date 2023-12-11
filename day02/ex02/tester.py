from load_csv import load
import sys

def main():
    try:
        assert len(sys.argv) > 1, "Wrong number of arguments"
    except AssertionError as e:
        print(f"{type(e).__name__} : {e}")
        sys.exit(1)
    load(sys.argv[1], "France", "Slovak Republic")

if __name__ == "__main__":
    main()