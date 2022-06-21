import tkinter as tk
from tkinter import messagebox


def input_form() -> dict:
    root = tk.Tk()
    root.title('Correct to 40 deg')
    root.geometry('300x200')

    tk.Label(root, text="Original IR").place(x=10, y=10)
    tk.Label(root, text="Temperature").place(x=10, y=40)

    et_ohm = tk.Entry(root)
    et_ohm.place(x=140, y=10)

    et_temp = tk.Entry(root)
    et_temp.place(x=140, y=40)

    return {
        "root": root,
        "et_ohm": et_ohm,
        "et_temp": et_temp
    }

def trans_40deg_Mohm(ori_Mohm: int, temp: int) -> float:
    correct_temp = 40
    return ori_Mohm * (0.5**((correct_temp-temp)/10))

if __name__ == "__main__":
    ori_Mohm = 627
    temp = 36

    print(trans_40deg_Mohm(ori_Mohm, temp))

    input_form()
