import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
root.geometry("300x300")
class Example(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.i = Image.open("ballfoot.png")
        self.ic= self.i.copy()
        self.bi = ImageTk.PhotoImage(self.i)
        self.b = tk.Label(self, image=self.bi)
        self.b.pack(fill=tk.BOTH, expand=tk.YES)
        self.b.bind('<Configure>', self._resize_image)
    def _resize_image(self,event):
        w = event.width
        h = event.height
        self.i = self.ic.resize((w, h))
        self.bi = ImageTk.PhotoImage(self.i)
        self.b.configure(image =  self.bi)
e = Example(root)
e.pack(fill=tk.BOTH, expand=tk.YES)
root.mainloop()