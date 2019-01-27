print("The first example of lambda function")
def myfunc(b):
  return lambda a : a * b
mydoubler = myfunc(2)
mytripler = myfunc(3)
print("11 * 2 =", mydoubler(11))
print("32 * 3 =", mytripler(32))

print("The second example of lambda function")
i = lambda j, k, l: (j+k+l)*4
m = i(2, 5, 3)
n = i(9, 1, 7)
o = i(8, 2, 6)
p = int(input("Pick a number 1, 2, 3  "))
if p == 1:
    print("The sum of random 3 numbers multiplied by 4 is %s" %(m))
elif p == 2:
    print("The sum of random 3 numbers multiplied by 4 is %s" %(n))
elif p == 2:
    print("The sum of random 3 numbers multiplied by 4 is %s" %(o))
else:
    print("I can't help with that")

print("The third example")
