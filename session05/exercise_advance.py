from dataclasses import dataclass

@dataclass
class IntBallPose:
    #Position
    x: float
    y: float
    z: float

    #Orientation
    qx: float
    qy: float
    qz: float
    qw: float

    def __str__(self):
        return (
            "Position:\n"
            f"X = {self.x:.2f}\n"
            f"Y = {self.y:.2f}\n"
            f"Z = {self.z:.2f}\n"

            "Orientation:\n"
            f"OX = {self.qx}\n"
            f"OY = {self.qy}\n"
            f"OZ = {self.qz}\n"
            f"OW = {self.qw}\n"
        )
    def is_valid(self):
        return (
            9.50 <= self.x <= 11.50 and -5.00 <= self.y <= -3.00 and 4.20 <= self.z <= 5.80
        )

poses = [
    IntBallPose(10.50, -4.00, 5.00, 0.0, 0.0, 0.0, 1.0),
    IntBallPose(9.80, -3.50, 4.50, 0.0, 0.0, 0.0, 1.0),
    IntBallPose(12.00, -4.00, 5.00, 0.0, 0.0, 0.0, 1.0)
]

for index, pose in enumerate(poses, start=1):
    print(f"No {index} {pose} {pose.is_valid()}")

        