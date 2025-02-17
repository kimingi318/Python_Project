#Warnocks Algorithm
import matplotlib.pyplot as plt #for plotting
import numpy as np  #numerical operations

def warnock_algorithm(x_min, x_max, y_min, y_max, depth):
    if depth > MAX_DEPTH:
        return
    #x_min, x_max: The horizontal boundaries of the area.
    #y_min, y_max: The vertical boundaries of the area.
    #depth: The current depth of recursion.
    
    # Base case: if area is trivially small(its width and height are less than
    #equal to 1 pixel)
    if (x_max - x_min <= 1) and (y_max - y_min <= 1):
        # Resolve visibility for the single pixel
        color_pixel(x_min, y_min)#colors the pixel
        return

    # Subdivide the area into 4 quadrants
    x_mid = (x_min + x_max) // 2
    y_mid = (y_min + y_max) // 2

    warnock_algorithm(x_min, x_mid, y_min, y_mid, depth + 1)
    warnock_algorithm(x_mid, x_max, y_min, y_mid, depth + 1)
    warnock_algorithm(x_min, x_mid, y_mid, y_max, depth + 1)
    warnock_algorithm(x_mid, x_max, y_mid, y_max, depth + 1)

def color_pixel(x, y):
    plt.plot(x, y, 'bo')  # Blue dot for the pixel

# Example usage
MAX_DEPTH = 3  # Set a limit to avoid infinite recursion
warnock_algorithm(0, 8, 0, 8, 0)
plt.show()