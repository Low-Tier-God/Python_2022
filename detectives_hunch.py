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
	You enter the kitchen and to your surprise, the light switch works this time, there is an unfamiliar scent and you can hear the buzzing of the light above you.
	You see the sink filled with filthy water and rusty kitchen appliances.""")

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


#current room you start in when starting the code

@when("enter inside")
@when("enter house")
@when("enter hall")
@when("enter the house")
def enter_house():
	global current_room
	if current_room is not outside: #Checks if outside
		say("There is no house here")
		return
	else:
		current_room = main_hall
		say("""You swing open the door and immediately feel your hand across the wall to find a light switch.
			The wallpaper is smooth, and you find the switch, upon flicking the light on, you are met with a dim light with an audible buzzing sound.
			""")

@when("enter basement")
@when("go to basement")
@when("go inside basement")
@when("enter the basement")
def enter_house():
	global current_room
	if current_room is not second_hall:
		say("There is no radio tower here")
		return
	elif rusty_key not in inventory: #Item required before entering
		say("You need some sort of key to enter as it is locked.")
		return
	else:
		current_room = basement
		say("""You unlock the door and enter the basement.""")
		print(current_room)

@when("enter kitchen")
@when("go to kitchen")
@when("go inside kitchen")
@when("enter the kitchen")
def enter_house():
	global current_room
	if current_room is not lounge:
		say("There is no kitchen here")
		return
	elif silver_key not in inventory: #Item required before entering              #needs fixed
		say("You need some sort of key to enter as it is locked.")
		return
	else:
		current_room = kitchen
		say("""You unlock the door and enter the kitchen.""")
		print(current_room)

@when("enter bathroom")
@when("go to bathroom")
@when("go inside bathroom")
def enter_house():
	global current_room
	if current_room is not main_hall:
		say("There is no kitchen here")
		return
	elif gold_key not in inventory: #Item required before entering
		say("You need some sort of key to enter as it is locked.")
		return
	else:
		current_room = kitchen
		say("""You unlock the door and enter the bathroom.""")
		print(current_room)

@when("enter radio tower")
@when("go to radio tower")
@when("go inside radio tower")
def enter_house():
	global current_room
	if current_room is not outside:
		say("There is no radio tower here")
		return
	elif battery not in inventory: #Battery required for entry
		say("There's no point in going in without the battery.")
		return
	else:
		current_room = radio_tower
		say("""The electricity station outside is making a loud buzzing noise, you open the door but quickly shut it upon hearing crunching leaves behind you.
	You look outside and realize it was only the wind. You flick the lights on.""")
		print(current_room)

@when("plug in battery") #Removes the battery from inventory when you use it and unlocks the ability to use the radio
@when("use battery")
@when("plug battery in")
@when("connect battery")
@when("connect battery to plugs")
def use_battery():
	say("You place the battery down and put the plugs into it, a button glows indicating that it is functioning.")
	battery.remove(inventory)
	batteryon = True



@when("look")
def look():
	print(current_room)
	say("You look around for any possible exits:")
	print(current_room.exits())
	if len(current_room.items) > 0: #if there are any items in the current room
		print("However, you also see:")
		for item in current_room.items:
			print(item)#prints out each items

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

@when("use ITEM")
def use(item):
	if inventory.find(item)==silver_key and current_room == lounge:
		print("You use the key to unlock the kitchen door.")
		print("The door to the kitchen creaks as it swings open.")
		lounge.north = kitchen
	else:
		print("You can use that here")

@when("go DIRECTION")
def travel(direction):
	global current_room
	
	if current_room == lounge and direction == 'north':
		print("The door to the kitchen is locked.")

	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f'You go {direction}.')
	else:
		print("You can't go that way.")


def main():
	start()

if __name__ == '__main__':
	main()