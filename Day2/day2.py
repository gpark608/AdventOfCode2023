import re

colorSet = {'red': 12, 'green': 13, 'blue': 14}
qOneAnswer = 0
qTwoAnswer = 0

def separateColors(colors):
    separate=re.split(r'[,;]', colors)
    stripped=list(map(str.strip, separate))
    return stripped

def validGame(separatedColors) -> bool:
    for color in separatedColors:
        number, c = color.split(' ')
        if colorSet[c] < int(number):
            return False
    return True

def fewestNumberOfCubes(separatedColors):
    fewestCubes = {'red': 0, 'green': 0, 'blue': 0}
    for color in separatedColors:
        number, c = color.split(' ')
        if fewestCubes[c] < int(number):
            fewestCubes[c] = int(number)
    answer = fewestCubes['red'] * fewestCubes['blue'] * fewestCubes['green']
    return answer

with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        game,colors=line.split(':')
        separatedColors=separateColors(colors)
        if validGame(separatedColors):
            qOneAnswer += int(game[4:])
        qTwoAnswer += fewestNumberOfCubes(separatedColors)
    print(f'Question One Answer is: {qOneAnswer}')
    print(f'Question Two Answer is: {qTwoAnswer}')


