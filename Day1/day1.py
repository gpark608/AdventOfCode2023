import re

qOneAnswer = 0
qTwoAnswer = 0
stringToInt = {
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
def findDigit(line):
    digits=re.findall(r'\d', line)
    firstDigit = digits[0]
    lastDigit = digits[-1]
    answer = firstDigit+lastDigit
    return int(answer)

def includeStrings(line):
    digits=re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|ten|\d))', line)
    firstDigit = digits[0]
    lastDigit = digits[-1]
    
    if firstDigit in stringToInt:
        firstDigit = stringToInt[firstDigit]
    if lastDigit in stringToInt:
        lastDigit = stringToInt[lastDigit]
    answer = firstDigit+lastDigit
    return int(answer)

with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        qOneAnswer += findDigit(line)
        qTwoAnswer +=includeStrings(line)
    print(qOneAnswer)
    print(qTwoAnswer)


