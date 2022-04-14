from adventurelib import *
Room.items = Bag()

#Rooms and their descriptions

outside = Room("""
	You're outside, you feel unsafe and uncertain about being outside in near pitch-black darkness,
	You hear the breeze of wind flying by. The grass is unnaturally cold and long.""")

main_hall = Room("""
	You now stand in the hallway, you can hear rodents running across the board, it is dark.
	You feel adrenaline from fear pumping inside you, and you feel like you are being watched.
	The feeling to run away is looming over you. There is a bathroom to your east.""")

lounge = Room("""
	You find yourself in the lounge, unable to collect your thoughts, you hear an eerie noise with an unknown location.
	You can hear your teeth chattering, it's very cold inside. There is an entrance to the kitchen.""")

kitchen = Room("""
	You walk into the kitchen and to your surprise, the light switch works this time, there is an unfamiliar scent and you can hear the buzzing of the light above you.
	You see the sink filled with filthy water and rusty kitchen appliances. The room is filled with mold.""")

second_hall = Room("""
	You look around the hallway, the dust inside is causing you to sniffle. The feeling of being watched is becoming harsher.
	You shiver from fear, the carpet seems to be wet, with liquid dripping from the wallpaper. You also notice a wooden hatch leading to what you assume is the basement.""")

bedroom = Room("""
	You enter the bedroom, the first thing you notice is the massive, luxurious bed. You have a feeling that it calls you to sleep on it,
	you resist that temptation.
	Aside from the bed, there are a few drawers and a closet, maybe it's best to check those?""")

bathroom = Room("""
	The bathroom has mold all over the curtains and tiles, the smell is hindering your ability to breathe.
	The faucet has water dropping from it, making a tiny, but audible splash sound when it hits the sink.
	You feel uncomfortable, you are only worried about getting out of there.""")

radio_tower = Room("""
	The dust flying around the tower is hindering your view, the moment you turn the light on, a swarm of moths fills the room, irritated, you scan the room for any plugs.
	There is a bunch of plugs connected to a generator which a radio sits by, you can choose to plug in the battery, but you also see a key on the table, which spikes your curiosity.""")

basement = Room("""
	You go down the flight of stairs leading to the basement, when you reach the bottom you hear footsteps above the basement.\n
	...\n
	You hear a laugh, the basement door slams shut,
	You climb back up, desperately trying to lift the door, but it's stuck for good.
	You look for any tools that might help, but it's empty, and too dark to see anything.
	You realize that you've just fallen into a trap and you will be spending your last few days down here.""")

#Room directions

outside.north = main_hall
main_hall.west = second_hall
main_hall.north = lounge
second_hall.north = bedroom
outside.east = radio_tower	

#Item and their descriptions

Item.description = ""

silver_key = Item("silver key","a silver key","the silver key")
silver_key.description = "The key shines faintly, it has a rough, metallic feeling. You put it back in your pocket."

gold_key = Item("gold key","a gold key","the gold key","key","golden key","the golden key","a golden key")
gold_key.description = "The key feels smooth feeling, althought it is scratched and rusted in some places. You put it back in your pocket."

battery = Item("battery","a battery","the battery","batteries")
battery.description = "You lift the battery you hold in your hand, it's heavy; but you don't let anything weigh you down even in the scariest of times."

rusty_key = Item("rusty key","a rusty key","the rusty key")
rusty_key.description = "It's gritty and hollow, the key gives you a bad feeling. It looks fit for a small lock. You put it back in your pocket."

#Items in rooms

bedroom.items.add(silver_key)
kitchen.items.add(gold_key)
bathroom.items.add(battery)
radio_tower.items.add(rusty_key)

#Ordered code for getting items

@when("get ITEM")
@when("get the ITEM")
@when("grab the ITEM")
@when("take the ITEM")
@when("pick up the ITEM")
@when("take ITEM")
@when("pick up ITEM")
@when("grab ITEM")
def pickup(item):#Function for obtaining items
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"You don't see a {item}")

