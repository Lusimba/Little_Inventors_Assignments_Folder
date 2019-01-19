oddlist = []
evenlist = []
alist = []
for counter in range(0,10+1):
    x = int(input("please enter a number: "))
    alist.append(x)
for counter2 in alist:
    if counter2%2==0:
        evenlist.append(counter2)
    else:
        oddlist.append(counter2)    

print("The even numbers are ",evenlist) 
print("The odd numbers are ",oddlist)        