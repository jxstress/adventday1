import re

def convertNumberWordsDigits(text):
    spellNumbers = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    numbers = re.findall(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', text)
    # text = text.lower()
    convertedLine = []

    for number in numbers:
        if number in spellNumbers:
            convertedLine.append(spellNumbers[number])
        else:
            convertedLine.append(number)
    
    return ''.join(convertedLine)

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
    convertLine = convertNumberWordsDigits(line.strip())
    firstDigit, lastDigit = get_digits(convertLine)
    combinedNumber = int(str(firstDigit) + str(lastDigit)) if firstDigit and lastDigit else None
    sumNumbers += combinedNumber


print("Overall sum of numbers:", sumNumbers)
#Answer Part 1: 53974
#ANser part 2: 52840
