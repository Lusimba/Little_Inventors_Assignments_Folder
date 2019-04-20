from tkinter import *
import tkinter as tk
rectanglecolor = 'orange'
background = tk_rgb = "#%02x%02x%02x" % (100, 255, 100)
disty = 6

root = tk.Tk()
root.geometry('1000x800+0+0')
root.title("Moving Object Test")

can = tk.Canvas (root,width=1000,height=800,bg=background)
can.grid()

rect = can.create_rectangle(400,0,600,200,fill=rectanglecolor)

for i in range(100):
    can.move(rect, 0, disty)
    root.update() # update the display
    root.after(30) # wait 30 ms

root.mainloop() 
