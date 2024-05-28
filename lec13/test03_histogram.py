import matplotlib.pyplot as plt
import numpy as np

def main():
    
    dices = np.random.randint(1, 7, size=100000000) # random 모듈과 다름
    
    # print(dices) - 터미널 출력해 확인용
    
    plt.hist(dices, bins=6, color="b") # bin = 통 개수, b = 블루 / k = 블랙 
    # plt.show()
    plt.savefig("./line_histogram.png")

if __name__ == "__main__":
    main()