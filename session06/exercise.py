# import math
# class BasePoint:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def distance_to(self, other_point):
#         if isinstance(other_point, BasePoint):
#             ox, oy, oz = other_point.x, other_point.y, other_point.z
#         else:
#             ox, oy, oz = other_point

#         dx = ox - other_point.x
#         dy = oy - other_point.y
#         dz = oz - other_point.z
#         return math.sqrt(dx**2 + dy**2 + dz**2)

# class CheckPoint(BasePoint):
#     def __init__(self, x, y, z, marker_id):
#         super().__init__(x, y, z)
#         self.id = marker_id
#         self.visted = False

import math

class BasePoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other_point):
        if isinstance(other_point, BasePoint):
            ox, oy, oz = other_point.x, other_point.y, other_point.z
        else:
            ox, oy, oz = other_point
        dx = ox - other_point.x
        dy = oy - other_point.y
        dz = oz - other_point.z

        return math.sqrt(dx**2 + dy**2 + dz**2)

class CheckPoint(BasePoint):
    def __init__(self, x, y, z, marker_id):
        super().__init__(x, y, z)
        self.id = marker_id
        self.visited = False



    
