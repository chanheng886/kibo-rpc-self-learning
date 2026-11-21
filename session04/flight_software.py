import json

with open("config.json", "r") as file:
    data = json.load(file)
    target = data["targets"]
    loaded_count = len(target)
    print(f"Loaded {loaded_count} targets")