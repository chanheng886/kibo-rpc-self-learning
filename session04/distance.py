import math
# calculate distance
# from curent position -> checkpoint position
# d = √( (x₂ - x₁)² + (y₂ - y₁)² + (z₂ - z₁)² )

def calculate_3d_distance(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p2[2]
    return math.sqrt(dx**2 + dy**2 + dz**2)

current_position = [0.0, 0.0, 0.0]
checkpoint_position = [10.4, -5.2, 1.8]

result =  calculate_3d_distance(current_position, checkpoint_position)
print(f"Distance from the current position to the checkpoint position is:\n {result:.2f} meters")