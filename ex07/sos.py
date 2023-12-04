NESTED_MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", 
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    " ": "/"
}

import sys

def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        argv1 = sys.argv[1]
        for char in argv1:
            assert char.isalnum() | char.isspace(), "the arguments are bad"
        for i, char in enumerate(argv1):
            if char.isalpha() & char.islower():
                char_bis = char.upper()
                if i == len(argv1) - 1:
                    print(NESTED_MORSE[char_bis])
                else:
                    print(NESTED_MORSE[char_bis], end = " ")
            else:
                if i == len(argv1) -1:
                    print(NESTED_MORSE[char])
                else:
                    print(NESTED_MORSE[char], end = " ")
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()