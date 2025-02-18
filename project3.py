#Warnocks Algorithm
import matplotlib.pyplot as plt #for plotting
import numpy as np  #numerical operations

def is_visible(x,y,polygon):#checks if a point x,y is inside a polygon
    n = len(polygon)        #number of vertices
    inside = False          #initialize inside to False
    p1x,p1y = polygon[0]      #initialize the first vertex
    for i in range(n+1):       #loop through all the vertices
        p2x,p2y = polygon[i % n]#get the next vertex
        if y > min(p1y,p2y):     #check if the y coordinate is greater than the minimum y coordinate
            if y <= max(p1y,p2y):#check if the y coordinate is less than the maximum y coordinate
                if x <= max(p1x,p2x):#check if the x coordinate is less than the maximum x coordinate
                    if p1y != p2y:#check if the y coordinates are not equal
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x# calculate the intersection point
                    if p1x == p2x or x <= xinters:#check if the x coordinate is less than the intersection point
                        inside = not inside#change the value of inside
        p1x,p1y = p2x,p2y#set the current vertex as the next vertex
    return inside


def color_pixel(x, y, color):
    plt.plot(x, y, color)

def warnock_algorithm(x_min, x_max, y_min, y_max, depth,polygons):
    if depth > MAX_DEPTH:
        return
    #x_min, x_max: The horizontal boundaries of the area.
    #y_min, y_max: The vertical boundaries of the area.
    #depth: The current depth of recursion.
    
    # Base case: if area is trivially small(its width and height are less than
    #equal to 1 pixel)
    if (x_max - x_min <= 1) and (y_max - y_min <= 1):
        # Resolve visibility for the single pixel
        for polygon in polygons:
            if is_visible((x_min + x_max)/ 2 ,(y_min + y_max)/2,polygon['vertices']):
                 color_pixel((x_min + x_max) / 2,(y_min + y_max) /2,polygon['color']) #colors the pixel
                 break
        return

    # Subdivide the area into 4 quadrants
    x_mid = (x_min + x_max) // 2
    y_mid = (y_min + y_max) // 2

    warnock_algorithm(x_min, x_mid, y_min, y_mid, depth + 1, polygons)
    warnock_algorithm(x_mid, x_max, y_min, y_mid, depth + 1, polygons)
    warnock_algorithm(x_min, x_mid, y_mid, y_max, depth + 1, polygons)
    warnock_algorithm(x_mid, x_max, y_mid, y_max, depth + 1, polygons)

# Define two overlapping polygons (images)
polygon1 = {
    'vertices': [(2, 1), (5, 1), (5, 4), (2, 4)],
    'color': 'r.'  # Red color
}
polygon2 = {
    'vertices': [(3, 2), (6, 2), (6, 5), (3, 5)],
    'color': 'b.'  # Blue color
}
polygons = [polygon1, polygon2]

# Example usage
MAX_DEPTH = 4 # Set a limit to avoid infinite recursion
warnock_algorithm(0, 8, 0, 8, 0,polygons)
plt.gca().invert_yaxis()
plt.show()