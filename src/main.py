from utilities import *
import time
from algorithm import *
from bruteforce import *

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
            animate_graph(controlPoints, iteration)
            stop = time.time()
            print(f"Runtime: {stop - start} ms")
        elif opsi == 3:
            N = inputN()
            controlPoints = inputPoints(N)
            iteration = inputIteration()
            bezierPoints = []
            start = time.time()
            bezierBF(controlPoints, N, 2**(iteration), bezierPoints)
            stop = time.time()
            print(f"Runtime: {stop - start} ms")
            generatePlotBF(controlPoints,bezierPoints)
        else:
            run = False
            print("Jaa matanee ~ ~")