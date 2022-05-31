from f1_types import F1Repository
from constants import CHARTS, COLORS


def fastest_laps(drivers: list[str], data: F1Repository):
    chart = {"chart": CHARTS['Q_FASTLAPS'], "data": []}
    for i in range(len(drivers)):
        chart_data = []
        for j in range(len(data.fastest_laps_telemetry[i])):
            chart_data.append({
                "speed": int(data.fastest_laps_telemetry[i].iloc[j]['Speed']),
                "distance": round(int(data.fastest_laps_telemetry[i].iloc[j]['Distance']))
            })
        chart['data'].append({"driver": drivers[i], "color": COLORS[i], "data": chart_data})

    return chart
