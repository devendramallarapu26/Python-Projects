print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
cost = 0
if size == "L":
    cost = 25
elif size == "M":
    cost = 20
else :
    cost = 15
if pepperoni == "Y":
    if size == "S":
        cost += 2
    elif size == "M" or size == "L":
        cost += 3

if extra_cheese == "Y":
    cost = cost + 1
print(f"Your final bill is: ${cost}.")
