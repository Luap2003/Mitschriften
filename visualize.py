import numpy as np
import plotly.graph_objs as go

def create_sphere(radius):
    sphere = np.zeros((2*radius+1, 2*radius+1, 2*radius+1))

    for x in range(-radius, radius+1):
        for y in range(-radius, radius+1):
            for z in range(-radius, radius+1):
                if x**2 + y**2 + z**2 <= radius**2:
                    sphere[x+radius, y+radius, z+radius] = 1

    return sphere

def plot_sphere(sphere):
    x_values = []
    y_values = []
    z_values = []

    for x in range(sphere.shape[0]):
        for y in range(sphere.shape[1]):
            for z in range(sphere.shape[2]):
                if sphere[x, y, z] == 1:
                    x_values.append(x)
                    y_values.append(y)
                    z_values.append(z)

    scatter = go.Scatter3d(
        x=x_values,
        y=y_values,
        z=z_values,
        mode='markers',
        marker=dict(
            size=6,
            color='blue',
            line= dict (
                color = 'black',
                width = 0.4),
            opacity=0.1,  # Erhöhe die Opazität der Marker
            symbol='square'  # Ändere die Markerform zu Würfeln
        ),
        #opacity= 0.1
    )

    layout = go.Layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        )
    )

    fig = go.Figure(data=[scatter], layout=layout)
    fig.show()

radius = 10
sphere = create_sphere(radius)
plot_sphere(sphere)
