import random

def random_function():

    problem_number = 5  
    end_range_number = 9
    point = 0

    for i in range(problem_number):
        while True:
            x = random.randint(1, end_range_number)
            y = random.randint(1, end_range_number)
            if x * y != 0:
                break

        print(f"{x} x {y} = ?")
        answer = int(input())

        # 정답 체크 및 point 계산
        if answer == x * y:
            print("정답입니다!")
            point += 1
        else:
            print(f"오답입니다. 정답은 {x * y}입니다.")

    return problem_number, point

def main():

    problem_number, point = random_function()

    print("\n===구구단 문제 풀이 결과====")
    print(f"문제 개수: {problem_number}")
    print(f"정답 개수: {point}")
    print(f"point: {point * 100 / problem_number:.2f}%")

if __name__ == "__main__":
    main()
