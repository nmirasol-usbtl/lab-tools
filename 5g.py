
# nunc stack number back-calculator
# NSNBC
# MSNBC
# MSM
# COVID CONSPIRACY
# 5G :)

from flask import Flask, render_template

stacks = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD']

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('input.html')

# used for testing only
def calc(plateNumber):
    numberInStack = plateNumber % 20
    stackNumber = (plateNumber - numberInStack) / 20

    if plateNumber < 20:
        stackNumber = 0
    elif numberInStack == 0:
        stackNumber -= 1
        numberInStack = 20
    
    stack = str(stacks[int(stackNumber)])

    if numberInStack < 10:
        numberInStack = '0' + str(numberInStack)

    return stack + str(numberInStack)

# used for testing only
def backCalc(stackNum):
    length = len(stackNum)
    letter = None
    index_number, index_str, number = 0, 0, 0

    index_number = 1 if length == 3 else 2
    index_str = index_number

    number = stackNum[index_number:]
    letter = stackNum[0:index_str]
    pos = 20 * stacks.index(letter)

    return pos + int(number)

#var = calc(193)
#print(var)
#print(backCalc(var))

app.run()
