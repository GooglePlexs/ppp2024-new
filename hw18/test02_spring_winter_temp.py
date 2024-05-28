import csv
import matplotlib.pyplot as plt

def main():
    f = open('hw18/weather_date.csv')
    data = csv.reader(f)

    next(data)
    winter = []
    summer = []
    
    
    for row in data :
        month = row[0].split('-')[1]

    if row[-1] != '' :
            
            if month == '12' :
                winter.append(float(row[-1]))
            if month == '01' :
                winter.append(float(row[-1]))
            if month == '02' :
                winter.append(float(row[-1]))

            if month == '07' :
                summer.append(float(row[-1]))
            if month == '08' :
                summer.append(float(row[-1]))
            if month == '09' :
                summer.append(float(row[-1]))
                
                
    plt.rc('font', family='NanumBarunGothic') 
    plt.rcParams['axes.unicode_minus'] = False

    plt.title('겨울철과 여름철의 기온차 분포도')  

    plt.hist(summer, bins=100, color='r', label='여름철')
    plt.hist(winter, bins=100, color='b', label='겨울철')
    plt.legend()

    plt.savefig("./spring_winter_temp.png")

if __name__ == "__main__":
    main()
