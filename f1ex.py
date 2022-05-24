import sys
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
metrics = sys.argv[5].split(",")

laps = []
fastest_laps = []
telemetry = []

ff1.Cache.enable_cache('cache')

data = ff1.get_session(year, track, session)
data.load()

# Laps, Telemetry
for driver in drivers:
    laps.append(data.laps.pick_driver(driver))
    telemetry.append(laps[len(laps)].pick_fastest())

# Extract the delta time
delta_time_1, ref_tel_1, compare_tel_1 = utils.delta_time(drivers[0], drivers[1])
delta_time_2, ref_tel_2, compare_tel_2 = utils.delta_time(drivers[2], drivers[3])

print(delta_time_1)