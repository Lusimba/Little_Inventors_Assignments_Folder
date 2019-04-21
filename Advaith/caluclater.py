z = int(input("How many calculations do you want to make   "))
for x in range(z):
	print("1 = Addition")
	print("2 = Subtraction")
	print("3 = Multiplication")
	print("4 = division")
	print("5 = Average")
	print("6 = power ")
	print("7 = exit")
	a = int(input("Which of the following do you choose  "))
	if a == 7:
		exit()
	else:
		print("  ")
	b = int(input("Type a number   "))
	c = int(input("Type a 2nd number   "))
	if a == 1:
		print("The sum of ", b," and ", c, " is ", b+c)
	elif a == 2:
		print("The difference between ", b," and ", c, " is ", b-c)
	elif a == 3:
		print("The product of ", b," and ", c, " is ", b*c)
	elif a == 4:
		print("The quotient of ", b," and ", c, " is ", b/c)
	elif a==5:
		print("The average of ", b," and ", c, " is ", (b+c)/2)
	elif a == 6:
		print("the power of ", b, " and ", c, " is ", b^c)
	else:
		print("Sorry I can not help you")
import tkinter
root = tkinter.Tk()
root.title("#########################  SIMPLE  CALUCLATOR  #########################")
var = 0
m = 0
if m == 0:
	def B1(inp, var):
		var = var + inp
		L = tkinter.Label(root, text = var)
		L.pack(side = "top")
		return
	def plus():
		m = 1
		return m
	def equal(var):
		L = tkinter.Label(root, text = var)
		L.pack(side = "top")
	B_1 = tkinter.Button(root, text = "1", width = 30, height = 2, command = B1(1, var))
	B_2 = tkinter.Button(root, text = "+", width = 30, height = 2, command = plus)
	B_3 = tkinter.Button(root, text = "=", width = 30, height = 2, command = equal(var))
	B_1.pack(side = "bottom")
	B_2.pack(side = "bottom")
	B_3.pack(side = "bottom")
elif m == 1:
	vari = 0
	def B1(inp, vari):
		vari = vari + inp
		globals(vari)
		L = tkinter.Label(root, textvariable = vari)
		L.pack(side = "top")
		return
	def equal(var, vari):
		L = tkinter.Label(root, textvariable = var)
		L.pack(side = "Top")
	B_1 = tkinter.Button(root, text = "1", width = 30, height = 2, command = B1(1, vari))
	B_3 = tkinter.Button(root, text = "=", width = 30, height = 2, command = equal(var, vari))
	B_1.pack()
	B_3.pack()
else:
	print("Error")
root.mainloop()