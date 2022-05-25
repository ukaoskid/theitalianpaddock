import fastf1
from f1_types import DataRequest, F1Repository


def get_session(request: DataRequest) -> F1Repository:
    f1_repository = F1Repository([], [], [], [])

    fastf1.Cache.enable_cache('cache')

    data = fastf1.get_session(request.year, request.track, request.session)
    data.load()

    # Laps
    for driver in request.drivers:
        f1_repository.laps.append(data.laps.pick_driver(driver))
        f1_repository.fastest_laps.append(f1_repository.laps[len(f1_repository.laps) - 1].pick_fastest())

    # Telemetry
    for lap in f1_repository.laps:
        f1_repository.laps_telemetry.append(lap.get_telemetry().add_distance())
    for fastest_lap in f1_repository.fastest_laps:
        f1_repository.fastest_laps_telemetry.append(fastest_lap.get_telemetry().add_distance())

    return f1_repository
