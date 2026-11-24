import math

def eucildean(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]
    return math.sqrt(dx**2 + dy**2 + dz**2)

pos1 = [12, -8.4, 16]
pos2 = [11, -6.2, 12]
dis = eucildean(pos1, pos2)

v_target = 2.5
time = dis / v_target

print(f"Distance: {dis:.2f} m")
print(f"Estimated travel time at{v_target:.2f} m/s: {time:.2f} s")