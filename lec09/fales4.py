def max_temp_high(filename):

    max_temp = -999
    max_date = ''

    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            year = int(tokens[0])
            tavg = float(tokens[2])
            tmin = float(tokens[3])
            tmax = float(tokens[4])
            

    fliename = 'lec09/jeonju_weather.csv'
    

    for line in lines :
       if line[-1] == '':
          line[-1] = -9999
    else:
        line[-1] = float(line[-1]) # 최고 기온을 실수로 변환
        
    if max_temp < line[-1]:
        max_date = line[0]
        max_temp = line[-1]
    f.close()
    
    

def max_temp_diff(filename):

    max_temp_diff = {}

    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            year = int(tokens[0])
            tavg = float(tokens[2])
            tmin = float(tokens[3])
            tmax = float(tokens[4])
            daily_temp_diff = tmax - tmin

            if year not in max_temp_diff or daily_temp_diff > max_temp_diff[year][0]:
               max_temp_diff[year] = (daily_temp_diff, f"{year}-{int(tokens[1]):02d}-{int(tokens[2]):02d}")

    return max_temp_diff
        
print(max_date, max_temp, max_temp_diff)

def max_temp_high(filename):

    



    max_temp = -999
    max_date = ''
    
    fliename = 'lec09/jeonju_weather.csv'
    
    with open(filename) as f:
        lines = f.readlines()
        
        for line in lines :
            if line[-1] == '':
                line[-1] = -9999
        else:
            line[-1] = float(line[-1]) # 최고 기온을 실수로 변환
        
    if max_temp < line[-1]:
        max_date = line[0]
        max_temp = line[-1]
