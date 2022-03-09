#Exercise 6.3

#1-5
input("Please enter any key and push enter\n")
input("Please enter your name and push enter\n")
input("Please enter your age and push enter\n")
name = input("Please enter your name again and push enter\n")
age = input(f"Hello {name}, Please enter your age again and push enter\n")

#6-10

print("\n")
fmovie = input("Please enter your favourite movie and push enter\n")
book = input("Please enter the name of a book and push enter\n")
adjective = input("Please enter any adjective and push enter\n")
noun = input("Please also enter any noun and push enter\n")
verb = input("Please enter any verb and push enter\n")

#11-15

print("\n")
#
print(f"Hello, {name}, your favourite movie is {fmovie}.")
print(f"You chose the book {book}.")
print(f"You entered your age as {age} years old.")
print(f"The {noun} is {verb}.")
print(f"The {noun} is {adjective}.")
print(f"The {noun} belongs to {name}.")
print(f"{name} is also {adjective}.")
print(f"{name} is a very nice person.")
print(f"I think {fmovie} is a cool movie too.")
#These are the 8 print statements for 11.

print("\n")
intage = int(input(f"Please enter your age as a number.\n"))
print(f"You will be {intage+10} in 10 years.")
print(f"You were born in approximately {2022-intage}.")
apples = int(input(f"How many apples do you have?\n"))

#16-20

print("\n")
friends = int(input(f"How many friends do you have?\n"))
print(f"You can share approximately {apples//friends} apples with all your friends.")
pizzas = int(input("How many pizzas do you want?\n"))
guests = int(input("How many guests are you feeding?\n"))
print(f"You can share approximately {8*pizzas//guests} slices among each the guests.")

#21-25

print("\n")
dollars = int(input("How many dollars do you have?\n"))
tvcost = int(input("How much money does a TV cost?\n"))
if tvcost > dollars:
	print("You can't afford this TV.")
elif dollars >= tvcost:
	print(f"If you buy this TV, you will have {dollars-tvcost} dollars left over.")
print(f"If you wait for a 20% sale for the TV, it will cost {tvcost*0.8} dollars instead.")

bitcoins = float(input(f"How many bitcoins do you have?\n"))

#26-30

print("\n")
bitcoins = bitcoins*62472
print(f"Your crypto portfolio is worth ${bitcoins} in NZD.")
income = int(input("How much money do you earn each week?\n"))
tax = float(input("How much tax do you pay? (As a decimal, not a percentage. (e.g 1.15))\n"))
print(f"You will take home {income/tax} each week after tax.")

#31 - 34

print("\n")
book2 = input("Please enter the name of a new book.\n")
print(str.lower(f"{book2}"))
print(str.upper(f"{book2}"))
print(str.title(f"{book2}"))
num2 = int(input("Please enter a number.\n"))
print(f"{book2} "*num2)