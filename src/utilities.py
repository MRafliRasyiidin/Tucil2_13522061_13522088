import matplotlib.pyplot as plt
from algorithm import *
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
                x, y = float(x_str), float(y_str)
                points.append((x, y))
                break
            except ValueError:
                print("Input salah! Pastikan input merupakan angka dan dibagi oleh satu spasi!")
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

def generatePlotBF(initialControlPoints, bezierPoints):
    bezierPoints = np.array(bezierPoints)
    plt.figure()
    plt.plot(bezierPoints[:, 0], bezierPoints[:, 1], 'o-', label='Brute Force Bézier Curve')
    initialControlPoints = np.array(initialControlPoints)
    plt.plot(initialControlPoints[:, 0], initialControlPoints[:, 1], 's--', label='Control Points', color='gray')
    plt.legend()
    plt.grid(True)
    plt.title('Brute Force Bézier Curve')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

def menuOptions():
    print("Silahkan pilih menu : ")
    print("1. Bezier Curve dengan algoritma Divide and Conquer")
    print("2. Bezier Curve dengan animasi per iterasi")
    print("3. Bezier Curve dengan algoritma Brute Force")
    print("4. Exit program")
    opsi = 0
    while True:
        try:
            opsi = int(input("Masukan opsi(1-4): "))
        except ValueError:
            print("Pastikan input merupakan angka!!")
            continue
        else:
            if opsi < 1 or opsi > 4:
                print("Pastikan opsi antara 1 dan 4!!")
            else:
                break
    return opsi

def animate_graph(control_points, iterate):
    root= tk.Tk()
    root.title("Bézier Curve Animation")
    for i in range(1, iterate + 1):
            result = []
            bezierDnC(control_points, result, i)
            result = np.array(result)
            root.after(i*1000, lambda result=result:animate_handler(control_points, result))

    def animate_handler(control_points, bezier_points):
        try:
            f = Figure(figsize = (5.4,5.4), dpi = 100)
            fig = f.add_subplot(111)
            fig.plot(bezier_points[:, 0], bezier_points[:, 1], 'o-', label='DnC Bézier Curve')
            fig.plot(control_points[:, 0], control_points[:, 1], 's--', label='Control Points', color='gray')
            fig.legend()
            fig.set_title('DnC Bézier Curve')
            fig.set_xlabel('X-axis')
            fig.set_ylabel('Y-axis')
            graph = FigureCanvasTkAgg(f, master=root)
            graph.draw()
            graph.get_tk_widget().grid(row=0, column=0)
        except:
            pass
    
    root.mainloop()