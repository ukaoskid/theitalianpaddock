import sys
import f1plotting
import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

import numpy as np
import pandas as pd

year = int(sys.argv[1])
track = int(sys.argv[2])
session = sys.argv[3]
drivers = sys.argv[4].split(",")
metrics = sys.argv[5].split(",") # Speed, Throttle, Brake, nGear, RPM, DRS

laps = []
laps_telemetry = []
fastest_laps = []
fastest_laps_telemetry = []

ff1.Cache.enable_cache('cache')

data = ff1.get_session(year, track, session)
data.load()

# Laps
for driver in drivers:
    laps.append(data.laps.pick_driver(driver))
    fastest_laps.append(laps[len(laps) - 1].pick_fastest())

# Telemetry
for lap in laps:
    laps_telemetry.append(lap.get_telemetry().add_distance())
for fastest_lap in fastest_laps:
    fastest_laps_telemetry.append(fastest_lap.get_telemetry().add_distance())

if session == "Q":
    f1plotting.plot_quali(
        drivers,
        event=data.event,
        fastest_laps=fastest_laps,
        fastest_laps_telemetry=fastest_laps_telemetry,
        metrics=metrics)
else:
    f1plotting.plot_race(drivers, event=data.event, laps=laps)
