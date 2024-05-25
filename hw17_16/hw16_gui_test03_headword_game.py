import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)


def get_chosung(text):
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    chosung = []

    for hangeul in text:
        chosung.append(CHOSUNG_LIST[(ord(hangeul) - ord('가')) // 588])

    return chosung


def main():

    hidden_answer = "스마트팜"
    lives = 5  # Initializing lives

    problem = get_chosung(hidden_answer)
    print(f"문제입니다. 주어진 초성은 '{''.join(problem)}'입니다.")

    while lives > 0:

        answer = input("답= ")

        if answer == hidden_answer:
            print(f"정답입니다!")
            break  # Exit the loop if the answer is correct

        lives -= 1  # Decrement lives on incorrect answer
        print(f"오답입니다. 남은 목숨은 {lives}개입니다.")

        if lives == 0:
            print("게임 오버!")
            break


if __name__ == "__main__":
    main()