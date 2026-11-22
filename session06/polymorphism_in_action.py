class BaseTarget:
    def process(self):
        pass

class CheckPointTarget(BaseTarget):
    def process(self):
        print("Decoded 4x4 ArUco Marker ID!")

class GoalTarget(BaseTarget):
    def process(self):
        print("Transimitted Mission Complete Report!")


mission_target = [CheckPointTarget(), CheckPointTarget(), GoalTarget()]

for target in mission_target:
    target.process()
    