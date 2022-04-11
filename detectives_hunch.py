from adventurelib import *
Room.items = Bag()


outside = Room("""
	You stand outside, in front of you is a house that seems to be abandoned, a radio tower next to it.
	Your only choice is to investigate the house in the hopes of finding something that can turn on the radio tower.
	The porch you stand on creaks, the radio tower sits next to the house.""")


main_hall = Room("""
	You now stand in the hallway, you can hear rodents running across the board, it is dark.
	You feel adrenaline from fear pumping inside you, and you feel like you are being watched.
	The feeling to run away is looming over you.""")

lounge = Room("""
	You stand in the lounge, unable to collect your thoughts, you hear an eerie noise with an unknown location.
	You can hear your teeth chattering, it's very cold inside. There is the entrance to the kitchen.""")

kitchen = Room("""
	You stand in the kitchen and to your surprise, the light switch works this time, there is an unfamiliar scent and you can hear the buzzing of the light above you.
	You see the sink filled with filthy water and rusty kitchen appliances. The room is filled with mold.""")

second_hall = Room("""
	You stand in the next hallway, the dust inside is causing you to sniffle. The feeling of being watched is becoming harsher.
	You shiver from fear, the carpet seems to be wet, with liquid dripping from the wallpaper.""")

bedroom = Room("""
	You enter the bedroom, the first thing you notice is the massive, luxurious bed. You have a feeling that it calls you to sleep on it,
	you resist that temptation.
	Aside from the bed, there are a few drawers and a closet, maybe it's best to check those?""")

bathroom = Room("""
	The hallway has mold all over the curtains and tiles, the smell is hindering your ability to breathe.
	The faucet has water dropping from it, making a tiny, but audible splash sound when it hits the sink.
	You feel uncomfortable, you are only worried about getting out of there.""")

radio_tower = Room("""
	The dust flying around the tower is hindering your view, the moment you turn the light on, a swam of moths fills the room, irritated, you scan the room for any plugs.
	There is a bunch of plugs connected to a generator a radio sits by, you can choose to plug in the battery, but you also see a key on the table, which spikes your curiosity.""")

basement = Room("""
	You go down the flight of stairs leading to the basement, when you reach the bottom you hear footsteps above the basement
	...
	You hear a laugh, the basement door slams shut,
	You climb back up, desperately trying to lift the door, but it's stuck for good.
	You look for any tools that might help, but it's empty, and too dark to see anything.
	You realize that you've just fallen into a trap and you will be spending your last few days down here.
	Sucks to be you.""")

outside.north = main_hall
main_hall.west = second_hall
main_hall.north = lounge
second_hall.north = bedroom
outside.east = radio_tower	

#define items go here
Item.description = ""

knife = Item("a dirty knife","knife")
knife.description = "The knife has a dull sheen to it but it looks rather sharp."

silver_key = Item("silver key","a silver key","the silver key","skey")
silver_key.description = "The key shines faintly, it has a rough, metallic feeling. You put it back in your pocket."

gold_key = Item("gold key","a gold key","the gold key","gkey","key")
gold_key.description = "The key feels smooth feeling, althought it is scratched and rusted in some places. You put it back in your pocket."

battery = Item("battery","a bettery","the battery","batteries")
battery.description = "You lift the battery you hold in your hand, it's heavy; but you don't let anything weigh you down even in the scariest of times."

rusty_key = Item("rusty key","a rusty key","the rusty key","rkey")
rusty_key.description = "It's gritty and hollow, the key gives you a bad feeling. It looks fit for the basement in the second hallway."

#define bags go here

bedroom.items.add(silver_key)
kitchen.items.add(gold_key)
bathroom.items.add(battery)
radio_tower.items.add(rusty_key)


