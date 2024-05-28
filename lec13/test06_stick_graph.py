import matplotlib.pyplot as plt
import numpy as np

def main():

    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False
    
    fig, ax = plt.subplots(figsize=(15, 6))

    year = [str(x+2001) for x in range(20)]
    rain = np.random.rand(20) * 200 + 1000

    ax.bar(year, rain, color="b")

    ax.set_ylabel("연평균강우량(mm)")
    
    fig.savefig("./bar_rain.png")

if __name__ == "__main__":
    main()