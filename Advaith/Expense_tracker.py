import tkinter as tk
root = tk.Tk()
root.title("Expense Tracker")
fl = open("Cost.txt", "a+")
b = []
c = []
i = []
o, k, l = 0, 0, 0
def ent_1(event_1):
    global b, c, i, k, o, l
    if j.get() == 'Vijetha':
        o+=1
    elif j.get() == 'Balaji':
        k+=1 
    elif j.get() == 'Ratnadeep':
        l+=1
    b.append(str(e.get()))
    if h.get()/f.get() == 0:
        c.append(f.get())
    else:
        c.append(f.get()-((h.get()/100)*f.get()))
    i.append(j.get())
    j.set('Shop')
    e.set('')
    f.set(0)
    h.set(0)
def send(c, b, i, o, k, l):
    root_1 = tk.Tk()
    try:
        for x in range(0, len(b)):
            tk.Label(root_1, text = ("Store        = "+str(i[x]))).grid(row = 1, column = x)
            tk.Label(root_1, text = ("Cost         = "+str(c[x]))).grid(row = 3, column = x)
            tk.Label(root_1, text = ("Shopping item= "+str(b[x]))).grid(row = 2, column = x)
        tk.Label(root_1, text = " ").grid(column = 0)
        m = max(o, k, l)
        if m == o:
            n = "Vijetha"
        elif m == k:
            n = "Balaji"
        else:
            n = "Ratnadeep"
        tk.Label(root_1, text = "Most visited store = "+str(n)).grid(column = 0)
        tk.Label(root_1, text = "Total : ").grid(column = 0)
        tk.Label(root_1, text = " ₹"+str(sum(c))).grid(column = 1)
        fl.write("{} \n".format(str(sum(c))))
        c, b = [], []
    except Exception as ex:
        tk.Label(root_1, text = ex).grid()
        c, b =[], []
e = tk.StringVar()
f = tk.IntVar()
h = tk.IntVar() 
j = tk.StringVar()
j.set('shop')
tk.Label(root, text = "Item Name").grid(row = 1,column = 0)
tk.Label(root, text = "Cost").grid(row = 2,column = 0)
tk.Label(root, text = "Discount in %").grid(row = 3,column = 0)
oplist = ["Vijetha", "Balaji", "Ratnadeep"]
tk.OptionMenu(root, j, *oplist).grid(row = 0,column = 0)
a1 = tk.Entry(root, text = e)
a1.grid(row = 1,column = 1)
d1 = tk.Entry(root, text = f)
d1.grid(row = 2,column = 1)
g1 = tk.Entry(root, text = h)
g1.grid(row = 3,column = 1)
g1.bind('<Return>', ent_1)
a1.bind('<Return>', ent_1)
d1.bind('<Return>', ent_1)
submit = tk.Button(root, text = "SUBMIT", command = lambda: send(c, b, i, o,k, l))
submit.grid(row = 4,column = 1)
root.mainloop()
fl.close()