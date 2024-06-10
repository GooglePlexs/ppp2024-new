import numpy as np
import os
import pickle

# DB_FILE = "./grade_db.txt" 
# DB_FILE = "./grade_db.csv"
DB_FILE = "./grade_db.pkl"

def read_db(): # 입력받은 정보를 망각하지 않고 txt 형태로 저장

    grade_db = []

    if not os.path.exists(DB_FILE):
        return grade_db
    
    with open(DB_FILE) as f:
      # grade_db = [float(x) for x in f.readlines()] txt버전
        grade_db = pickle.load(f)
      # grade_db = [float(x) for x in f.readlines().split(",")] csv버전

    return grade_db


def write_db(grade_db):
    with open(DB_FILE,"wb") as fout:
        pickle.dump(grade_db,fout)
    # with open(DB_FILE,"w") as fout:

        # for x in grade_db: txt, csv버전
            # fout.write(f"{x}\n") txt버전
          # fout.write(",".join(map(str, grade_db))) csv버전


def main():

    # grade_total = [3.5, 4.5] 
    # grade_total = {"프원실": 4.5,"토양학": 4.0}

    grade_total = read_db()

    print(f"현재까지의 학점 목록은 {grade_total}입니다.")
    while True:
        grade = float(input("학점을 입력하세요"))
        if grade < 0:
            break
        # grade_total.append(grade) 과목명 없는 경우
        subject = input("과목명을 입력하세요")
        grade_total[subject] = grade

    print(f"현재까지의 학점 목록은 {grade_total}입니다.")
    # print(f"평균 학점은 {np.average(grade_total):.2f}입니다.")
    print(f"평균 학점은 {np.average(list(grade_total.values())):.2f}입니다.")

    write_db(grade_total)


if __name__ == "__main__":
    main()