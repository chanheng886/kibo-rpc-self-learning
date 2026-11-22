from dataclasses import dataclass, field

# Advanced Codes
@dataclass
class InspectionPoint:
    pt_id: str
    x: float
    y: float
    z: float
    pos: tuple[float, float, float] = field(init=False)

    def __post_init__(self) -> None:
        self.pos = (self.x, self.y, self.z)

@dataclass
class LeakCheckPoint(InspectionPoint):
    marker_id: int
    inspect: bool = False

check = LeakCheckPoint("CH_01", 10.5, -2.8, 4.3, marker_id=14)
print(f"Point {check.pt_id} at {check.pos} | Marker: {check.marker_id}")

# Beginner Friendly Code

class InspectionPoint2:
    def __init__(self, pt_id, x, y, z):
        self.id = pt_id
        self.pos = [x, y, z]

class LeakCheckPoint2(InspectionPoint2):
    def __init__(self, pt_id, x, y, z, expect_marker_id):
        super().__init__(pt_id, x, y, z)
        self.marker_id = expect_marker_id
        self.inspected = False

check2 = LeakCheckPoint2("CH_02", x=10.5, y=-2.8, z=4.3, expect_marker_id=15)
print(f"Point {check2.id} At {check2.pos} | Mark: {check2.marker_id}")
