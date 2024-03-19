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
            start = time.perf_counter()
            bezierDnC(controlPoints, bezierPoints, iteration)
            stop = time.perf_counter()
            print(f"Runtime: {(stop - start)*1000} ms")
            generatePlot(controlPoints,bezierPoints)
        elif opsi == 2:
            N = inputN()
            controlPoints = inputPoints(N)
            iteration = inputIteration()
            bezierPoints = []
            animate_graph(controlPoints, iteration)
        elif opsi == 3:
            N = inputN()
            controlPoints = inputPoints(N)
            iteration = inputIteration()
            bezierPoints = []
            start = time.perf_counter()
            bezierBF(controlPoints, N, 2**(iteration), bezierPoints)
            stop = time.perf_counter()
            print(f"Runtime: {(stop - start)*1000} ms")
            generatePlotBF(controlPoints,bezierPoints)
        else:
            run = False
            print("Jaa matanee ~ ~")