from adventurelib import *



space = Room("""
	You are drifting in space. It feels very cold.
	A slate-blue spaceship sits completely silently in front of you,
	its spaceship open and waiting
	""")

spaceship = Room("""
	The bridge of the spaceship is shiny and white, with thousands 
	of small, red, blinking lights, to your left is the hallway, and the quarters are forward
	""")

cargo = Room("""
	You enter the cargo room. There are thousands of storage
	boxes holding all kinds of resources, to the left is the docking room""")

docking = Room("""
	The docking room is completely empty, with a ton of tempting buttons to press
	the cargo room is now to your right""")

hallway = Room("""
	Upon entering the hallway, it is brightened by hundreds of lights to illuminate your path,
	your available options here is back to the spaceship, to the bridge or the mess hall""")

bridge = Room("""
	Despite there being no reason to enter the bridge compartment, you enter anyway
	There's nothing except a locked bridge entry way, the escape pods are forward from your position""")

quarters = Room("""
	The quarters are filled with beds and drawers of your fellow crewmates,
	the spaceship room is behind you and the mess hall sits to your left""")

mess_hall = Room("""
	At the table are your fellow crewmates, though they don't look interested in conversing,
	the hallway is behind you and the quarters are to your right""")

escape_pods = Room("""
	Why are you here? Do you seriously plan on escaping? Turn back to the bridge""")


spaceship.east = hallway
spaceship.south = quarters
hallway.east == bridge
hallway.north = cargo
hallway.west == spaceship
cargo.east == docking
hallway.south == mess_hall
bridge.south == escape_pods
mess_hall.west == quarters


#variables

current_room = space
print(current_room)

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


@when("go DIRECTION")
def travel(direction):
	pass
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(current_room)
		print(current_room.exits())


def main():
	start()

if __name__ == '__main__':
	main()