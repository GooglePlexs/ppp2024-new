import matplotlib.pyplot as plt
import numpy as np

def main():

    np.random.seed(0) # 랜덤이지만 랜덤 형태를 고정

    n = 50

    x = np.random.rand(n)
    y = np.random.rand(n)

    plt.scatter(x, y)
    plt.savefig("./scatter.png")

if __name__ == "__main__":
    main()