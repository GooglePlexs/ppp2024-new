import sys
if "./" not in sys.path: 
  sys.path.append("./")

from lec09 import hw_submission

def read_col(filename, col_idx):

  results = []
  with open(filename) as f:
    lines = f.readlines()
    for line in lines[1:]:
      tokens = line.split(",")
      results.append(float(tokens[col_idx]))
  return results

def max_temp_diff(filename):

    max_temp_diff = {}

    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            year = int(tokens[0])
            tmax = float(tokens[3])
            tmin = float(tokens[5])
            daily_temp_diff = tmax - tmin

            if year not in max_temp_diff or daily_temp_diff > max_temp_diff[year][0]:
               max_temp_diff[year] = (daily_temp_diff, f"{year}-{int(tokens[1]):02d}-{int(tokens[2]):02d}")

    return max_temp_diff


def cal_temps(filename):
    cal_temp = {}  

    with open(filename) as f:
         lines = f.readlines()
         for line in lines[1:]:
            tokens = line.split(",")
            year = int(tokens[0])
            month = int(tokens[1])
            tavg = float(tokens[4])  # Assuming average temperature (you can adjust this based on your data)

            if 5 <= month <= 9:  # Consider only May to September
                if year in cal_temp:
                    cal_temp[year] += tavg
                else:
                    cal_temp[year] = tavg

    return cal_temp


def main():

    filename = "hw13/weather_146_2022.csv"
    
    tavg_year = read_col("hw13/weather_146_2022.csv", 4)
    rainfall = read_col("hw13/weather_146_2022.csv", 9)

    temp_max = max()

    # 1번 최대일교차
    for year, (max_diff, date) in max_temp_diffs_years.items():
        print(f"{year}년의 최대일교차가 발생한 날짜는 {date}이며 {max_diff:.1f}°C 입니다")
    
    # 2번 5월부터 9월까지의 적산온도
    for year, temp in sorted(accumulated_temps.items()):
        print(f"{year}년의 5월부터 9월까지의 적산온도는 {temp:.1f}°C 입니다.")

    hw_submission.submit("홍길동", rain_max, rain_max_date, tdiff_max, tdiff_max_date)


if __name__ == '__main__':
    main()