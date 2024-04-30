import csv
f = open('lec09/jeonju_weather.csv')
data=csv.reader(f)
header=next(data)
max_temps = -999
min_temps = ''
day_temps = -999
max_dates = ''
day_dates = ''
for row in data :
    if row[2] == '':
      row[2] = 0
    if row[3] == '':
      row[3] = 0
    if row[4] == '':
      row[4] = -999

    row[2] = float(row[2])
    row[3] = float(row[3])
    row[4] = float(row[4])

    if(row[4] - row[3]) > day_temps:
      day_temps = (row[4] - row[3])
      max_temps =row[4]
      min_temps =row[3]
      day_dates = row[0]

print('수원의 일교차가 가장 큰 날짜는',day_dates,'이고 최저 기온',min_temps,'최고 기온',max_temps,' 일교차는',day_temps,'도 입니다.')