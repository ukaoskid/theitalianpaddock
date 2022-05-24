import sys
import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

import numpy as np
import pandas as pd

ff1.Cache.enable_cache('../cache')  # replace with your cache directory

year, grand_prix, session = 2022, 6, 'Q'

quali = ff1.get_session(year, grand_prix, session)
quali.load() # This is new with Fastf1 v.2.2

# This is how it used to be:
# laps = quali.load_laps(with_telemetry=True)

driver_1, driver_2, driver_3 = 'LEC', 'VER', 'SAI'

# Laps can now be accessed through the .laps object coming from the session
laps_driver_1 = quali.laps.pick_driver(driver_1)
laps_driver_2 = quali.laps.pick_driver(driver_2)
laps_driver_3 = quali.laps.pick_driver(driver_3)

# Select the fastest lap
fastest_driver_1 = laps_driver_1.pick_fastest()
fastest_driver_2 = laps_driver_2.pick_fastest()
fastest_driver_3 = laps_driver_3.pick_fastest()

# Retrieve the telemetry and add the distance column
telemetry_driver_1 = fastest_driver_1.get_telemetry().add_distance()
telemetry_driver_2 = fastest_driver_2.get_telemetry().add_distance()
telemetry_driver_3 = fastest_driver_3.get_telemetry().add_distance()

# Make sure whe know the team name for coloring
team_driver_1 = fastest_driver_1['Team']
team_driver_2 = fastest_driver_2['Team']
team_driver_3 = fastest_driver_3['Team']

color_1 = '#cc0000'
color_2 = '#0034cc'
color_3 = '#00cc48'

# Extract the delta time
delta_time_1, ref_tel_1, compare_tel_1 = utils.delta_time(fastest_driver_1, fastest_driver_2)
delta_time_2, ref_tel_2, compare_tel_2 = utils.delta_time(fastest_driver_2, fastest_driver_3)

plot_size = [15, 15]
plot_title = f"{quali.event.year} {quali.event.EventName} - {quali.name} - {driver_1} VS {driver_2} VS {driver_3}"
plot_ratios = [1, 1, 5, 3, 3, 2] # [1, 3, 2, 1, 1, 2, 1]
plot_filename = plot_title.replace(" ", "") + ".png"

# Make plot a bit bigger
plt.rcParams['figure.figsize'] = plot_size

# Create subplots with different sizes
fig, ax = plt.subplots(6, gridspec_kw={'height_ratios': plot_ratios}) # previously 7

# Set the plot title
ax[0].title.set_text(plot_title)

# Delta line 1 vs 2
ax[0].plot(ref_tel_1['Distance'], delta_time_1)
ax[0].axhline(0)
ax[0].set(ylabel=f"1 VS 2 (s)")

# Delta line 2 vs 3
ax[1].plot(ref_tel_2['Distance'], delta_time_2)
ax[1].axhline(0)
ax[1].set(ylabel=f"2 VS 3 (s)")

# Speed trace
ax[2].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Speed'], label=driver_1, color=color_1)
ax[2].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Speed'], label=driver_2, color=color_2)
ax[2].plot(telemetry_driver_3['Distance'], telemetry_driver_3['Speed'], label=driver_3, color=color_3)
ax[2].set(ylabel='Speed')
ax[2].legend(loc="lower right")

# Throttle trace
ax[3].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Throttle'], label=driver_1, color=color_1)
ax[3].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Throttle'], label=driver_2, color=color_2)
ax[3].plot(telemetry_driver_3['Distance'], telemetry_driver_3['Throttle'], label=driver_3, color=color_3)
ax[3].set(ylabel='Throttle')

# Brake trace
ax[4].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Brake'], label=driver_1, color=color_1)
ax[4].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Brake'], label=driver_2, color=color_2)
ax[4].plot(telemetry_driver_3['Distance'], telemetry_driver_3['Brake'], label=driver_3, color=color_3)
ax[4].set(ylabel='Brake')

# # Gear trace
# ax[4].plot(telemetry_driver_1['Distance'], telemetry_driver_1['nGear'], label=driver_1, color=color_1)
# ax[4].plot(telemetry_driver_2['Distance'], telemetry_driver_2['nGear'], label=driver_2, color=color_2)
# ax[4].plot(telemetry_driver_3['Distance'], telemetry_driver_3['nGear'], label=driver_3, color=color_3)
# ax[4].set(ylabel='Gear')

# RPM trace
ax[5].plot(telemetry_driver_1['Distance'], telemetry_driver_1['RPM'], label=driver_1, color=color_1)
ax[5].plot(telemetry_driver_2['Distance'], telemetry_driver_2['RPM'], label=driver_2, color=color_2)
ax[5].plot(telemetry_driver_3['Distance'], telemetry_driver_3['RPM'], label=driver_3, color=color_3)
ax[5].set(ylabel='RPM')

# # DRS trace
# ax[6].plot(telemetry_driver_1['Distance'], telemetry_driver_1['DRS'], label=driver_1, color=color_1)
# ax[6].plot(telemetry_driver_2['Distance'], telemetry_driver_2['DRS'], label=driver_2, color=color_2)
# ax[6].plot(telemetry_driver_3['Distance'], telemetry_driver_3['DRS'], label=driver_3, color=color_3)
# ax[6].set(ylabel='DRS')
# ax[6].set(xlabel='Lap distance (meters)')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for a in ax.flat:
    a.label_outer()
    
# Store figure
plt.savefig(plot_filename, dpi=300)
plt.show()
