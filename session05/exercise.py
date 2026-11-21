class IntBallPose:
    def __init__(self, x, y, z, qx, qy, qz, qw):
        #Position
        self.x = x
        self.y = y
        self.z = z

        #Orientation
        self.qx = qx
        self.qy = qy
        self.qz = qz
        self.qw = qw

    def __str__(self):
        return (
            "Robot Position:"
            f"X = {self.x:.2f}\n"
            f"Y = {self.y:.2f}\n"
            f"Z = {self.z:.2f}\n"

            "Robot Orientation: "
            f"QX = {self.qx:.2f}\n"
            f"QY = {self.qy:.2f}\n"
            f"QZ = {self.qz:.2f}\n"
            f"QW = {self.qw:.2f}\n"
        )

    def is_valid(self):
        x_valid = 9.50 <= self.x <= 11.50
        y_valid = -5.00 <= self.y <= -3.00
        z_valid = 4.20 <= self.z <= 5.80
        return x_valid and y_valid and z_valid


pose1 = IntBallPose(10.50, -4.00, 5.00, 0.0, 0.0, 0.0, 1.0)
pose2 = IntBallPose(9.80, -3.50, 4.50, 0.0, 0.0, 0.0, 1.0)
pose3 = IntBallPose(12.00, -4.00, 5.00, 0.0, 0.0, 0.0, 1.0)

poses = [pose1, pose2, pose3]

for idx, pos in enumerate(poses, start=1):
    print(f"\n\nNo.: {idx}, Pose: {pos}Valid: {pos.is_valid()}")