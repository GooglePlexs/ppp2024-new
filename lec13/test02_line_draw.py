import matplotlib.pyplot as plt
import numpy as np # numpy를 np로 변환

def main():

    tmax = np.random.rand(30) * 15 + 15
    tmin = tmax - (np.random.rand(30) * 5 + 5)

    plt.plot(tmax, color="r", label="TMAX")
    plt.plot(tmin, color="b", label="TMIN")

    plt.ylabel("Temperature(℃)")

    plt.legend() # 색 이름부여
    # plt.show() - 로컬
    plt.savefig("./line_temp.png")

if __name__ == "__main__":
    main()