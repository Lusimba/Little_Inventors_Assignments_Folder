import time
print("___________________________________")
lop = []
loa = []
count = 15
size = 0.0
print("WELCOME TO -; LITLLE INVENTORS TRAVELS")
print("___________________________________")
class reservation:
    def __init__(self, human, year, arrive, arrivetime, departime, tickets, pay, cost):
        self.start = 'Hyderabad'
        self.person = human
        self.years = year
        self.arrive = arrive
        self.arrivation = arrivetime
        self.departure = departime
        self.tick = tickets
        self.payment = pay
        self.rupees = cost
    def printer(self):
        print("Name: %s   From: %s   To: %s   arrival time: %s" %(self.person, self.start, self.arrive, self.arrivation))
        print("no. of tickets: %s   paying by: %s   cost: %s   departure time: %s   age: %s" %(self.tick, self.payment, self.rupees, self.departure, self.years))
        print("Have a nice trip")
        print("******VISIT AGAIN******")
        print("Thank You")

x = 0
print("The places are-;")
print("Delhi, Mumbai, Chennai, Pune, and Bangalore")

arrivation = input("Which place do you want to go to  ")
arrivation = arrivation.lower()
people = int(input("How many people are you booking it for  "))

if people > 10:
    exit("Sorry, you can only book 10 or lesser tickets. Try again")

else:
    if people >= 5:
        print("Congratulations! :D You've gotten a bonus ticket for booking 5+ tickets")
        print("This is for family enjoyment time")
        people += 1

print("1 = 8 am, 2 = 9 am, 3 = 10 am, 4 = 11 am, 5 = 12 pm, 6 = 1 pm, 7 = 2 pm ... 15 = 10 pm")
departure = int(input("Pick the number following the time you want to start  "))

for loop in range(0, people):
    name = input("person: {} What's your name  ".format(loop+1))
    age = int(input("How many years are you  "))
    print("  ")
    if age > 15:
        size += 1.0
    elif age < 15:
        if age > 5:
            size += 0.5
    lop.append(name)
    loa.append(age)
    count -= 1
if count <= 0:
    print("Sorry, we don't have those many tickets")
if arrivation == "delhi":
    amount = size * 10000
    arriving = departure + 20
elif arrivation == "mumbai":
    amount = size * 8000
    arriving = departure + 15
elif arrivation == "pune":
    amount = size * 4000
    arriving = departure + 13
elif arrivation == "chennai":
    amount = size * 6000
    arriving = departure + 10
elif arrivation == "bangalore":
    amount = size * 2000
    arriving = departure + 7
else:
    exit("There was a problem. Can you please try it again")
print("Smartcard")
print("Fare")
print("Money")
payer = input("How do you want to pay  ")
print(" ")
for loop_2 in range(0, people):
    printing_1 = reservation(lop[loop_2], loa[loop_2], arrivation, arriving, departure+7, 15-count, payer, amount)
    printing_1.printer()
    print(" ")
    print(" ")