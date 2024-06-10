import numpy as np

def main():
    grade_total = [3.5, 4.5] # 지워지지 않는 데이터
    while True:
        grade = float(input("학점을 입력하세요"))
        if grade < 0:
            break
        grade_total.append(grade) # 실행 때 마다 달라지는 데이터 (삭제)
    print(f"현재까지의 학점 목록은 {grade_total}입니다.")
    print(f"평균 학점은 {np.average(grade_total):.2f}입니다.")


if __name__ == "__main__":
    main()