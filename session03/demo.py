# Autonomous Decision Logic
print("<=====Autonomous Decision Logic=====>")
battery_level = 18.2 # Percentage
time_remaining = 24.5 # Seconds
dist_to_goal = 1.1 # Meters

if time_remaining < 30.0:
    print("[CRITICAL] Low time remaining -> Abort to Goal Checkpoint!")
elif time_remaining < 20.0:
    print("[WARNING] Low battery -> Transition to conservation velocity.")
else:
    print("[NOMINAL] Proceed to next inspection checkpoint")

# Interating Through Target Queues
print("<=====Interating Through Target Queues=====>")
checkpoints = [1, 2, 4, 7, 9]
for cp_id in checkpoints:
    print(f"[NAV] Computing trajectory to Checkpoint {cp_id}...")
    print(f"[NAV] Checkpoint {cp_id} reached successfully")

# Waiting for Spacecraft Stabilizatoin
print("<=====Waiting for Spacecraft Stabilizatoin=====>")
import time
is_steady = False
setter_counter = 0

while not is_steady:
    print("Reading IMU...Robot is stabilizing in microgravity")
    time.sleep(2)
    setter_counter += 1
    if setter_counter >= 4:
        is_steady = True
        print("[STABILIZED] Ready to trigger AR camera capture.")