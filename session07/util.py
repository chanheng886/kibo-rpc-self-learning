import math

def eucildean(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]

    return math.sqrt(dx**2 + dy**2 + dz**2)