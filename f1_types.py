class DataRequest:
    def __init__(self, year, track, session, drivers, metrics):
        self.year = year
        self.track = track
        self.session = session
        self.drivers = drivers
        self.metrics = metrics


class F1Repository:
    def __init__(self, laps, laps_telemetry, fastest_laps, fastest_laps_telemetry):
        self.laps = laps
        self.laps_telemetry = laps_telemetry
        self.fastest_laps = fastest_laps
        self.fastest_laps_telemetry = fastest_laps_telemetry
