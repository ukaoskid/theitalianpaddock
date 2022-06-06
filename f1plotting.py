from constants import COLORS

from fastf1 import utils
from fastf1 import plotting

from matplotlib import pyplot as plt


def plot_quali(drivers, event, fastest_laps, fastest_laps_telemetry, metrics):
    # 1 = delta time, 2 = ref telemetry
    delta_times = []
    real_len = len(fastest_laps) - 1

    # Event name
    event_name = f"{event.year} {event.EventName} - Qualification - {', '.join(drivers)}"

    # Delta times
    for i in range(len(fastest_laps)):
        next_lap = i + 1
        if next_lap <= real_len:
            delta_times.append(utils.delta_time(fastest_laps[i], fastest_laps[next_lap]))

    plot_counter = 0
    plot_size = [14 + len(delta_times) + len(metrics), 14 + len(delta_times) + len(metrics)]
    plot_ratios = []
    for i in range(len(delta_times)):
        plot_ratios.append(1)
    for i in range(len(metrics)):
        plot_ratios.append(5)

    plot_filename = event_name.replace(" ", "") + ".png"

    # Make plot a bit bigger
    plt.rcParams['figure.figsize'] = plot_size

    # Create subplots with different sizes
    fig, ax = plt.subplots(len(plot_ratios), gridspec_kw={'height_ratios': plot_ratios})

    ax[plot_counter].title.set_text(event_name)

    for delta_time in delta_times:
        ax[plot_counter].plot(delta_time[1]['Distance'], delta_time[0])
        ax[plot_counter].axhline(0)
        # ax[plot_counter].set(ylabel=f"1 VS 2 (s)")
        plot_counter = plot_counter + 1

    # Speed trace
    for metric in metrics:
        for i in range(len(fastest_laps_telemetry)):
            ax[plot_counter].plot(fastest_laps_telemetry[i]['Distance'], fastest_laps_telemetry[i][metric],
                                  label=drivers[i], color=COLORS[i])
            ax[plot_counter].set(ylabel=metric)
            ax[plot_counter].legend(loc="lower right")
        plot_counter = plot_counter + 1

    for a in ax.flat:
        a.label_outer()

    # Store figure
    plt.savefig(plot_filename, dpi=600)


def plot_race(drivers, event, laps, session_name):
    # Event name
    plotting.setup_mpl()

    event_name = f"{event.year} {event.EventName} - {session_name} - {', '.join(drivers)}"
    plot_filename = event_name.replace(" ", "") + ".png"

    fig, ax = plt.subplots()
    ax.set_title(event_name)
    ax.set_xlabel("Lap Number")
    ax.set_ylabel("Lap Time")

    for i in range(len(drivers)):
        ax.plot(laps[i]['LapNumber'], laps[i]['LapTime'], color=COLORS[i])

    # Store figure
    plt.savefig(plot_filename, dpi=600)
