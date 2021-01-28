from base import *

# Checks if the polygon is convex or not
# (points are given in the right order)


def polygon_is_convex(polygon: List[Tuple[int, int]]):
    rotation = None

    for first_point_index in range(len(polygon)):
        second_point_index = (first_point_index + 1) % len(polygon)
        third_point_index = (first_point_index + 2) % len(polygon)

        this_rot = point_orient(
            polygon[first_point_index],
            polygon[second_point_index],
            polygon[third_point_index]
        )
        if this_rot == 0:
            continue

        if rotation is None:
            rotation = this_rot
        else:
            if rotation != this_rot:
                return False

    return True



n = int(input())
pnts = []
for i in range(n):
    pnts.append(tuple(map(int, input().split())))

if polygon_is_convex(pnts):
    print("YES")
else:
    print("NO")
