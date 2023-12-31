def get_digits(text):
    # Remove any non-digit characters from the text
    digits = ''.join(filter(str.isdigit, text))

    firstDigit = digits[0] if digits else None
    lastDigit = digits[-1] if digits else None

    return firstDigit, lastDigit


file1 = open("puzzle-input-day1.txt", 'r')
Lines = file1.readlines()

sumNumbers = 0
# Process each line of text
for line in Lines:
    firstDigit, lastDigit = get_digits(line.strip())
    combinedNumber = int(str(firstDigit) + str(lastDigit)) if firstDigit and lastDigit else None
    sumNumbers += combinedNumber


print("Overall sum of numbers:", sumNumbers)
#Answer Part 1: 53974
