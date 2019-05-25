# Create a GUI expense tracker program that performs the following functions.
# 1. Keeps track of shopping spendings for the family
# 2. Calculates the total expense of bills to be paid at the end of the month. 
# 3. Factors in discounts and calculates the total amount saved at the end of the month. 
# 4. Displays the most frequently visited stores/shops.
# 5. Create a report of this information in a Microsoft Word file format and store it in your Python files folder. 
# Upload it to GitHub. 
import tkinter as tk
root = tk.Tk()
root.title("Expense Tracker")
fl = tk.Tk()
b = []
c = []
i = []
def ent_1(event_1):
    global b, c, i
    try:
        b.append(str(e.get()))
        c.append(f.get()-(h.get()/100*f.get()))
        e.set('')
        f.set(0)
        h.set(0)
    except:
        pass
def send(c, b, i):
    root_1 = tk.Tk()
    try:
        for x in range(0, len(b)):
            v = ("shopping item = "+str(b[x]))
            u = (", Cost = "+str(c[x]))
            tk.Label(root_1, text = v).grid(row = x, column = 0)
            tk.Label(root_1, text = u).grid(row = x, column = 1)
        tk.Label(root_1, text = "Total : ").grid(column = 0)
        tk.Label(root_1, text = " ₹"+str(sum(c))).grid(column = 1)
        fl.write("Total : ")
        fl.write(" ₹"+str(sum(c)))
        c, b = [], []
    except Exception as ex:
        tk.Label(root_1, text = ex).grid()
        c, b =[], []
e = tk.StringVar()
f = tk.IntVar()
h = tk.IntVar() 
tk.Label(root, text = "Item Name").grid(row = 0,column = 0)
tk.Label(root, text = "Cost").grid(row = 1,column = 0)
tk.Label(root, text = "Discount in %").grid(row = 2,column = 0)
a1 = tk.Entry(root, text = e)
a1.grid(row = 0,column = 1)
d1 = tk.Entry(root, text = f)
d1.grid(row = 1,column = 1)
g1 = tk.Entry(root, text = h)
g1.grid(row = 2,column = 1)
g1.bind('<Return>', ent_1)
a1.bind('<Return>', ent_1)
d1.bind('<Return>', ent_1)
submit = tk.Button(root, text = "SUBMIT", command = lambda: send(c, b, i))
submit.grid(row = 4,column = 1)
root.mainloop()
fl.close()