class RobotState:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z
        self.is_steady = False

current_pose = RobotState(10.5, -4.0, 5.0)
target_pose = RobotState(11.2, -3.8, 4.8)
        
print(f"Current Position: {current_pose}")
print(f"Target Position: {target_pose}")