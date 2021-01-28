from random import random

from base import *

# Checks if the given point lies in the middle of the polygon
# (the polygon isn't necessarily convex)


def ray_intersects_segment(ray_pnt, ray_direction, segment_point1, segment_point2):
    pass


def point_lies_in_polygon(point, polygon):
    # Views a ray from the given point and understands
    # if the number of intersections is even or odd

    # Select direction:
    # TODO: select two vertexes for which the angle is next to each other
    # and direction is the sum of the vectors
    direction = random()  # Its tangent, let it be from 0 to one

    intersections = 0
    for i in range(len(polygon)):
        first_point = polygon[i]
        second_point = polygon[(i + 1) % len(polygon)]
        if ray_intersects_segment(point, direction, first_point, second_point):
            intersections += 1

    return bool(intersections % 2)


data = []
n, px, py = map(int, input().split())

for _ in range(n):
    data.append(tuple(map(int, input().split())))

if point_lies_in_polygon((px, py), data):
    print("YES")
else:
    print("NO")


