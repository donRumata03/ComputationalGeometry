from typing import *


def sgn(x):
    return 1 if x > 0 else (-1 if x < 0 else 0)


def cross_product(v1: Tuple[int, int], v2: Tuple[int, int]):
    return v1[0] * v2[1] - v1[1] * v2[0]


def orient(v1: Tuple[int, int], v2: Tuple[int, int]):
    return sgn(cross_product(v1, v2))


def point_orient(p1, p2, p3):
    v1 = (p1[0] - p2[0], p1[1] - p2[1])
    v2 = (p3[0] - p2[0], p3[1] - p2[1])

    return orient(v1, v2)


if __name__ == '__main__':
    print(orient((1, 1), (0, 1)))
    print(orient((0, 1), (1, 1)))
    print(orient((1, 1), (1, 1)))


