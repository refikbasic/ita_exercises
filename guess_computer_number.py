import random

computer=random.randrange(1,6)
user=int(input("Please input your number: "))
if user==computer:
    print("Congratulations, you guessed right!")
else:
    print("Unfortunatelly, you missed. Try again.")
    print("Mine number was ", computer)
