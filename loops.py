#Exercise 9.2
"""
print("Hi, welcome to Ice Cream Maker")
order_complete = False
toppings_list = []

toppings_available = ["vanilla","strawberry","chocolate","sprinkles","nuts","raisins","chocolate sauce","flake","m&ms"]
print("Hello, customer, here are available toppings for your icecream:\n") #Prints avaiailable toppings
print(toppings_available)
print("\n") #This all prints the toppings available

topping_count = 0

while order_complete == False:
	topping = input("What topping? - push enter to finish")
	if topping.lower() == "": 
		print("Order Done")
		order_complete = True #Shows the order is complete
	elif topping.lower() not in toppings_available:
		print("That topping is not in the available toppings.") #Makes it so that any topping entered not in the list isn't added
	elif topping.lower() in toppings_list:
		print("You already have that topping")
	else:
		print("Great, adding it to the list")
		toppings_list.append(topping.lower()) #Makes it so that capitals in the inputs don't change the value and
		#are printed in the same case each time





print("\n")
print("Here are your toppings:\n")
print(*toppings_list,sep = "\n")
"""
#Exercise 9.3

countup = []
start = 0

while countup != 100:
	start = start + 2
	start.append(countup)
	print(countup)