import csv
import matplotlib.pyplot as plt


f = open('hw18/weather_date.csv')
data = csv.reader(f)

next(data)
high = []
low = []
year =[]

for row in data :
    if row[-1] != '' and row[-2] != '':
        if 1981 <= int(row[0].split('-')[0]) : 
                if row[0].split('-')[1] == '05' and row[0].split('-')[2] == '30':
                    high.append(float(row[-2]))
                    low.append(float(row[-1]))
                    year.append(int(row[0].split('-')[0]))

plt.rc('font', family='NanumBarunGothic') 
plt.title('생일 기온 변화 그래프')    

plt.plot(year, high, 'r', label='최고')
plt.plot(year, low, 'b', label='최저')
plt.legend()


plt.savefig("./birth_temp.png")
