import numpy as np
import matplotlib.pyplot as plt
import dp_triangulation

#This code uses matplotlib to display an empty plot and waits for the user to click on it to add vertices to the polygon. 
# The user can add as many vertices as they want by clicking on the plot. 
# To stop adding vertices and return the polygon, the user can simply close the plot window.

def draw_polygon():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_aspect('equal')
    polygon = []
    while True:
        points = np.array(plt.ginput(1, timeout=0))
        if len(points) == 0:
            break
        polygon.append((points[0][0], points[0][1]))
        ax.plot(points[0][0], points[0][1], 'ro')
        plt.draw()
    
    plt.close(fig)
    return polygon

# Example usage
polygon = draw_polygon()

dp_triangulation.dp_triangulation(polygon)