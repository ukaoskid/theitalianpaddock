from f1_types import F1Repository
from constants import CHARTS, COLORS
from normalizers import normalize


def fastest_laps(drivers: list[str], data: F1Repository):
    chart = {"chart": CHARTS['Q_FASTLAPS'], "data": []}
    lengths = []
    for i in range(len(drivers)):
        chart_data = []
        for j in range(len(data.fastest_laps_telemetry[i])):
            chart_data.append({
                "speed": int(data.fastest_laps_telemetry[i].iloc[j]['Speed']),
                "distance": round(int(data.fastest_laps_telemetry[i].iloc[j]['Distance']))
            })
        # normalize distance
        normalized_data = normalize(chart_data, 'distance')
        chart['data'].append({"driver": drivers[i], "color": COLORS[i], "data": normalized_data})
        lengths.append(len(normalized_data))

    # align lengths
    shortest = min(lengths)
    for i in range(len(chart['data'])):
        if len(chart['data'][i]['data']) > shortest:
            chart['data'][i]['data'] = chart['data'][i]['data'][:len(chart['data'][i]['data']) - (len(chart['data'][i]['data']) - shortest)]

    return chart
