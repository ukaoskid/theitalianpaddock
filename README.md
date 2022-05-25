# F1 Data
Using FastF1

# How to use

## Available metrics
- Speed
- Throttle
- Brake
- nGear
- RPM
- DRS

## Qualifying
```bash
python3 f1ex [YEAR] [ROUND] Q 3 [DRIVER 3 letter comma separated no spaces] [METRICS comma separated no spaces]

# 2022 Spanish GP
python3 f1ex.py 2022 6 Q LEC,VER,SAI Speed,Throttle,Brake,nGear,RPM,DRS
```

## Race
```bash
python3 f1ex [YEAR] [ROUND] R 3 [DRIVER 3 letter comma separated no space]

# 2022 Spanish GP
python3 f1ex.py 2022 6 R LEC,VER,SAI
```