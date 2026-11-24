import numpy as np

def compute_kinematics(r_current, r_target, v_target):
    curr = np.array(r_current, dtype=float)
    targ = np.array(r_target, dtype=float)

    delta_r = targ - curr

    distance = float(np.linalg.norm(delta_r))   

    est_time = distance / v_target if v_target > 0 else ("inf")

    arrive_tolerance = 0.05
    if distance <= arrive_tolerance:
        print("[STATUS] Arrived at checkpoint! Triggering ArUCO camera scan...")

    return print(f"Delta R: {delta_r}\nCurrent Position: {curr}\nTarget Position: {targ}\nDistance: {distance:.2f} m\nTime: {est_time:.2f} m/s")

curr = [0.0, -3.4, 0.0]
targ = [12.4, -7.8, 6.8]
speed = 4.5
compute_kinematics(curr, targ, speed)
    