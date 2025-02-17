#weiher_atherton algorithm
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

def weiler_atherton(subject_polygon, clip_polygon):
    subject = Polygon(subject_polygon)
    clip = Polygon(clip_polygon)
    result = subject.intersection(clip)
    return result

# Example polygons
subject_polygon = [(2, 1), (4, 1), (4, 3), (2, 3)]# the polygon that is to be clipped
clip_polygon = [(1, 0), (5, 0), (5, 2), (1, 2)]#thr polygon that is to be used to clip the subject polygon

result = weiler_atherton(subject_polygon, clip_polygon)

# Plotting the polygons
plt.plot(*zip(*subject_polygon, subject_polygon[0]), 'r-', label='Subject Polygon')
plt.plot(*zip(*clip_polygon, clip_polygon[0]), 'b-', label='Clip Polygon')
if result.is_empty:
    print("No intersection")
else:
    plt.plot(*zip(*result.exterior.coords), 'g-', label='Clipped Polygon')

plt.legend()
plt.show()