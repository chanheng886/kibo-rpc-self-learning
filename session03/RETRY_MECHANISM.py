# Handling Vision Errors & Early Exits
MAX_RETRIES = 5
for attempt in range(1, MAX_RETRIES + 1):
    marker_found = detech_aruco_marker()
    if marker_found:
        print(f"Marker identified on attempt {attempt}!")
        break
    else:
        print(f"Attempt {attempt} failed. Nidging...")
        continue



# Simulated mockup function testing
def detech_aruco_marker():
    return True