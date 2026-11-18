import math

class RobotState:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]

    def distance_to(self, target_pos):
        dx = target_pos[0] - self.pos[0]
        dy = target_pos[1] - self.pos[1]
        dz = target_pos[2] - self.pos[2]
        return math.sqrt(dx**2 + dy**2 + dz**2)

bot = RobotState(10.5, -4.0, 5.0)
dist = bot.distance_to([11.2, -3.8, 4.8])
print(f"Distance to target: {dist:.3f} m")