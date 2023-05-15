import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter
t = np.linspace(0, 8 * np.pi, num=1000)

# Spirale-Funktion
x = np.cos(t)
y = np.sin(t)
z = t

# 3D-Plot erstellen
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)

# Achsenbeschriftung
ax.set_xlabel('X-Achse')
ax.set_ylabel('Y-Achse')
ax.set_zlabel('Z-Achse')

# Titel
ax.set_title('3D-Aufsteigende Spirale')

# Plot anzeigen
plt.show()
