import numpy as np
import matplotlib.pyplot as plt

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


#TESTING
initialControlPoints = [(0, 0), (1, 2), (3, 2), (4, 0),(5,4)]
bezierPoints = []
bezierDnC(initialControlPoints, bezierPoints, 3)
bezierPoints = np.array(bezierPoints)

plt.figure()
plt.plot(bezierPoints[:, 0], bezierPoints[:, 1], 'o-', label='DnC Bézier Curve')
initialControlPoints = np.array(initialControlPoints)
plt.plot(initialControlPoints[:, 0], initialControlPoints[:, 1], 's--', label='Control Points', color='gray')
plt.legend()
plt.grid(True)
plt.title('DnC Bézier Curve')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()