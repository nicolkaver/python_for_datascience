from ft_filter import ft_filter

def isPositive(numberToTest):
    return numberToTest > 0

def main():
    listOfNumbers = [-1, 1, 5, -2]
    positive_numbers = ft_filter(isPositive, listOfNumbers)
    # it is important to convert it back to a list
    print(list(positive_numbers))

if __name__ == "__main__":
    main()