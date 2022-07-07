import sys
import f1plotting
import fastf1 as ff1

year = int(sys.argv[1])
track = int(sys.argv[2])
session = sys.argv[3]
drivers = sys.argv[4].split(",")
metrics = sys.argv[5].split(",")  # Speed, Throttle, Brake, nGear, RPM, DRS

laps = []
laps_telemetry = []
fastest_laps = []
fastest_laps_telemetry = []

ff1.Cache.enable_cache('cache')

data = ff1.get_session(year, track, "R")
data.load()

# Laps - considering only accurate data
for driver in drivers:
    current_laps = data.laps.pick_driver(driver)
    laps.append(current_laps)
    latest_laps = laps[len(laps) - 1]
    specific_lap = latest_laps[latest_laps['LapNumber'] == 39].iloc[0]
    fastest_laps.append(specific_lap)


# Telemetry
for lap in laps:
    laps_telemetry.append(lap.get_telemetry().add_distance())
for fastest_lap in fastest_laps:
    fastest_laps_telemetry.append(fastest_lap.get_telemetry().add_distance().add_differential_distance())

if session == "Q":
    f1plotting.plot_quali(
        drivers,
        event=data.event,
        fastest_laps=fastest_laps,
        fastest_laps_telemetry=fastest_laps_telemetry,
        metrics=metrics)
elif session == "FP1":
    f1plotting.plot_race(drivers, event=data.event, laps=laps, session_name="FP1")
elif session == "FP2":
    f1plotting.plot_race(drivers, event=data.event, laps=laps, session_name="FP2")
elif session == "FP3":
    f1plotting.plot_race(drivers, event=data.event, laps=laps, session_name="FP3")
else:
    f1plotting.plot_race(drivers, event=data.event, laps=laps, session_name="Race")