#Variables

current_room = outside
print(current_room)
inventory = Bag()
batteryon = False
kitchen_unlocked = False
bathroom_unlocked = False
basement_unlocked = False

#Functions

say("""You, Jacob Harper, are a detective in your 30s on your way to investigate a case.
	While driving there, something appeared in front of your car almost instantly.
	You swerve into a ditch flipping the car over, damaging your car beyond repair.
	You get out and the engine is smoking.
	You give up on trying to repair the car and look around, maybe someone can help?
	That wasn't the case, however, you've travelled far enough to find a house sitting in the middle of the cold night.\n
	You stand outside, in front of you is the house that seems to be abandoned, a radio tower next to it.
	Your only choice is to investigate the house in the hopes of finding something that can turn on the radio inside the tower.
	The porch you stand on creaks, the radio tower sits next to the house.""") #Starting message and background of the player

@when("sleep on bed")
@when("lay on bed")
@when("sleep in bed")
@when("sleep on the bed")
@when("sleep in the bed")
@when("lay on the bed")
@when("lay in the bed")
def sleepyhead():
	global asleep
	if current_room == bedroom:
		say("""You lay down on the bed.
		You're asleep as soon as your head hits the pillow.\n
			...\n
			You don't wake up.""")
		quit()                             #Another bad ending for if you sleep on the bed in the bedroom

@when("plug in battery") #Removes the battery from inventory when you use it and unlocks the ability to use the radio
@when("use battery")
@when("plug battery")
@when("plug battery in")
@when("connect battery")
@when("connect battery to plugs")
@when("use the battery")
@when("plug in the battery")
def use_battery():
	global batteryon
	if current_room == radio_tower and inventory.find("battery"):
		say("You place the battery down and put the plugs into it, a button glows indicating that it is functioning. You can now use the radio.")
		batteryon = True
	else:
		say("You actually need a battery to do that")

@when("use radio")
@when("use the radio")
@when("try to use the radio")
@when("interact with radio")
@when("call radio")
@when("interact with the radio")
@when("call on radio")
@when("try to use radio")
def escape():
	global escape
	if current_room == radio_tower and batteryon == True:
		print("You use the radio and somebody responds, it's the authorities!")#Lets you escape when using the radio when the battery is on, good ending!
		quit()
	elif current_room == radio_tower and batteryon == False:
		print("The battery to the radio is not on.")
	else:
		print("There's no radio around.")

@when("look")
@when("look around")
def look():
	say("You look around for any possible exits:")
	print(current_room.exits())
	if len(current_room.items) > 0: #Checks if there are any items in the current room
		print("However, you also see:")
		for item in current_room.items:
			print(item) #Prints out each item in the room

@when("inventory")
@when("show inventory")
@when("pocket")
@when("what is in my pocket")
@when("check inventory")
@when("check pocket")
def player_inventory():
	print("You are carring:")
	for item in inventory:
		print(item) #This shows you what is currently in your inventory.

