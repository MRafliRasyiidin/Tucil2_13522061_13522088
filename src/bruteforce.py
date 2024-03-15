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


# TESTING
points = []

points_ex = [(1, 2), (5, 10), (10, 10), (14,2), (15,8), (17,10), (20,1)]
bezierBF(points_ex, len(points_ex), 100, points)
points.append(points_ex[0])
points.append(points_ex[len(points_ex)-1])
points.sort()
print(points)

excluded = []
for i in range (1,len(points_ex)):
    excluded.append(points_ex[i])

x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]
exc_x = [point[0] for point in excluded]
exc_y = [point[1] for point in excluded]
# Plot the points
plt.plot(x_coords, y_coords, 'bo')  # 'bo' stands for blue circles
plt.scatter(exc_x,exc_y)


# Connect the points with lines
plt.plot(x_coords, y_coords, 'r-')  # 'r-' stands for red lines

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Brute Force Bézier Curve')

# Show the plot
plt.grid(True)
plt.show()
