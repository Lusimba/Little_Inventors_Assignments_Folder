from tkinter import *
import tkinter as tk
def submit():
    print("your idotic profile has been taken out of the toilet")
    root = tk.Tk() 
    root.configure(background="black") 
    root.title("Final Form")  
    root.geometry("400x450")
    fName = StringVar()
    fName = a1.get()
    lname = StringVar()
    lname = b1.get()
    gender = v.get()
    email = c1.get()
    country = tkvar.get()
    fp1 = h.get()
    fp2 = d.get()
    fp3 = e.get()
    fp4 = f.get()
    fp5 = g.get()
    fpList = []
    L1 = Label(root ,text = "your first name is--",fg = "white", bg = "black")
    L1.grid(row = 1,column = 0)
    L11 = Label(root,text = fName,fg = "white", bg = "black")
    L11.grid(row = 1,column = 1)
    L2 = Label(root,text = "your last name is--",fg = "white", bg = "black")
    L2.grid(row = 2,column = 0)
    L22 = Label(root,text = lname,fg = "white", bg = "black")
    L22.grid(row = 2,column = 1)
    L3 = Label(root,text = "your gender is--",fg = "white", bg = "black")
    L3.grid(row = 3,column = 0)
    if gender == 1:
        L33 = Label(root,text = "Male",fg = "white", bg = "black") 
        L33.grid(row = 3,column = 1)
    elif gender == 2:
        L33 = Label(root,text = "Female",fg = "white", bg = "black") 
        L33.grid(row = 3,column = 1)  
    L4 = Label(root,text = "your email is--",fg = "white", bg = "black")     
    L4.grid(row = 4,column = 0)
    L44 = Label(root,text = email,fg = "white", bg = "black")  
    L44.grid(row = 4,column = 1)  
    L5 = Label(root,text = "your country is--",fg = "white", bg = "black")
    L5.grid(row = 5,column = 0)
    L55 = Label(root,text = country,fg = "white", bg = "black")
    L55.grid(row = 5,column = 1)
    L6 = Label(root,text = "your food preferences",fg = "white", bg = "black")
    L6.grid(row = 6,column = 0)
    if fp1 == 1:
        fpList.append("French Fries,")
    if fp2 == 2:
        fpList.append("Burger,")  
    if fp3 == 3 :
        fpList.append("Ice-cream,")  
    if fp4 == 4:
        fpList.append("Pizza,")
    if fp5 == 5:
        fpList.append("Cake,")
    L66 = Label(root,text = fpList,fg = "white", bg = "black")   
    L66.grid(row = 6,column = 1) 

def destroy(self):
        """Internal function.

        Delete all Tcl commands created for
        this widget in the Tcl interpreter."""
        if self._tclCommands is not None:
            for name in self._tclCommands:
                #print '- Tkinter: deleted command', name
                self.tk.deletecommand(name)
            self._tclCommands = None    
if __name__ == "__main__":
    gui = tk.Tk() 
    gui.configure(background="white") 
    gui.title("Registration Form")  
    gui.geometry("350x450") 
    a = Label(gui ,text = "First Name",fg = "black", bg = "white")
    b = Label(gui ,text = "Last Name",fg = "black", bg = "white")
    c = Label(gui ,text = "Email Id",fg = "black", bg = "white")
    a.grid(row = 0,column = 0)
    b.grid(row = 1,column = 0)
    c.grid(row = 2,column = 0)
    a1 = Entry(gui)
    b1 = Entry(gui)
    c1 = Entry(gui)
    a1.grid(row = 0,column = 1)
    b1.grid(row = 1,column = 1)
    c1.grid(row = 2,column = 1)
    v = tk.IntVar()
    gender = Label(gui,text = "Gender",fg = "black", bg = "white")
    gender.grid(row = 3,column = 0)
    Male = Radiobutton(gui,text = "male",padx = 20,variable =  v,value = 1)
    Male.grid(row = 3,column = 1)
    Female = Radiobutton(gui,text = "female",padx = 20,variable =  v,value = 2)
    Female.grid(row = 4,column = 1)
    choices = { 'USA','INDIA','UK','ADVAITH (the best SHIT)','NONE'}
    tkvar = StringVar(gui)
    tkvar.set('Select')
    popupMenu = OptionMenu(gui, tkvar, *choices)
    Label(gui, text="Choose a country").grid(row = 5, column = 0)
    popupMenu.grid(row = 5, column =1)
    def change_dropdown(*args):
        print( tkvar.get() )
    tkvar.trace('w', change_dropdown)
    food = Label(gui,text = "food preferences",fg = "black", bg = "white")
    h = tk.IntVar()
    d = tk.IntVar()
    e = tk.IntVar()
    f = tk.IntVar()
    g = tk.IntVar()
    C1 = tk.Checkbutton(gui, text = "French-fries", variable = h, onvalue = 1 ,offvalue = 6)
    C2 = tk.Checkbutton(gui, text = "Burger", variable = d, onvalue = 2 ,offvalue = 7)
    C3 = tk.Checkbutton(gui, text = "Ice-cream", variable = e, onvalue = 3 ,offvalue = 8)
    C4 = tk.Checkbutton(gui, text = "Pizza", variable = f, onvalue = 4 ,offvalue = 9)
    C5 = tk.Checkbutton(gui, text = "Cake", variable = g, onvalue = 5 ,offvalue = 0)
    C1.grid(row = "6",column = "1")
    C2.grid(row = "7",column = "1")
    C3.grid(row = "8",column = "1")
    C4.grid(row = "9",column = "1")
    C5.grid(row = "10",column = "1")
    submitbutt = Button(gui, text = "Submit",command = submit) 
    submitbutt.grid(row = 11,column = 1)
    quit = Button(gui, text="QUIT", command=gui.destroy)
    quit.grid(row = 12,column = 1)
    gui.mainloop()