import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np

def printTitle():
    print("-----------------------------------------------------------------------------------------")
    print("|    Membangun Kurva Bézier dengan Algoritma Titik Tengah berbasis Divide and Conquer   |")
    print("-----------------------------------------------------------------------------------------")

def inputPoints(n):
    points = []
    for i in range(n):
        while True:
            try:
                line = input(f"Masukan point ke-{i+1} (format 'x y'): ")
                x_str, y_str = line.split()
                x, y = int(x_str), int(y_str)
                points.append((x, y))
                break
            except ValueError:
                print("Input salah! Pastikan input merupakan integer dan dibagi oleh satu spasi!")
    points = np.array(points)
    return points

def inputN():
    N = 0
    while True:
            try:
                N = int(input("Masukan banyak titik kontrol (N >= 3): "))
            except ValueError:
                print("Pastikan input merupakan angka!!")
                continue
            else:
                if N < 3:
                    print("Pastikan N lebih besar dari 2!!")
                else:
                    break
    return N

def inputIteration():
    iteration = 0
    while True:
        try:
            iteration = int(input("Masukan banyak iterasi yang diinginkan(iterasi > 0): "))
        except ValueError:
            print("Pastikan input merupakan angka!!")
            continue
        else:
            if iteration < 0:
                print("Pastikan iteration lebih besar dari 0!!")
            else:
                break
    return iteration

def generatePlot(initialControlPoints, bezierPoints):
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

def menuOptions():
    print("Silahkan pilih menu : ")
    print("1. Bezier Curve dengan hasil akhir saja")
    print("2. Bezier Curve dengan animasi per iterasi")
    print("3. Exit program")
    opsi = 0
    while True:
        try:
            opsi = int(input("Masukan opsi(1-3): "))
        except ValueError:
            print("Pastikan input merupakan angka!!")
            continue
        else:
            if opsi < 1 or opsi > 3:
                print("Pastikan opsi antara 1 dan 3!!")
            else:
                break
    return opsi