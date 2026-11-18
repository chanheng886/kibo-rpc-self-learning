class SafetyMonitor:
    def __init__(self):
        self.__battery = 100

    def update_battery(self, val):
        # this mean between
        if 0.0 <= val <= 100.0:
            self.__battery = val
        else:
            print("[ERROR] Invalid battery telemetry")

    def get_battery(self):
        return self.__battery

battery = SafetyMonitor()
battery.update_battery(50)
print(f"Your robot's battery is: {battery.get_battery()}")
# print(battery.get_battery())