import tkinter
top = tkinter.Tk()
top.configure(background = "red")
def submit():
    root = tkinter.Tk() 
    root.configure(background="blue") 
    root.title("CREATED PROFILE!!!")  
    root.geometry("500x500")
    b = NameE.get()
    tkinter.Label(root, text = " ", bg = "blue", fg = "blue").pack()
    tkinter.Label(root, text = "Your name is ").pack()
    namep = tkinter.Label(root, text = b)
    namep.pack()
    c = EmailE.get()
    tkinter.Label(root, text = " ", bg = "blue", fg = "blue").pack()
    tkinter.Label(root, text = "Your email id is ").pack()
    emailp = tkinter.Label(root, text = c)
    emailp.pack()
    tkinter.Label(root, text = " ", bg = "blue", fg = "blue").pack()
    tkinter.Label(root, text = "Your gender is ").pack()
    if fm.get() == 1:
        Gender = tkinter.Label(root, text = "Male")
        Gender.pack()
    else:
        Gender = tkinter.Label(root, text = "Female")
        Gender.pack()
    tkinter.Label(root, text = " ", bg = "blue", fg = "blue").pack()
    tkinter.Label(root, text = "Your country is ").pack()
    country = tkinter.Label(root, text = tkvar.get())
    country.pack()
    tkinter.Label(root, text = " ", bg = "blue", fg = "blue").pack()
    tkinter.Label(root, text= "Your favourite food(s) is/are-;").pack()
    if CheckVar1.get() == 1:
        tkinter.Label(root, text= "French Fries, ").pack()
    if CheckVar2.get() == 1:
        tkinter.Label(root, text= "Pizza, ").pack()
    if CheckVar3.get() == 1:
        tkinter.Label(root, text= "Cake, ").pack()
    if CheckVar4.get() == 1:
        tkinter.Label(root, text= "Burger, ").pack()
    tkinter.Label(root, text= "etc.").pack()
    return
def quiter():
    exit()
fm = tkinter.IntVar()
fm.set(0)

Name = tkinter.Label(top, text="Full Name")
Name.grid(row = 0, column = 0)
NameE = tkinter.Entry(top, bd = 10, width = 25)
NameE.grid(row = 0, column = 1)

Email = tkinter.Label(top, text="Email ID")
Email.grid(row = 1, column = 0)
EmailE = tkinter.Entry(top, bd = 10, width = 30)
EmailE.grid(row = 1, column = 1)

Gend_1 = tkinter.Label(top, text="Gender")
Gend_1.grid(row = 2, column = 0)
Gender_1 = tkinter.Radiobutton(top, text = "Male",padx = 20, variable = fm, value = 1)
Gender_1.grid(row = 4, column = 0)
Gender_2 = tkinter.Radiobutton(top, text = "Female",padx = 20, variable = fm, value = 2)
Gender_2.grid(row = 4, column = 1)
tkinter.Label(top, text = " ", bg = "red", fg = "red").grid()
count =("Asia", "Africa", "America", "Oceania")
tkvar = tkinter.StringVar()
tkvar.set('select')
popup = tkinter.OptionMenu(top, tkvar, *count)
popup.grid(row = 6, column = 0)
tkinter.Label(top, text = " ", bg = "red", fg = "red").grid()
C = tkinter.Label(top, text = "Pick your favourite food -;")
C.grid(row = 8, column = 0)
CheckVar1 = tkinter.IntVar()
CheckVar2 = tkinter.IntVar()
CheckVar3 = tkinter.IntVar()
CheckVar4 = tkinter.IntVar()
C1 = tkinter.Checkbutton(top, text = "French fries", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0)
C2 = tkinter.Checkbutton(top, text = "Pizza", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0)
C3 = tkinter.Checkbutton(top, text = "Cake", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0)
C4 = tkinter.Checkbutton(top, text = "Burger", variable = CheckVar4, \
                 onvalue = 1, offvalue = 0)
tkinter.Label(top, text = " ", bg = "red", fg = "red").grid(row = 9)
C1.grid(row = 10, column = 0)
C2.grid(row = 10, column = 1)
tkinter.Label(top, text = " ", bg = "red", fg = "red").grid(row = 9)
C3.grid(row = 12, column = 0)
C4.grid(row = 12, column = 1)
tkinter.Label(top, text = " ", bg = "red", fg = "red").grid()
Button = tkinter.Button(top, text = "SUBMIT", command = submit)
Button.grid(row = 20, column = 0)

Button2 = tkinter.Button(top, text="EXIT", command = quiter)
Button2.grid(row = 20, column = 1)

top.mainloop()