from f1_types import F1Repository
from constants import CHARTS, COLORS
from normalizers import normalize


def fastest_laps(drivers: list[str], metrics: list[str], data: F1Repository):
    chart = {"chart": 'FASTLAPS', "data": []}
    lengths = []
    for i in range(len(drivers)):
        chart_data = []
        for j in range(len(data.fastest_laps_telemetry[i])):
            telemetry_metric = {}
            for metric in metrics:
                telemetry_metric[metric.lower()] = int(data.fastest_laps_telemetry[i].iloc[j][metric])
            telemetry_metric['distance'] = round(int(data.fastest_laps_telemetry[i].iloc[j]['Distance']))
            chart_data.append(telemetry_metric)

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


def laps(drivers: list[str], data: F1Repository):
    chart = {"chart": 'LAPSTIME', "data": []}
    for i in range(len(drivers)):
        chart_data = []
        for j in range(len(data.laps[i])):
            print(data.laps[i].columns)
            chart_data.append({
                "time": int(data.laps[i].iloc[j]['LapTime'].total_seconds() * 1e3),
                "lap": round(int(data.laps[i].iloc[j]['LapNumber'])),
                "s1": int(data.laps[i].iloc[j]['Sector1Time'].total_seconds() * 1e3),
                "s2": int(data.laps[i].iloc[j]['Sector2Time'].total_seconds() * 1e3),
                "s3": int(data.laps[i].iloc[j]['Sector3Time'].total_seconds() * 1e3),
                "compound": str(data.laps[i].iloc[j]['Compound'])
            })
        chart['data'].append({"driver": drivers[i], "color": COLORS[i], "data": chart_data})

    return chart


def layout(drivers: list[str], data: F1Repository):
    chart = {"chart": 'LAYOUT', "data": []}
    for i in range(len(drivers)):
        chart_data = []
        for j in range(len(data.laps_telemetry[i])):
            # print(data.laps_telemetry[i].columns)
            chart_data.append({})
        chart['data'].append({"driver": drivers[i], "color": COLORS[i], "data": chart_data})

    return chart