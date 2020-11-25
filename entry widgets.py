from tkinter import *
root = Tk()


def getvals():
    print("Submitting form")

    print(f"{uservar.get(), passvar.get()} ")



    with open("records.txt", "a") as f:
        f.write(f"{uservar.get(), passvar.get()}\n ")

root.geometry("655x333")



label = Label(text="login form",fg = "black",padx = 150 , pady = 30,font="Helvetica 26 bold")
label.grid(row=0,column=3)

username = Label(root,text="username",font="Helvetica 20 bold",fg = "black",pady = 20)
password = Label(root , text ="password",font="Helvetica 20 bold",fg = "black")
username.grid(row=1,column=2)
password.grid(row=2,column=2)

uservar=StringVar()
passvar=StringVar()

entryuser = Entry(root , textvariable = uservar,font="Helvetica 20 bold",relief = RIDGE)
entrypass = Entry(root , textvariable = passvar,font="Helvetica 20 bold",relief = RIDGE)
entryuser.grid(row=1,column=3)
entrypass.grid(row=2,column=3,pady=10)

btn = Button(root, text="Submit",font="Helvetica 16 bold",command = getvals)
btn.grid(row = 3 , column=3)

root.mainloop()