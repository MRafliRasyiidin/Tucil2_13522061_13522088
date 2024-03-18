from math import factorial
import matplotlib.pyplot as plt
import numpy as np

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