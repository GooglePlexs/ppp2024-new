import tkinter as tk
from tkinter import *


def convert_to_gram():
    kg_value = float(kg_entry.get())
    gram_value = kg_value * 1000
    result_label.config(text=f"변환된 단위는 {gram_value:.2f} gram입니다.")

def convert_to_ounce():
    kg_value = float(kg_entry.get())
    ounce_value = kg_value * 35.274
    result_label.config(text=f"변환된 단위는 {ounce_value:.2f} ounces 입니다.")

def convert_to_pound():
    kg_value = float(kg_entry.get())
    pound_value = kg_value * 2.20462
    result_label.config(text=f"변환된 단위는 {pound_value:.2f} pounds 입니다.")


def main():
    window = Tk()
    window.title("무게 변환기")
    window.geometry("400x200")

    Label(window, text="SI단위 변환기(kg단위)", font=("Arial", 14)).pack()
    global kg_entry  
    kg_entry = Entry(window)
    kg_entry.pack()

    Button(window, text="Convert to Gram", bg="red", command=convert_to_gram).pack()
    Button(window, text="Convert to Ounce", bg="yellow", command=convert_to_ounce).pack()
    Button(window, text="Convert to Pound", bg="white", command=convert_to_pound).pack()

    global result_label  
    result_label = Label(window, font=("NanumBarunGothic", 12))
    result_label.pack()

    window.mainloop()

if __name__ == "__main__":
    main()