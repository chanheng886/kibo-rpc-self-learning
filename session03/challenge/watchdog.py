import random
battery = 100.0

# Note: we check the lowest value first
# Why?
# Because if elif always stop at the first condition that is true
# If we check 80.0 first, imagine you robot reach 75.0 of battery, the condition will now check because 80.0 is already true
for i in range(0, 10):
    battery -=  random.uniform(1.5, 3.5)
    if battery < 75.0:
        print(f"[EMERGENCY RETURN TRIGGERED] Your battery is now lower than {battery}")
        break
    elif battery < 80.0:
        print(f"[CAUTION MESSAGE] Your battery is now lower than {battery}")
