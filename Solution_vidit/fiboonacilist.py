def fibonacilist(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fibonacilist(n-1)+fibonacilist(n-2)

n = int(input("Please enter a number"))
numbers = [str(fibonacilist(x)) for x in range(0, n+1)]
print (",".join(numbers)) 
print("""hy bro i love this theme""")
     
       