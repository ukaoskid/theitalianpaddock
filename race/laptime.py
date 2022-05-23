import fastf1
from fastf1 import plotting
from matplotlib import pyplot as plt

fastf1.Cache.enable_cache('../cache')  # replace with your cache directory

plotting.setup_mpl()

race = fastf1.get_session(2022, 'Spanish Grand Prix', 'R')
race.load()

lec = race.laps.pick_driver('SAI')
ham = race.laps.pick_driver('PER')

fig, ax = plt.subplots()
ax.plot(lec['LapNumber'], lec['LapTime'], color='red')
ax.plot(ham['LapNumber'], ham['LapTime'], color='cyan')
ax.set_title("Sainz vs Perez")
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time")
plt.show()