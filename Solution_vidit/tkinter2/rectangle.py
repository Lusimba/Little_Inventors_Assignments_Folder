import tkinter as tk
root = tk.Tk()
C = tk.Canvas(root)
C.pack()
C.create_polygon(210, 110, 150, 110, 150, 30, 210, 30, 210, 110)
root.mainloop()