@when("look at ITEM")
@when("inspect ITEM")
@when("what is ITEM")
def inspect(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying an {item}") #This shows you what item you are carrying's description, you won't be able to if it is not in your inventory


@when("use silver key")
@when("use the silver key")
@when("use a silver key")
@when("unlock kitchen")
@when("unlock kitchen door")
@when("unlock the kitchen")
@when("unlock the kitchen door")
def unlock_kitchen():
	global kitchen_unlocked
	if current_room == lounge and inventory.find("silver key"):
		say("You unlock the kitchen door.")
		kitchen_unlocked = True
	elif current_room is not lounge:
		say("You cannot use that here.") #This unlocks the kitchen upon the command function, removes the item, and checks if you are in the right room to use the item

@when("use gold key")
@when("use the gold key")
@when("use a gold key")
@when("unlock bathroom")
@when("unlock bathroom door")
@when("unlock the bathroom")
@when("unlock the bathroom door")
@when("use golden key")
@when("use a golden key")
@when("use the golden key")
def unlock_bathroom():
	global bathroom_unlocked
	if current_room == main_hall and inventory.find("gold key"):
		say("You unlock the bathroom door.")
		bathroom_unlocked = True
	elif current_room is not main_hall:
		say("You cannot use that here.") #This unlocks the bathroom upon the command function, removes the item, and checks if you are in the right room to use the item

@when("use rusty key")
@when("use the rusty key")
@when("use a rusty key")
@when("unlock basement")
@when("unlock basement door")
@when("unluck the basement")
@when("unlock the basement door")
@when("unlock the hatch")
@when("unlock the basement hatch")
def unlock_basement():
	global basement_unlocked
	if current_room == second_hall and inventory.find("rusty key"):
		say("You unlock the basement door.")
		basement_unlocked = True
	elif current_room is not second_hall:
		say("You cannot use that here.") #This unlocks the basement upon the command function, removes the item, and checks if you are in the right room to use the item


@when("go DIRECTION") #Allows you to travel rooms by typing directions
def travel(direction):
	global current_room
	
	if kitchen_unlocked == True: #Checks if the kitchen is unlocked, allowing you to enter if it is
		lounge.north = kitchen	

	if current_room == lounge and kitchen_unlocked == False and direction == 'north': #Checks if the kitchen is unlocked, not allowing you to enter if it isn't
		print("The door to the kitchen is locked.")
		return


	if basement_unlocked == True: #If the basement is unlocked, you are able to enter it as it adds it to the room exits, this applies to the bathroom_unlocked and kitchen_unlocked variable
		second_hall.west = basement

	if current_room == second_hall and basement_unlocked == False and direction == 'west': #Checks if the basement is unlocked, not allowing you to enter if it isn't
		print("The door to the basement is locked.")
		return

	if current_room == basement:
		quit() #Quits the game when you enter the basement (bad ending)

	if bathroom_unlocked == True:
		main_hall.east = bathroom #Checks if the bathroom is unlocked

	if current_room == main_hall and bathroom_unlocked == False and direction == 'east':
		print("The door to the bathroom is locked.")

    #All of the codes below check what items you have for different dialogue when you enter the radio tower

	elif current_room == outside and direction == 'east' and "battery" in inventory and "rusty key" not in inventory:
		print("You go east.")
		current_room = radio_tower
		print(current_room)
		

	elif current_room == outside and direction == 'east' and "rusty key" in inventory and "battery" in inventory:
		print("You go east.")
		current_room = radio_tower
		say("""
		The dust flying around the tower is hindering your view, the moment you turn the light on, a swarm of moths fills the room, irritated, you scan the room for any plugs.
		There is a bunch of plugs connected to a generator which a radio sits by, you can choose to plug in the battery.
		""")

	elif current_room == outside and direction == 'east' and "battery" not in inventory and "rusty key" in inventory:
		print("You go east.")
		current_room = radio_tower
		say("""
		The dust flying around the tower is hindering your view, the moment you turn the light on, a swarm of moths fills the room, irritated, you scan the room for any plugs.
		There is a bunch of plugs connected to a generator which a radio sits by.
		""")

	elif current_room == outside and direction == 'east' and "battery" not in inventory and "rusty key" not in inventory:
		print("You go east.")
		current_room = radio_tower
		say("""	
		The dust flying around the tower is hindering your view, the moment you turn the light on, a swarm of moths fills the room, irritated, you scan the room for any plugs.
		There is a bunch of plugs connected to a generator which a radio sits by, you also see a key on the table, which spikes your curiosity.
		""")

	elif direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f'You go {direction}.')
		print(current_room)

	else:
		print("You can't go that way.")


def main():
	start()

if __name__ == '__main__':
	main()