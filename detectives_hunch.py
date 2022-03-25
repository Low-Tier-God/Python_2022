from adventurelib import *
Room.items = Bag()


outside = Room("""
	You stand outside, in front of you is a house that seems to be abandoned, a radio tower next to it.
	Your only choice is to investigate the house in the hopes of finding something that can turn on the radio tower.
	The porch you stand on creaks""")


main_hall = Room("""
	You now stand in the hallway, you can hear rodents running across the board, it is dark.
	You feel adrenaline from fear pumping inside you, and you feel like you are being watched.
	The feeling to run away is looming over you.""")

lounge = Room("""
	You stand in the lounge, unable to collect your thoughts, you hear an eerie noise with an unknown location.
	You can hear your teeth chattering, it's very cold inside.""")

kitchen = Room("""
	The docking room is completely empty, with a ton of tempting buttons to press
	the cargo room is now to your west""")

second_hall = Room("""
	Upon entering the hallway, it is brightened by hundreds of lights to illuminate your path,
	your available options here is back to the spaceship, the cargo room, to the bridge or the mess hall""")

bedroom = Room("""
	Despite there being no reason to enter the bridge compartment, you enter anyway
	There's nothing except a locked bridge entry way, the escape pods are south from your position""")

bathroom = Room("""
	The quarters are filled with beds and drawers of your fellow crewmates,
	the spaceship room is north from you and the mess hall is to your east""")

bathroom = Room("""
	At the table are your fellow crewmates, though they don't look interested in conversing,
	the hallway is north from you and the quarters are to your west""")

radio_tower = Room("""
	Why are you here? Do you seriously plan on escaping? Turn back to the bridge""")

hallway.north = cargo
hallway.east = bridge
hallway.south = mess_hall
hallway.west = spaceship
mess_hall.west = quarters
bridge.south = escape_pods
cargo.east = docking
quarters.north = spaceship


#define items go here
Item.description = ""

knife = Item("a dirty knife","knife")
knife.description = "the knife has a dull sheen to it but it looks rather sharp."

red_keycard = Item("a red keycard","rkeycard","red card","red keycard")
red_keycard.description = "It's a red keycard. It probably opens a door or a locker."

green_keycard = Item("a green keycard","gkeycard","green card","green keycard")
green_keycard.description = "It's a green keycard, It probably opens a door or a locker... or something else?"

blue_keycard = Item("a blue keycard","bkeycard","blue card","blue keycard")
blue_keycard.description = "It's a blue keycard. It probably opens a door or a locker."

#define bags go here
mess_hall.items.add(red_keycard)
cargo.items.add(knife)
docking.items.add(green_keycard)
quarters.items.add(blue_keycard)

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

current_room = space
print(current_room)
inventory = Bag()

#current room you start in when starting the code

@when("enter spaceship")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global current_room
	if current_room is not space:
		say("There is no spaceship here")
		return
	else:
		current_room = spaceship
		say("""You heave yourself into the spaceship and slam your hand on the button to close the door.""")
		print(current_room)

@when("look")
def look():
	print(current_room)
	say("You look around for any possible exits:")
	print(current_room.exits())
	if len(current_room.items) > 0: #if there are any items in the current room
		print("However, you also see:")
		for item in current_room.items:
			print(item)#prints out each items


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

@when("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(current_room)


def main():
	start()

if __name__ == '__main__':
	main()