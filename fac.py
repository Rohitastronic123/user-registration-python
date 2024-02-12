import tkinter as tk
from tkinter import ttk, messagebox


def pay():
  if (fac_1.get() == "Fac_2023"):
    messagebox.showinfo("Success", "Successfully", parent=root)
    root.destroy()
    import faculty
  else:
    messagebox.showerror("Warning", "Please Enter valid code.", parent=root)

root = tk.Tk()
root.title("Faculty Page")
label = tk.Label(root,
                 text="Please enter code ,if you are a Faculty",
                 font="20",
                 fg="red")
label.place(x=80, y=10)
En_fac = tk.Label(root, text="Faculty Code :", font='Verdana 10 bold')
En_fac.place(x=50, y=80)
En_fee = tk.StringVar()
fac_1 = tk.Entry(root, width=20,show="*", textvariable=En_fee)
fac_1.place(x=190, y=80)
btn_sub = tk.Button(root, text="Submit Now", font='Verdana 10 bold', command=pay)
btn_sub.place(x=140, y=120)
root.mainloop()