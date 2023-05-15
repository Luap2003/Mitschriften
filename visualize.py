import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function z = x * y
def func(x, y):
    return x * y

# Create a meshgrid for x and y
x = np.linspace(0, 1, 1000)
y = np.linspace(0, 1, 1000)
x_grid, y_grid = np.meshgrid(x, y)

# Check if x^2 + y^2 <= 1 and mask the values that don't satisfy the condition
mask = x_grid**2 + y_grid**2 <= 1
z_grid = np.where(mask, func(x_grid, y_grid), np.nan)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_grid, y_grid, z_grid)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()
