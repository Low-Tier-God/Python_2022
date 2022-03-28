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
	The electricity station outside is making a loud buzzing noise, you open the door but quickly shut it upon hearing crunching leaves behind you.
	You look outside and realize it was only the wind,
	There is plugs and a dead battery, maybe try swapping the dead battery with the one you found?""")

basement = room("""
	You go down the flight of stairs leading to the basement, when you reach the bottom you hear footsteps above the basement
	...
	You hear a laugh, the basement door slams shut,
	You climb back up, desperately trying to lift the door, but it's stuck for good.
	You look for any tools that might help, but it's empty, and too dark to see anything.
	You realize that you've just fallen into a trap and you will be spending your last few days down here.
	Sucks to be you.""")

outside.north = main_hall
main_hall.east = bathroom
main_hall.west = second_hall
main_hall.north = lounge
lounge.north = kitchen
second_hall.north = bedroom
outside.east = radio_tower
second_hall.basement = basement


#define items go here
Item.description = ""

knife = Item("a dirty knife","knife")
knife.description = "the knife has a dull sheen to it but it looks rather sharp."

silver_key = Item("silver key","a silver key","the silver key","skey")
silver_key.description = "the key shines faintly, it has a rough, metallic feeling. You put it back in your pocket."

gold_key = Item("gold key","a gold key","the gold key","gkey","key")
gold_key.description = "the key feels smooth feeling, althought it is scratched and rusted in sode places. You put it back in your pocket."



#define bags go here


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

#current room you start in when starting the code

@when("enter inside")
@when("enter house")
@when("enter hall")
def enter_house():
	global current_room
	if current_room is not outside:
		say("There is no house here")
		return
	else:
		current_room = main_hall
		say("""You swing open the door and immediately feel your hand across the wall to find a light switch.
			The wallpaper is smooth, and you find the switch, upon flicking the light on, you are met with a dim light with an audible buzzing sound.
			""")
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