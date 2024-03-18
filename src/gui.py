import tkinter as tk
from algorithm import *
from bruteforce import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from tkinter import ttk
import time

def process_point():
    global canvas, warn_label, iterate, points, result_points, exec_label
    points = []
    try:
        clear_warn_label()
        clear_graph()
        iterate = int(iterate_entry.get())
        for i in range (jumlah_titik):
            x, y = map(float, arr[i].get().split())
            points.append((x,y))
        result_points = []
        start = time.time()
        bezierDnC(points, result_points, iterate)
        stop = time.time()
        exec_time = stop-start
        result_points = np.array(result_points)
        points = np.array(points)
        generate_plot(points, result_points)
        update_exec(exec_time)
    except ValueError:
        clear_warn_label()
        warn_label = tk.Label(text="Pastikan input yang diberikan sudah sesuai")
        warn_label.grid(row=13,column=0, columnspan=3, sticky=tk.W+tk.E)
        root.columnconfigure(1, weight=0)
    except NameError:
        clear_warn_label()
        warn_label = tk.Label(text="Iterate-nya diisi mas")
        warn_label.grid(row=13,column=0, columnspan=3, sticky=tk.W+tk.E)
        root.columnconfigure(1, weight=0)
    
def input_titik():
    global arr, label_point, jumlah_titik, submit_button, canvas, warn_label
    clear_graph()
    clear_warn_label()
    clear_grid()
    clear_exec()
    reset()
    try:
        jumlah_titik = int(n.get())
        if jumlah_titik < 3:
            clear_warn_label()
            warn_label = tk.Label(text="Jumlah titik minimal 3, Mas")
            warn_label.grid(row=13,column=0, columnspan=3,sticky=tk.W+tk.E)
        else:
            arr = [0 for i in range (jumlah_titik)]
            label_point = [0 for i in range (jumlah_titik)]
            for i in range (jumlah_titik):
                label_point[i] = tk.Label(inner_frame, text=f"Masukkan P{i}:")
                label_point[i].grid(row=i+2,column=0,sticky=tk.W)
                arr[i] = tk.Entry(inner_frame)
                arr[i].grid(row=i+2,column=1, sticky=tk.W, padx=80)
            
    except ValueError:
        clear_warn_label()
        warn_label = tk.Label(text="Pastikan input yang diberikan sudah sesuai")
        warn_label.grid(row=13,column=0, columnspan=3,sticky=tk.W+tk.E)

def show_all():
    global graph
    f = Figure(figsize = (5.4,5.4), dpi = 100)
    fig = f.add_subplot(111)
    fig.plot(points[:, 0], points[:, 1], 's--', label='Control Points', color='gray')
    for i in range (1, iterate+1):
        result = []
        bezierDnC(points, result, i)
        result = np.array(result)
        fig.plot(result[:, 0], result[:, 1], 'o-', label=f'Iterasi ke-{i}')
        fig.legend()
        fig.set_title('DnC Bézier Curve')
        fig.set_xlabel('X-axis')
        fig.set_ylabel('Y-axis')
    graph = FigureCanvasTkAgg(f, master=root)
    graph.draw()
    graph.get_tk_widget().grid(row=0, column=5, rowspan=30)

def update_exec(time):
    global exec_label
    try:
        exec_label.grid_remove()
        exec_label = tk.Label(root, text=f"Execution time: {time} ms")
        exec_label.grid(row=40, column=5, sticky="w")   
    except:
        pass

def clear_exec():
    global exec_label
    try:
        exec_label.grid_remove()
        exec_label = tk.Label(root, text=f"Execution time: 0 ms")
        exec_label.grid(row=40, column=5, sticky="w")   
    except:
        pass

def clear_submit_button():
    global submit_button
    try:
        if submit_button != None:
            submit_button.grid_remove()
    except:
        pass

def clear_grid():
    global arr, label
    try:
        if arr != None and label != None:
            for i in range (jumlah_titik):
                label_point[i].grid_remove()
                arr[i].grid_remove()
    except:
        pass

