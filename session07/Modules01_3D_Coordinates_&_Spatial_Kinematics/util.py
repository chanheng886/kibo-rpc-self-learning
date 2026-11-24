import numpy as np

def calculate(current, target, v_target = 0.15):
    curr = np.array(current, dtype=float)
    targ = np.array(target, dtype=float)
    delta_r = targ - curr
    distance = float(np.linalg.norm(delta_r))

    est_time = distance / v_target

    return distance, np.round(delta_r, 2).tolist(), est_time

docking_position = [10.2, -4.0, 4.8]
target_position = [11.4, -3.5, 5.3]
distance, delta_r, est_time = calculate(docking_position, target_position)
print(f"Distance: {distance:.2f} m")
print(f"Delta R: {delta_r}")
print(f"Time that that robot will arrived: {est_time:.2f} s")