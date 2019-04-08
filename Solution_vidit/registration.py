from tkinter import *
if __name__ == "__main__": 
    gui = Tk() 
    gui.configure(background="green") 
    gui.title("Registration Form")  
    gui.geometry("350x150") 
    equation = StringVar()  
    expression_field = Entry(gui, textvariable=equation) 
    expression_field.grid(columnspan=4, ipadx=70) 
