import sys

def building(textToCount):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuation_count = 0
    spaces_count = 0

    for char in textToCount:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in punctuation_chars:
            punctuation_count += 1
        elif char.isspace():
            spaces_count += 1
        
    print(f"The text contains {len(textToCount)} characters:")
    print(f"{uppercase_count} upper letters")
    print(f"{lowercase_count} lowe letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{spaces_count} spaces")
    print(f"{digit_count} digits")

def main():
    try:
        assert len(sys.argv) == 2, "What is the text to count?"
        textToCount = sys.argv[1]
        building(textToCount)
    except AssertionError as e:
        print(f"{e}") 

if __name__ == "__main__":
    main()