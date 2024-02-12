from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
import re



def switch():
    root.destroy()


def signup():
    def validate_phone_number(phone_number):
        phone_pattern = r'^\d{10}$'
        return re.match(phone_pattern, phone_number)

    def validate_email(email1):
        #  regular expression pattern for a valid email address.
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_pattern, email1)

    def validate_data():
        #  regular expression pattern for a valid phone number.
        phone_number = mobile_No.get()
        email1 = email.get()

        phone_valid = validate_phone_number(phone_number)
        email_valid = validate_email(email)

        if phone_valid and email_valid:
            messagebox.showinfo("Validation Result", "Valid Phone Number and Email")
        elif phone_valid:
            messagebox.showinfo("Validation Result", "Valid Phone Number\nInvalid Email")
        elif email_valid:
            messagebox.showinfo("Validation Result", "Invalid Phone Number\nValid Email")
        else:
            messagebox.showerror("Validation Result", "Invalid Phone Number and Email")

    # signup database connect
    if first_name.get() == "" or last_name.get() == "" or age.get() == "" or city.get() == "" or add.get() == "" or user_name.get() == "" or password.get() == "" or very_pass.get() == "" or mobile_No.get() == "" or email.get() == "":
        messagebox.showerror("Error", "All Fields Are Required", parent=root)
    elif len(password.get()) <= 5:
        messagebox.showerror("Error", "PLease Enter password upto 5 Words.", parent=root)
    elif password.get() != very_pass.get():
        messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=root)

    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="cism")
            cur = con.cursor()
            cur.execute("select * from user_information where username=%s", user_name.get())
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User Name Already Exits", parent=root)
            else:
                cur.execute(
                    "insert into user_information(field,first_name,last_name,age,gender,city,address,username,password,mobile_No,email) "
                    "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    [
                        field.get(),
                        first_name.get(),
                        last_name.get(),
                        age.get(),
                        var.get(),
                        city.get(),
                        add.get(),
                        user_name.get(),
                        password.get(),
                        mobile_No.get(),
                        email.get()
                    ])
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Registration Successfully", parent=root)
                clear()
                switch()

        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=root)


def clear():
    first_name.delete(0, END)
    last_name.delete(0, END)
    age.delete(0, END)
    var.set("Male")
    city.delete(0, END)
    add.delete(0, END)
    user_name.delete(0, END)
    password.delete(0, END)
    very_pass.delete(0, END)
    mobile_No.delete(0, END)
    email.delete(0, END)


# clear data function
root = Tk()
root.title("Faculty Registration Form")
root.maxsize(width=500, height=600)
root.minsize(width=500, height=600)

heading = Label(root, text="Faculty Registration", font='Verdana 20 bold')
heading.place(x=80, y=60)

field = Entry(root, font='Verdana 10 bold', fg="blue")
field.configure(state=tk.DISABLED)
field.place(x=80, y=100)
# form data label
first_name = Label(root, text="First Name :", font='Verdana 10 bold')
first_name.place(x=80, y=130)

last_name = Label(root, text="Last Name :", font='Verdana 10 bold')
last_name.place(x=80, y=160)

age = Label(root, text="Age :", font='Verdana 10 bold')
age.place(x=80, y=190)

Gender = Label(root, text="Gender :", font='Verdana 10 bold')
Gender.place(x=80, y=313)

city = Label(root, text="City :", font='Verdana 10 bold')
city.place(x=80, y=366)

add = Label(root, text="Address :", font='Verdana 10 bold')
add.place(x=80, y=399)

user_name = Label(root, text="User Name :", font='Verdana 10 bold')
user_name.place(x=80, y=220)

password = Label(root, text="Password :", font='Verdana 10 bold')
password.place(x=80, y=253)

very_pass = Label(root, text="Verify Password: ", font='Verdana 10 bold')
very_pass.place(x=80, y=283)

mobile_No = Label(root, text="Mobile No. :", font='Verdana 10 bold')
mobile_No.place(x=80, y=422)

email = Label(root, text="Email ID :", font='Verdana 10 bold')
email.place(x=80, y=455)
# Entry Box ------------------------------------------------------------------
field = StringVar(root, value="FACULTY")
first_name = StringVar()
last_name = StringVar()
age = StringVar(root, value='0')
var = StringVar()
city = StringVar()
add = StringVar()
user_name = StringVar()
password = StringVar()
very_pass = StringVar()
mobile_No = IntVar()
email = StringVar()

first_name = Entry(root, width=40, textvariable=first_name)
first_name.place(x=200, y=133)

last_name = Entry(root, width=40, textvariable=last_name)
last_name.place(x=200, y=163)

age = Entry(root, width=40, textvariable=age)
age.place(x=200, y=193)

user_name = Entry(root, width=40, textvariable=user_name)
user_name.place(x=200, y=220)

password = Entry(root, width=40, textvariable=password)
password.place(x=200, y=253)

very_pass = Entry(root, width=40, show="*", textvariable=very_pass)
very_pass.place(x=200, y=283)

ttk.Radiobutton(root, text='Male', value="Male", variable=var).place(x=200, y=313)

ttk.Radiobutton(root, text='Female', value="Female", variable=var).place(x=200, y=333)

city = Entry(root, width=40, textvariable=city)
city.place(x=200, y=366)

add = Entry(root, width=40, textvariable=add)
add.place(x=200, y=399)

mobile_No = Entry(root, width=40, textvariable=checkcontact)
mobile_No.place(x=200, y=422)

email = Entry(root, width=40, textvariable=email)
email.place(x=200, y=455)

# button login and clear

btn_signup = Button(root, text="Signup", font='Verdana 10 bold', command=signup)
btn_signup.place(x=200, y=488)

btn_login = Button(root, text="Clear", font='Verdana 10 bold', command=clear)
btn_login.place(x=280, y=488)

root.mainloop()
# ---------------------------------------------------------------------------End Singup Window-----------------------------------


# -------------------------------------------------------------------------- End Login Window ---------------------------------------------------
