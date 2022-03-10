print("Hi, welcome to Ice Cream Maker")
order_complete = False
toppings_list = []

toppings_available = ["vanilla","strawberry","chocolate","sprinkles","nuts","raisins","chocolate sauce","flake","m&ms"]
print("Hello, customer, here are available toppings for your icecream:\n")
print(toppings_available)
print("\n")

topping_count = 0
	

while order_complete == False:
	topping = input("What topping? - push enter to finish")
if topping == "": 
	print("Order Done")
	order_complete = True
elif topping in toppings_list: 
	print("You already have that topping")
else:
	print("Great, adding it to the list")
	toppings_list.append(topping)

print("\n")
print("Here are your toppings:\n")
print(toppings_list.join(","))

