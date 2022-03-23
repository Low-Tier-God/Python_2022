from adventurelib import *
Room.items = Bag()


space = Room("""
	You are drifting in space. It feels very cold.
	A slate-blue spaceship sits completely silently in front of you,
	its spaceship open and waiting""")

spaceship = Room("""
	The bridge of the spaceship is shiny and white, with thousands 
	of small, red, blinking lights, to your east is the hallway, and the quarters are to the south""")

cargo = Room("""
	You enter the cargo room. There are thousands of storage
	boxes holding all kinds of resources, to the east is the docking room""")

docking = Room("""
	The docking room is completely empty, with a ton of tempting buttons to press
	the cargo room is now to your west""")

hallway = Room("""
	Upon entering the hallway, it is brightened by hundreds of lights to illuminate your path,
	your available options here is back to the spaceship, the cargo room, to the bridge or the mess hall""")

bridge = Room("""
	Despite there being no reason to enter the bridge compartment, you enter anyway
	There's nothing except a locked bridge entry way, the escape pods are south from your position""")

quarters = Room("""
	The quarters are filled with beds and drawers of your fellow crewmates,
	the spaceship room is north from you and the mess hall is to your east""")

mess_hall = Room("""
	At the table are your fellow crewmates, though they don't look interested in conversing,
	the hallway is north from you and the quarters are to your west""")

escape_pods = Room("""
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
docking.items.add(green)keycard
quarters.items.add(blue_keycard)

#adding items to bags code goes here

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