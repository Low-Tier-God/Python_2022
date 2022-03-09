#Exercise 8.7

#1-5
"""
sequence = ["0","1","1","2","3","5","8","13","21","34"]
print(sequence)
fruits = ["apples","grapes","bananas","plums","kiwi"]
print(fruits)
youtubers = ["PewDiePie","Jacksetpiceye","Markiplier","ishowspeed"]
print(youtubers)
songs = []
songs.append("Mr. Blue Sky")
songs.append("Hey Ya!")
songs.append("Don't Cry")
songs.append("T.N.T")
songs.append("Uptown Funk")
print(songs)

books = []
book1 = input("Please add your fifth favourite book.\n")
books.append({book1})
book2 = input("Please add your fourth favourite book.\n")
books.append({book2})
book3 = input("Please add your third favourite book.\n")
books.append({book3})
book4 = input("Please add your second favourite book.\n")
books.append({book4})
book5 = input("Please add your favourite book.\n")
books.append({book5})
print(books)
"""
#6
print("\n")
pizza_toppings = []
pizza = False

while pizza == False:
	topping = input("What toppings for your pizza? - push enter to finish.\n")
	if topping == "":
		print("Order Done")
		pizza = True
	elif topping.lower() in pizza_toppings:
		print("You already have that topping.")
	else:
		print("Great, we will add that to your pizza.")
		pizza_toppings.append(topping.lower())

print("Here are your toppings:")
print(pizza_toppings)

#7
fruits_in_basket = ["apple","banana","grapes","tomato","orange"]
basket_is_full = False

while basket_is_full == False:
	fruit_add = input("Please add a fruit to the basket - push enter to finish\n")
	if fruit_add == "":
		print("Okay, the basket is full.")
		basket_is_full = True
	elif fruit_add.lower() in fruits_in_basket:
		print("That fruit is already in the basket.")
	else:
		print("Okay, I will add it to the basket.")
		fruits_in_basket.append(fruit_add.lower())

print("Here are the fruits:")
print(fruits_in_basket)