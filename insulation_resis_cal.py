import tkinter as tk
from tkinter import messagebox


def input_form() -> dict:
    root = tk.Tk()
    root.title('Correct to 40 deg')
    root.geometry('300x200')

    tk.Label(root, text="Original IR(請輸入整數)").place(x=10, y=10)
    tk.Label(root, text="Temperature(請輸入整數)").place(x=10, y=40)

    et_ohm = tk.Entry(root)
    et_ohm.place(x=140, y=10)

    et_temp = tk.Entry(root)
    et_temp.place(x=140, y=40)

    def pop_calculate():
        ohm = et_ohm.get()
        temp = et_temp.get()

        try:
            ohm = int(ohm)
            temp = int(temp)

            messagebox.showinfo(title="Result", message=str(trans_40deg_Mohm(ohm, temp)))

        except Exception:
            messagebox.showerror(title="Input Error", message="Please input integer")

    tk.Button(root, text="計算", command=pop_calculate, height=3, width=13).place(x=10, y=100)

    return {
        "root": root
    }

def trans_40deg_Mohm(ori_Mohm: int, temp: int) -> float:
    correct_temp = 40
    return ori_Mohm * (0.5**((correct_temp-temp)/10))

if __name__ == "__main__":
    ori_Mohm = 627
    temp = 36

    print(trans_40deg_Mohm(ori_Mohm, temp))

    form_obj = input_form()
    form_obj["root"].mainloop()
