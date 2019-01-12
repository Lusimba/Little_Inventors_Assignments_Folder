a = int (input("type a number  "))
b = int (input("type a number  "))
c = int (input("type a number  "))
d = int (input("type a number  "))
# print(a)
# print(b)
# print(c)
# print(d)
e = a**b
f = c**d
g = 1
# print("%d^%d = %d" %(a, b, e))
# print("%d^%d = %d" %(c, d, f))
# print("The number of atoms present ON Earth are", f-e)
h = int(input("type a number  "))
for i in range(1, h+1):
	g = g*i
	print("%d * %d = %d" %(g/i, i, g))
# print("The factorial of %d is %d" %(h, g))
j = f-e
# if j < g:
# 	print("Therefore the no. of atoms are greater than 52!")
# 	print("The differenece is", g-j)
# 	print("Advaith wins :D ;D :) ;) :> ;> :] ;] :} ;}")
# else:
# 	print("Therefore the no. of atoms are lesser than 52!")
# 	print("The differenece is", j-g)
# 	print("Adithi wins :C ;C :( ;( :< ;< :[ ;[ :{ ;{")
# e = 52*51*50*49*48*47*46*45*44*43*42*41*40*39*38*37*36*35*34*33*32*31*30*29*28*27*26*25*24*23*22*\
# 21*20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1
# f = (a**b) - (c**d)
# print("The differenece is", e-f)
g = str(g)
j = str(j)
print(len(g))
print(len(j))