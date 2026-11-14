telemetry_line = "STATUS:OK|ID:04|MARGIN:LV3"
fields = telemetry_line.split("|")

status = fields[0].split(":")[1]
level = fields[2].split(":")[1]
id = fields[1].split(":")[0]

print(f"Flight status is {status}, achieved margin {level} and id is {id}")