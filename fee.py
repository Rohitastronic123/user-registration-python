import tkinter as tk
from tkinter import ttk, messagebox


def pay():
  if (En_fee1.get() >= "2000"):
    messagebox.showinfo("Success", "Registration Successfully", parent=root)
    root.destroy()
    import main
  elif (En_fee1.get() >= "10000"):
    messagebox.showerror("Warning", "Please Enter valid fee.", parent=root)
  else:
    messagebox.showerror("Warning", "Please Enter valid fee.", parent=root)

root = tk.Tk()
root.title("Enrollment page")
label = tk.Label(root,
                 text="Please Pay Fees ,If you are a Student",
                 font="20",
                 fg="red")
label.place(x=80, y=10)
En_fee = tk.Label(root, text="Enrollment Fee :", font='Verdana 10 bold')
En_fee.place(x=50, y=80)
En_fee = tk.IntVar()
En_fee1 = tk.Entry(root, width=20, textvariable=En_fee)
En_fee1.place(x=190, y=80)
btn_pay = tk.Button(root, text="Pay Now", font='Verdana 10 bold', command=pay)
btn_pay.place(x=140, y=120)
root.mainloop()