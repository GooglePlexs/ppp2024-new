class Cake:

    coat = '생크림'
    
    def __init__(self, topping, price, candles=0): 

        self.topping = topping   # 케익에 올린 토핑
        self.price = price      # 케익의 가격
        self.candles = candles  # 케익에 꽂은 초 개수
        
    def describe(self):

        print(f"이 케이크는 {self.coat}으로 덮여 있다.")
        print(f"이 케이크의 토핑은 {self.topping}을 올려 장식했다.")
        print(f"이 케이크의 가격은 {self.price:,d}원이다.")

        if self.candles > 0:
            print(f"이 케이크는 초가 {self.candles}개 포함되어 있다.")


def main(): 

    #cake_truck = []

    #cake_truck.append(Cake('눈사람 사탕', 10000))
    #cake_truck.append(Cake('한라봉', 9000, 8))

    #for cake in cake_truck:
    #    print(cake) # - 전체
    #    print(cake.price) # - 일부 출력
    #    cake.describe()

    cake_1 = Cake('눈사람 사탕', 10000) 
    cake_2 = Cake('한라봉', 9000, 8)

    print('케이크 1:') 
    cake_1.describe()

    print('케이크 2:') 
    cake_2.describe()


if __name__ == "__main__":
    main()