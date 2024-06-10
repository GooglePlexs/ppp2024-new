import pandas as pd

def main():
    df = pd.read.csv("./hw12/weather(146)_2001-2022.csv")

    print(df[df['month'] == 8]["tavg"].mean())
    ax = df[df['rainfall'] > 10]["rainfall"].plot.bar()
    ax.figure.savefig("pandas_tavg.png")

if __name__ == "__main__":
    main()