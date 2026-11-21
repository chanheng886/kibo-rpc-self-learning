class Waypoint:
    def __init__(self, point_id, coords):
        self.id = point_id
        self.coords = coords

    def __str__(self):
        return f"[CP # {self.id:02f}] @ X = {self.coords[0]:.2f}, Y = {self.coords[1]:.2f}, X = {self.coords[2]:.2f}"

wp = Waypoint(3, [10.12, -3.96, 4.80])
print(wp)
        