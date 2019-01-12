
print("The first task -;")
def find_max():
    a = int(input("Type a number  "))
    b = int(input("Type a number  "))
    c = int(input("Type a number  "))
    d = max(a, b, c)
    print(d, "is the largest number")
find_max()

print("The second task -;")
def sum_of_list():
    loa = []
    f = 0
    e = int(input("Type how many numbers you want to add "))
    while(f < e):
        f = f + 1
        g = int(input("Type a number  "))
        loa.append(g)
    h = sum(loa)
    print("The sum of all the numbers is", h)
sum_of_list()

print("The third task is -;")
def pol():
    lom = []
    i = int(input("Type how many numbers you want to multiply  "))
    multi = 1
    for j in range(0, i):
        print(j)
        k = int(input("Type a number  "))
        lom.append(k)
    for l in lom:
        multi = multi*l
    print(multi)
pol()

print("The fourth task -;")
def reverse_string():
    m = input("Type a random.randrange word  ")
    mo = m[::-1]
    print("The reverse %s is %s" %(m, mo))
    m = input("Type a string  ")
    n = len(m)
    p = ""
    for o in range(n-1, -1, -1):
        p = p+m[o]
        p = p+" "
    p = p.upper()
    print("The reverse string is", p)
reverse_string()

print("The fifth task -;")
import random
def gr():
    a = random.randrange(1, 10)
    b = random.randrange(11, 20)
    c = int(input("Type a number  "))
    d = b - a
    if c <= d:
        print("Yes, %d is in the given range" %(c))
        print("The range is in between %d and %d" %(a, b))
    else:
        print("No, %d is not in the given range" %(c))
        print("The range is in between %d and %d" %(a, b))
gr()

print("The sixth task -;")
def ulc():
    g = 0
    h = 0
    e = input("Type a sentence  ")
    for f in e:
        a = f.isupper()
        if a == True:
            g = g + 1
        else:
            h = h+1
    print("The number of uppercases are %d" %(g))
    print("The number of lowercases are %d" %(h))
ulc()

print("The seventh task -;")
def lis():
    i = list(input("Type a list  "))
    j = ["hi", "bye", "see", "you", "die"]
    print(i)
    print(j)
lis()

print("The eighth task -;")
def ponp():
    m = 0
    n = 0
    k = int(input("Type a number  "))
    for l in range(1, k):
        if k%l == 0:
            m = m+1
        else:
            n = n+1
    if m > 1:
        print("%d is a composite number" %(k))
    else:
        print("%d is a prime number" %(k))
ponp()

print("The tenth task -;")
import datetime
def bday():
    o = int(input("Which month were you born "))
    p = int(input("Which day were you born "))
    s = datetime.datetime(year = 2019, month = o, day = p)
    q = datetime.datetime.now()
    r = q - s
    print(r, "time is left for your bday")
bday()

print("The last task -;")
def ppi():
    w = []
    t = int(input("Type a number  "))
    if t > 0:
        for u in range(0, int(t/2)):
            w.append(u)
        x = sum(w)
        if t == x:
            print("Yes, %d is a proper number" %(t))
        else:
            print("No, %d isn't a proper number" %(t))
    else:
        print("No, %d isn't a proper number" %(t))
ppi()