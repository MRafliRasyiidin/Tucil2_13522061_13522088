from math import factorial
import numpy as np

def midPoint(P1, P2):
    return ((P1[0] + P2[0]) / 2,(P1[1] + P2[1]) / 2)

def bezierDnC(controlPoints, bezierPoints, iteration):
    if iteration == 0:
        bezierPoints.append(controlPoints[0])
        bezierPoints.append(controlPoints[-1])
        return
    else:
        leftControlPoints = []
        rightControlPoints = []
        while len(controlPoints) > 1:
            leftControlPoints.append(controlPoints[0])
            rightControlPoints.insert(0, controlPoints[-1])

            newControlPoints = []
            for i in range(len(controlPoints) - 1):
                newControlPoints.append(midPoint(controlPoints[i], controlPoints[i+1]))
            controlPoints = newControlPoints

        leftControlPoints.append(controlPoints[0])
        rightControlPoints.insert(0, controlPoints[0])

        bezierDnC(leftControlPoints, bezierPoints, iteration-1)
        bezierDnC(rightControlPoints, bezierPoints, iteration-1)

def bezierBF(list, nTitik, iterasi, points):
    inc = 1/iterasi
    N = nTitik-1
    for t in np.arange(inc,1,inc):
        x = 0
        y = 0
        list_index = 0
        nPangkat_p = N
        nPangkat_t = 0
        p = 1-t
        for j in range (0,nTitik):
            fact = (factorial(N)//(factorial(j)*factorial(N-j))) 
            x += fact*(p**nPangkat_p)*(t**nPangkat_t)*(list[list_index][0])
            y += fact*(p**nPangkat_p)*(t**nPangkat_t)*(list[list_index][1])
            list_index += 1
            nPangkat_p -= 1
            nPangkat_t += 1
        points.append((x,y))
    
def bezierTigaDnC(P0, P1, P2, iterasi, points):
    if iterasi == 0:
        points.append(P0)
        points.append(P2)
    else:
        M0 = (P0 + P1) / 2
        M1 = (P1 + P2) / 2
        Q = (M0 + M1) / 2
        bezierDnC(P0, M0, Q, iterasi - 1, points)
        bezierDnC(Q, M1, P2, iterasi - 1, points)