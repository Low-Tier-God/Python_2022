#Exercise 7.5

#1

icecreams = int(input("How many ice creams would you like to order?"))

if icecreams >= 20:
	print("There is not enough ice cream in stock.")
elif icecreams < 20:
	print(f"{icecreams} ice creams coming right up.")

#2

traveldistance = int(input("How far do you want to travel? (Just a number please.)"))

if traveldistance > 200:
	print("Please remember to fill your petrol tank before you leave.")
elif traveldistance <= 200:
	print("Please have a safe journey!")