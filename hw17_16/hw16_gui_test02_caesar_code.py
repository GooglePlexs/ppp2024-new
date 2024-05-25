import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)


def toggle_text(text: str) -> str:
    result = ""

    for word in text:

        if word.isalpha():

            if 'A' <= word <= 'Z':
                result += chr(ord(word) + 32)  # 대문자 -> 소문자

            elif 'a' <= word <= 'z':
                result += chr(ord(word) - 32)  # 소문자 -> 대문자

            else:
                result += word

    return result


def main():
    input_text = input("대/소문자 변환이 필요한 영단어를 입력하시오 : ")
    print_text = toggle_text(input_text)
    print(print_text)


if __name__ == "__main__":
    main()