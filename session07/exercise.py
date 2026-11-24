import numpy as np

def calculate_distance(current_position, target_position, v_target = 0.55):
    curr = np.array(current_position, dtype=float)
    targ = np.array(target_position, dtype=float)
    delta_r = targ - curr
    distance = float(np.linalg.norm(delta_r))   

    est_time = distance / v_target if v_target > 0 else print("Inf")

    return delta_r, curr, targ, distance, est_time, v_target
    
docking_station = [0.152, 1.22, 2.01]
target_position = [-0.552, 1.223, -3.225]

delta_r, curr, targ, distance, est_time, v_target= calculate_distance(docking_station, target_position)
status = ""
arrival_tolerance = 0.05 #0.05m = 5cm

if distance <= arrival_tolerance:
    status = "[STATUS] Robot Arrivaled Successfully!"
else:
    status = "[STATUS] Robot Arrivaled Faild!"

print(f"""
        Docking Station: {curr}
        Target Position: {targ}
        Delta Value: {np.round(delta_r, 3).tolist()}
        Distance: {distance:.2f} m
        Speed: {v_target:.2f} m/s
        Arrival time: {est_time:.2f} s
        Status: {status}
    """)