# def ponp():
#     m = 0
#     n = 0
#     k = int(input("Type a number  "))
#     for l in range(1, k):
#         if k%l == 0:
#             m = m+1
#         else:
#             n = n+1
#     if m > 1:
#         print("%d is a composite number" %(k))
#     else:
#         print("%d is a prime number" %(k))
# ponp()
import time
print("Hello")
for x in range (0,5):  
    b = "Loading" + "." * x
    if x != 5:
        print (b, end="\r")
    time.sleep(1)