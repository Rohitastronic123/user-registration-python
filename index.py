from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
import re


def checkname(name):
  if name.isalnum():
    return True
  if name == "":
    return True
  else:
    messagebox.showwarning("Invalid", "Not allowed " + name[-1])
    return False


"""
^                                            Match the beginning of the string
(?=.*[0-9])                                  Require that at least one digit appear anywhere in the string
(?=.*[a-z])                                  Require that at least one lowercase letter appear anywhere in the string
(?=.*[A-Z])                                  Require that at least one uppercase letter appear anywhere in the string
(?=.[.!@$%^&(){}[]:;<>,.?/~_+-=|\])    Require that at least one special character appear anywhere in the string
.{8,32}                                      The password must be at least 8 characters long, but no more than 32
$                                            Match the end of the string.
"""


def checkpassword(password):
  if len(password) <= 20:
    if re.match("^(?=.[0-9])(?=.[a-z])(?=.[A-Z](?=.[^a-bA-B0-9]))", password):
      return True

    messagebox.showwarning("Invalid", "Enter valid password")
    return False
  else:
    messagebox.showwarning("Invalid", "Length try to exceed")
    return False


def checkcontact(con):
  if con.isdigit():
    return True
  if len(str(con)) == 0:
    return True

  else:
    messagebox.showwarning("Invalid", "Invalid Entry")
    return False


def checkemail(email):
  if len(email) > 7:
    if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",
                email):
      return True

    else:
      messagebox.showwarning("Alert", "Invalid E-mail enter by user")
      return False
  else:
    messagebox.showwarning("Alert", "Email length is too small")


# validate all field at submit time
def validations():
  x = y = 0
  if first_name.get() == "":
    messagebox.showinfo("Alert", "Enter your name first")
  elif last_name.get() == "":
    messagebox.showinfo("Alert", "Enter your last name")
  elif user_name.get() == "":
    messagebox.showinfo("Alert", "Enter your user name")
  elif password.get() == "":
    messagebox.showinfo("Alert", "Enter Password")
  elif mobile_No.get() == "" or len(mobile_No.get()) != 10:
    messagebox.showinfo("Alert", "Enter valid Contact ")
  elif email.get() == "":
    messagebox.showinfo("Alert", "Enter Email")
  elif age.get() == "":
    messagebox.showinfo("Alert", "Enter Age")
  elif var.get() == 0:
    messagebox.showinfo("Alert", "Select Gender")
  elif city.get() == "" or city.get() == "Enter your city":
    messagebox.showinfo("Alert", "Select country")
  elif add.get() == "" or add.get() == "Enter your address":
    messagebox.showinfo("Alert", "Select country")
  elif email.get() != None and password.get() != None:

    x = checkemail(email.get())
    y = checkpassword(password.get())
    print(x, y)


#----------------------------------------------------------- Signup Window --------------------------------------------------


def switch():
  root.destroy()


def signup():
  # signup database connect

  if first_name.get() == "" or last_name.get() == "" or age.get(
  ) == "" or city.get() == "" or add.get() == "" or user_name.get(
  ) == "" or password.get() == "" or very_pass.get() == "" or mobile_No.get(
  ) == "" or email.get() == "":
    messagebox.showerror("Error", "All Fields Are Required", parent=root)
  elif password.get() != very_pass.get():
    messagebox.showerror("Error",
                         "Password & Confirm Password Should Be Same",
                         parent=root)
  else:
    try:
      con = pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="cism")
      cur = con.cursor()
      cur.execute("select * from user_information where username=%s",
                  user_name.get())
      row = cur.fetchone()
      if row is not None:
        messagebox.showerror("Error", "User Name Already Exits", parent=root)
      else:
        cur.execute(
            "insert into user_information(first_name,last_name,age,gender,city,address,username,password,mobile_No,email) "
            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [
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
        messagebox.showinfo("Success",
                            "Registration Successfully",
                            parent=root)
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
root.title("User Registration Form")
root.maxsize(width=500, height=600)
root.minsize(width=500, height=600)

heading = Label(root, text="User Registration", font='Verdana 20 bold')
heading.place(x=80, y=60)

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
mobile_No.place(x=80, y=432)

email = Label(root, text="Email ID :", font='Verdana 10 bold')
email.place(x=80, y=465)
# Entry Box ------------------------------------------------------------------

first_name = StringVar()
last_name = StringVar()
age = IntVar(root, value='0')
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
very_pass.place(x=220, y=283)

ttk.Radiobutton(root, text='Male', value="Male", variable=var).place(x=200,
                                                                     y=313)

ttk.Radiobutton(root, text='Female', value="Female", variable=var).place(x=200,
                                                                         y=333)

city = Entry(root, width=40, textvariable=city)
city.place(x=200, y=366)

add = Entry(root, width=40, textvariable=add)
add.place(x=200, y=399)

mobile_No = Entry(root, width=40, textvariable=checkcontact)
mobile_No.place(x=200, y=432)

email = Entry(root, width=40, textvariable=email)
email.place(x=200, y=465)

# button login and clear

btn_signup = Button(root,
                    text="Signup",
                    font='Verdana 10 bold',
                    command=signup)
btn_signup.place(x=200, y=498)

btn_login = Button(root, text="Clear", font='Verdana 10 bold', command=clear)
btn_login.place(x=280, y=498)

root.mainloop()
#---------------------------------------------------------------------------End Singup Window-----------------------------------

#-------------------------------------------------------------------------- End Login Window ---------------------------------------------------
