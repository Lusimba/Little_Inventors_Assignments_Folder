from tkinter import *
window = Tk()
window.state('zoomed')
window.configure(bg = 'green4')

def drag(event):
    card.place(x=event.x_root, y=event.y_root,anchor=CENTER)

card = Canvas(window, width=74, height=97, bg='blue')
card.place(x=300, y=600,anchor=CENTER)
card.bind("<B1-Motion>", drag)

window.mainloop()