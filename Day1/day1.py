import re

qOneAnswer = 0
def findDigit(line):
    digits=re.findall(r'\d', line)
    firstDigit = digits[0]
    lastDigit = digits[-1]
    answer = firstDigit+lastDigit
    return int(answer)

def includeStrings(line):
    
    return 0
with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        qOneAnswer += findDigit(line)
    print(qOneAnswer)


