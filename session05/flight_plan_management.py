class FlightPlan:
    def __init__(self):
        self.queue = []

    def add_poin(self, pt):
        self.queue.append(pt)

    def __len__(self):
        return len(self.queue)


plan = FlightPlan()
plan.add_poin([10.5, -4.0, 5.0])
print(f"Remaining Waypoints: {len(plan)} # Call __len__!")
