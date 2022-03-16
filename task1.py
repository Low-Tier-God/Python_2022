from adventurelib import *

@when("brush teeth")
@when("brush")
@when("clean teeth")
def brush_teeth():
	print("You brush your teeth")

@when("comb hair")
@when("comb")
def comb_hair():
	say("""
		You brush your long flowing locks with 
		the gold hairbrush that you have selected from the 
		in the red basket
		""")

def main():
	start()

if __name__ == '__main__':
	main()