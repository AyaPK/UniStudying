import random
import itertools

inputLabels = "ABCD"
inputs = input("How many inputs? ")
topRow = ""


def makeBinary():
    binary = list(itertools.product(["0", "1"], repeat=int(inputs)))
    return binary

def makeOutputs():
    outputs = []
    for x in range(0, 2**int(inputs)):
        outputs.append(random.randint(0,1))
    return outputs

def makeTopRow():
    global inputLabels
    global inputs
    global topRow
    topRow = ""
    for x in range(0, int(inputs)):
        toAdd = f"| {inputLabels[x]} "
        topRow = topRow+toAdd
    topRow = topRow+"|   | Z |"
    print("-"*len(topRow))
    print(topRow)
    print("-"*len(topRow))

def insertBinary():
    binary = makeBinary()
    outputs = makeOutputs()
    for x in range(0, len(binary)):
        thisrow = ""
        for y in binary[x]:
            thisrow = thisrow+f"| {y} "
        thisrow = thisrow+f"|   | {outputs[x]} |"
        print(thisrow)

def tableBase():
    print("-" * len(topRow))


makeTopRow()
insertBinary()
tableBase()

close = input("Press enter to close when you're finished.")