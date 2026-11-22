class Transceiver:
    def transmit(self, msg):
        print("Saving to share/logs: ", msg)

class LogWriter:
    def write_disk(self, log):
        print("Saving to share/logs: ", log)

class FlightComputer(Transceiver, LogWriter):
    pass

fc = FlightComputer()
fc.transmit("Nav Cam calibration complete.")
fc.write_disk("Status: Nominal, Battery: 98&")