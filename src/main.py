from utilities import *
import time
from algorithm import *

if __name__ == "__main__":
    run = True
    N = 0
    while run:
        printTitle()
        opsi = menuOptions()
        if opsi == 1:
            N = inputN()
            controlPoints = inputPoints(N)
            iteration = inputIteration()
            bezierPoints = []
            start = time.time()
            bezierDnC(controlPoints, bezierPoints, iteration)
            stop = time.time()
            print(f"Runtime: {stop - start} ms")
            generatePlot(controlPoints,bezierPoints)
        elif opsi == 2:
            N = inputN()
            controlPoints = inputPoints(N)
            iteration = inputIteration()
            bezierPoints = []
            start = time.time()
            bezierDnC(controlPoints, bezierPoints, iteration)
            stop = time.time()
            print(f"Runtime: {stop - start} ms")
            # to be added
        else:
            run = False
            print("Jaa matanee ~ ~")