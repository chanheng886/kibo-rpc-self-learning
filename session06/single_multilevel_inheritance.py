
# Advanced Code
from dataclasses import dataclass
@dataclass
class SpaceHardware:
    name: str
    is_powered: bool = True

class Sensor(SpaceHardware):
    def read_raw(self):
        return 0.0

class Navigationcamera(Sensor):
    def capture_frame(self):
        print(f"{self.name}: Grabbing 1280 x 960 optical frame.")

cam = Navigationcamera("Front_Camera")
print(cam.is_powered)
cam.capture_frame()

#Beginner Friendly Code
class SpaceHardware2:
    def __init__(self, name):
        self.name = name
        self.is_powered = True
class Sensor2(SpaceHardware2):
    def read_raw(self):
        return 0.0

class NavigationCamera(Sensor2):
    def capture_frame(self):
        print(f"{self.name}: Grabbing 1280 x 960 optical frame.")

cam2 = Navigationcamera("Back Camera")
print(cam2.is_powered)
cam2.capture_frame()
        