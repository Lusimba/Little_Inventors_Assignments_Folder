import tkinter as tk
import time
root = tk.Tk()
a = 0
et = 0
def enterpress():
    global a, et
    if a == 0:
        et = time.time()
    a+=1
    tex.set(a)
    if a == 10:
        st = time.time()
        print("click speed = {} clicks/second".format(10/(st-et)))
        a = 0
        tex.set(a)
tex = tk.IntVar()
tk.Label(root, textvariable = tex).grid()
tk.Button(root, text = "Click Me!!!", height = 10, width = 20,command = enterpress).grid()
root.mainloop()