from tkinter import *

main = Tk()
def destroy(self):
        """Internal function.

        Delete all Tcl commands created for
        this widget in the Tcl interpreter."""
        if self._tclCommands is not None:
            for name in self._tclCommands:
                #print '- Tkinter: deleted command', name
                self.tk.deletecommand(name)
            self._tclCommands = None  
def leftKey(event):
    print ("Left key pressed")

def rightKey(event):
    print ("Right key pressed")

def upkey(event):
    print("Up key pressed")

def downkey(event):
    print("Down key pressed")    

frame = Frame(main, width=100, height=100)
frame.bind('<Left>', leftKey)
frame.bind('<Right>', rightKey)
frame.bind('<Up>', upkey)
frame.bind('<Down>', downkey)
quit = Button(main, text="QUIT", command=main.destroy)
quit.pack()
frame.focus_set()
frame.pack()
main.mainloop()