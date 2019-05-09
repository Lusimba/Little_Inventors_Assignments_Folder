#here is all the testing i do
from tkinter import *
import tkinter as tk
root = tk.Tk()
def motion():
      if m==1:
           can.move (id, 0,-5)
      elif m==3:
           can.move (id,0, 5)
      elif m==0:
           can.move (id,5, 0)
      elif m == 2:
           can.move (id, - 5,0)
      else:
          can.move (id, 0,0)     
      can.after (50, motion)
def arrows (event):
    global m
    if event.keysym=='Up':
          m=1
    elif event.keysym=='Down':
          m=3
    elif event.keysym=='Right':
          m=0
    elif event.keysym=='Left':
          m=2
    else:
        m=0      
can=tk.Canvas (width=800,height=800)
can.pack ()
id=can.create_oval (50,20,200,200) 
m=3
motion () 
can.bind ('<Button-1>',motion)
can.bind_all ('<Key>', arrows) 
root.mainloop()
