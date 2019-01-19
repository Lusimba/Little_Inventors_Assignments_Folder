li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print (squaredNumbers)
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print (evenNumbers)
squaredNumbers = map(lambda x: x**2, range(1,21))
print (squaredNumbers)
s = input()
u = unicode( s ,"utf-8")
print (u)