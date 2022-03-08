#Exercise 7.5

#1

icecreams = int(input("How many ice creams would you like to order?\n"))

if icecreams >= 20:
	print("There is not enough ice cream in stock.")
else:
	print(f"{icecreams} ice creams coming right up.")

#2

print("\n")
traveldistance = int(input("How far do you want to travel? (Just a number please.)\n"))

if traveldistance > 200:
	print("Please remember to fill your petrol tank before you leave.")
else:
	print("Please have a safe journey!")

#3

print("\n")
age = int(input("How old are you?\n"))

if age >= 18:
	print("You are an adult.")
else:
	print("You are a minor.")

#4

print("\n")
fmovie = input("What is your favourite movie?\n")

if fmovie.lower() == "lord of the rings":
	print("You have excellent taste.")
else:
	print("Lord of the rings is clearly superior to your favourite movie.")

#5

print("\n")
dptw = input("Have you heard of Darth Plagueis the Wise?\n")

if dptw.lower() == "no":
	print("The Tragedy of Darth Plagueis the Wise was a 'Sith legend' that was relayed to Anakin Skywalker by Palpatine, telling of his master, Darth Plagueis.\nPlagueis, the legend went, was 'so powerful and so wise he could use the Force to influence the midi-chlorians to create life,' and even saved others from dying.")
else:
	print("You must be a fan?")

#6

print("\n")
potc = input("Who directed Passion of the Christ?\n")

if potc.lower() == "mel gibson":
	print("Correct")
else:
	print("No Mel Gibson did.")

#7 Quiz

print("\n")
score = 0

riddle1 = input("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind.\nWhat am I?\n")

if riddle1.lower() == "echo":
	score = score+1
elif riddle1.lower() == "an echo":
	score = score+1
else:
	score = score

print("\n")
riddle2 = input("I have cities, but no houses. I have mountains, but no trees. I have water, but no fish.\nWhat am I?\n")

if riddle2.lower() == "map":
	score = score+1
elif riddle2.lower() == "a map":
	score = score+1
else:
	score = score

print("\n")
riddle3 = input("What disappears as soon as you say its name? (Teachers should know this.)\n")

if riddle3.lower() == "silence":
	score = score+1
else:
	score = score

print("\n")
riddle4 = input("I have keys, but no locks and space, and no rooms. You can enter, but you can’t go outside.\nWhat am I?\n")

if riddle4.lower() == "keyboard":
	score = score+1
elif riddle4.lower() == "a keyboard":
	score = score+1
else:
	score = score

print("\n")
riddle5 = input("What gets wet while drying?\n")

if riddle5.lower() == "towel":
	score = score+1
elif riddle5.lower() == "a towel":
	score = score+1
else:
	score = score

if score == 0:
	print(f"You got {score}. It's okay, it wasn't meant to be easy.")
elif score == 5:
	print(f"You got {score}. Wow, you're smart!")
else:
	print(f"You got {score}. Nice go!")