import tkinter as tk
from tkinter import simpledialog, messagebox

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

def caesar_encode(text: str, shift: int = 3) -> str:
    input_text = ""

    for word in text:
        if word.isalpha():
            if word.isupper():
                lock_text = ord(word) + shift
                if lock_text > ord('Z'):
                    lock_text -= 26
            else:
                lock_text = ord(word) + shift
                if lock_text > ord('z'):
                    lock_text -= 26
            input_text += chr(lock_text)
        else:
            input_text += word

    return input_text

def caesar_decode(text: str, shift: int = 3) -> str:
    trans_shift = -shift
    return caesar_encode(text, trans_shift)

def encrypt_button_click():
    original_text = gui_input("암호화가 필요한 영단어를 입력하시오: ")
    if original_text:
        encoded_text = caesar_encode(original_text)
        messagebox.showinfo("암호화 결과", f"암호화된 텍스트: {encoded_text}")

def decrypt_button_click():
    encoded_text = gui_input("복호화가 필요한 영단어를 입력하시오: ")
    if encoded_text:
        decoded_text = caesar_decode(encoded_text)
        messagebox.showinfo("복호화 결과", f"복호화된 텍스트: {decoded_text}")

def main():
    window = tk.Tk()
    window.title("카이사르 코드 변환기")
    window.geometry("200x100")

    encrypt_button = tk.Button(window, text="암호화", command=encrypt_button_click)
    encrypt_button.pack()

    decrypt_button = tk.Button(window, text="복호화", command=decrypt_button_click)
    decrypt_button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()