#adding items to bags code goes here
@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
@when("grab ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"You don't see a {item}")

#variables go here

current_room = outside
print(current_room)
inventory = Bag()
batteryon = False
kitchen_unlocked = False
bathroom_unlocked = False
basement_unlocked = False
witches = 1000

#current room you start in when starting the code

if witches <= 0:
	print("go get some witches")

@when("enter kitchen")
@when("go to kitchen")
@when("go inside kitchen")
@when("enter the kitchen")
def enter_house():
	global current_room
	if current_room is not lounge:
		say("There is no kitchen here")
		return

@when("plug in battery") #Removes the battery from inventory when you use it and unlocks the ability to use the radio
@when("use battery")
@when("plug battery in")
@when("connect battery")
@when("connect battery to plugs")
def use_battery():
	global batteryon
	if current_room == radio_tower:
		say("You place the battery down and put the plugs into it, a button glows indicating that it is functioning.")
		#battery.remove(inventory)
		batteryon = True
	elif battery is not in inventory:
		say("You need actually a battery to do that")


@when("look")
def look():
	print(current_room)
	say("You look around for any possible exits:")
	print(current_room.exits())
	if len(current_room.items) > 0: #if there are any items in the current room
		print("However, you also see:")
		for item in current_room.items:
			print(item)#prints out each items
	elif current_room == radio_tower:
		say("""It's too bright to see anything, not to mention the moths hindering your view.""")

if current_room == radio_tower:
	if rusty_key not in inventory:
		print(current_room)
	else:
		say("""The dust flying around the tower is hindering your view, the moment you turn the light on, a swam of moths fills the room, irritated, you scan the room for any plugs.
	There is a bunch of plugs connected to a generator a radio sits by, you can choose to plug in the battery or loiter.""") #Different dialogue if rusty key is already picked up

@when("inventory")
@when("show inventory")
@when("pocket")
@when("what is in my pocket")
@when("check inventory")
@when("check pocket")
def player_inventory():
	print("You are carring:")
	for item in inventory:
		print(item)

@when("look at ITEM")
@when("inspect ITEM")
def inspect(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying an {item}")


@when("use silver key")
@when("use the silver key")
@when("use a silver key")
@when("unlock kitchen")
@when("unlock kitchen door")
@when("unlock the kitchen door")
def unlock_kitchen():
	global kitchen_unlocked
	if current_room == lounge and inventory.find("silver key"):
		say("You unlock the kitchen door.")
		#inventory.remove("silver_key")
		kitchen_unlocked = True
	elif current_room is not lounge:
		say("You cannot use that here.")

@when("use gold key")
@when("use the gold key")
@when("use a gold key")
@when("unlock bathroom")
@when("unlock bathroom door")
@when("unlock the bathroom door")
def unlock_bathroom():
	global bathroom_unlocked
	if current_room == main_hall and inventory.find("gold key"):
		say("You unlock the bathroom door.")
		#inventory.remove("silver_key")
		bathroom_unlocked = True
	elif current_room is not main_hall:
		say("You cannot use that here.")

@when("use rusty key")
@when("use the rusty key")
@when("use a rusty key")
@when("unlock basement")
@when("unlock basement door")
@when("unlock the basement door")
def unlock_basement():
	global basement_unlocked
	if current_room == second_hall and inventory.find("rusty key"):
		say("You unlock the basement door.")
		#inventory.remove("rusty_key")
		basement_unlocked = True
	elif current_room is not second_hall:
		say("You cannot use that here.")


@when("go DIRECTION")
def travel(direction):
	global current_room
	
	if kitchen_unlocked == True:
		lounge.north = kitchen	

	if current_room == lounge and kitchen_unlocked == False and direction == 'north':
		print("The door to the kitchen is locked.")
		return

	if basement_unlocked == True:
		second_hall.west = basement

	if current_room == second_hall and basement_unlocked == False and direction == 'below':
		print("The door to the basement is locked")
		return

	if bathroom_unlocked == True:
		main_hall.east = bathroom

	if current_room == main_hall and bathroom_unlocked == False and direction == 'east':
		print("The door to the bathroom is locked.")

	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f'You go {direction}.')
		print(current_room)
	else:
		print("You can't go that way.")


def main():
	start()

if __name__ == '__main__':
	main()