def clear_graph():
    global graph
    try:
        if graph != None:
            graph.get_tk_widget().destroy()
        empty_graph()
    except NameError:
        pass

def clear_warn_label():
    global warn_label
    try:
        if warn_label != None:
            warn_label.grid_remove()
    except:
        pass

def reset():
    global points, iterate, result_points
    points = []
    iterate = None
    result_points = []

def generate_plot(control_points, bezier_points):
    global graph
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
        graph.get_tk_widget().grid(row=0, column=5, rowspan=30)
    except:
        pass

def empty_graph():
    global graph
    f = Figure(figsize = (5.4,5.4), dpi = 100)
    fig = f.add_subplot(111)
    fig.set_title('DnC Bézier Curve')
    fig.set_xlabel('X-axis')
    fig.set_ylabel('Y-axis')
    graph = FigureCanvasTkAgg(f, master=root)
    graph.draw()
    graph.get_tk_widget().grid(row=0, column=5, rowspan= 30)

def set_scrollregion(event):
    canvas.config(scrollregion=canvas.bbox("all"))

def checkbox_handler():
    try:
        if checkbox_var.get():
            show_all()
        else:
            generate_plot(points, result_points)
    except:
        pass
        
def animate_graph():
    global iterate, warn_label
    try:
        iterate = int(iterate_entry.get())
        for i in range(1, iterate + 1):
            result = []
            bezierDnC(points, result, i)
            result = np.array(result)
            root.after(i*1000, lambda result=result:generate_plot(points, result))
    except:
        clear_warn_label()
        warn_label = tk.Label(text="Error animate")
        warn_label.grid(row=13,column=0, columnspan=3,sticky=tk.W+tk.E) 
    

# MAIN
root = tk.Tk()

root.title("Bezier Curve")
empty_graph()
top_frame = ttk.Frame(root)
top_frame.grid(row=0, column=0, sticky="ew")

# Create a label
label = tk.Label(top_frame, text="Masukkan banyak titik:")
label.grid(row=0, column=0, sticky=tk.W)

# Input N
n = tk.Entry(top_frame)
n.grid(row=0, column=1, sticky=tk.W)

# Submit N button
submit_n_button = tk.Button(top_frame, text="Submit", command=input_titik)
submit_n_button.grid(row=0, column=2, padx=10, sticky=tk.W)

scroll_frame = ttk.Frame(top_frame)
scroll_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")

canvas = tk.Canvas(scroll_frame, height=400)
canvas.pack(side="left", fill="both", expand=True)

entry_frame = ttk.Frame(scroll_frame)
entry_frame.pack(side="left", fill="y")

scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
# Link the scrollbar to the canvas
canvas.configure(yscrollcommand=scrollbar.set)

# Bind the event to update scroll region
canvas.bind("<Configure>", set_scrollregion)

checkbox_var = tk.BooleanVar()
iterate_label = tk.Label(top_frame, text="Masukkan banyak iterasi:")
iterate_label.grid(row=9,column=0, sticky=tk.W)
iterate_entry = tk.Entry(top_frame)
iterate_entry.grid(row=9, column=1, sticky=tk.W)
submit_button = tk.Button(root, text="Submit", command=process_point)
submit_button.grid(row=10, column=0)
animate_button = tk.Button(root, text="Animate", command=animate_graph)
animate_button.grid(row=11,column=0)
check_button = ttk.Checkbutton(root, text="Tampilkan semua iterasi", command=checkbox_handler, variable=checkbox_var)
check_button.grid(row=12, column=0)

exec_label = tk.Label(root, text="Execution time: 0 ms")
exec_label.grid(row=40, column=5, sticky="w")

# Create another frame inside the canvas to hold the input fields
inner_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")
inner_frame.bind("<Configure>", set_scrollregion)

arr = []
label_point = []


# Run the main event loop
root.mainloop()