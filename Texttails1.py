import time

chk = False
snkfill = False
dintact = False

def start():
	cont = False
	while cont == False:
		opt1 = input("observe the room? [y/n]: ")
		if opt1 == "y":
			level_1_init()
			cont = True
		elif opt1 == "n":
			print("you've decided to accept your fate")
			boom()
			cont = True
		else:
			print("invalid input")


def level_1_init():
	print("looking around the room you see a chair and table, a ceiling light in the middle of the room")
	print("on one wall there is a utility sink and a shelf with many boxes on it")
	lvl_1_choice()


def boom ():
	countdown = 3
	while countdown > 0:
		print(countdown)
		time.sleep(1)
		countdown = countdown - 1
	print("B O O M")
	exit()


def lvl_1_choice():
	cont = True
	while cont == True:
		opt2 = input("what's your action? [goto table/goto shelf/try door]: ")
		if opt2 == "goto table":
			print("you walk over to the table and find a puzzlepiece set, its almost done but is missing one piece, however there are three puzzle pieces on the table")
			cont = False
			lvl_2a_choice()
		elif opt2 == "goto shelf":
			print("you walk to the shelf and notice some devices in one of the boxes, the utility sinks drain is plugged")
			cont = False
			lvl_2b_choice()
		elif opt2 == "try door":
			if dintact == True:
				print("you open the door... and no explosion, your free!!!")
				cont = False
				win()
			else:
				cont = False
				boom()
		else:
			print("invalid input")

def lvl_2a_choice():
	cont = True
	while cont == True:
		opt3 = input("what will you do? [obsv puzzle/sit chair]: ")
		if opt3 == "obsv puzzle":
			cont = False
			puzzle()
		elif opt3 == "sit chair":
			print("you decide to rest your feet and sit down for a while")
			boom()
			cont = False
		else:
			print("invalid input")

def puzzle():
	print("you look at the puzzle, its some kind of industrial scene, the missing puzzlepiece seems to be on one of the brick smokestacks")
	cont = False
	global chk
	while cont == False:
		opt4 = input("looking at the 3 pieces, which one will you choose? [red/blue/yellow]: ")
		if opt4 == "red":
			chk = True
			correct_piece()
			cont = True
		elif opt4 == "blue":
			boom()
			cont = True
		elif opt4 == "yellow":
			boom()
			cont = True
		else:
			print("invalid input")

def lvl_2b_choice():
	global chk
	cont = False
	if chk == True:
		while cont == False:
			opt5 = input("what is your choice? [goto sink/goto shelf]: ")
			if opt5 == "goto sink":
				print("you go over to the sink")
				lvl_3a_choice()
				cont = True
			elif opt5 == "goto shelf":
				print("you go to the shelf and look inside one of the boxes")
				print("there is a device in the box you look in, it looks like some kind of transmitter device with some buttons on it, does this control the bomb?")
				lvl_2c_choice()
				cont = True
			else:
				print("invalid input")
	else:
		print("you suddenly get a feeling that your missing something, which is awfully convenient, you go back")
		lvl_1_choice()

def lvl_3a_choice():
	print("you look inside the sink and find nothing but the drain plug, the faucet is dripping slightly with water")
	sink_choice()


def lvl_2c_choice():
	cont = False
	while cont == False:
		opt6 = input("what will you do? [inspect device/go back]: ")
		if opt6 == "inspect device":
			print("you pick up the device and inspect it, there are buttons but they are all unlabeled")
			device_choice()
			cont = True
		elif opt6 == "go back":
			print("you go back")
			lvl_2b_choice()
			cont = True
		else:
			print("invalid input")

def device_choice():
	cont = False
	while cont == False:
		opt7 = input("what will you do with the device? [press buttons/break it open]: ")
		if opt7 == "press buttons":
			print("you press the buttons on the device")
			buttons_pressed()
			cont = True
		elif opt7 == "break it open":
			boom()

def buttons_pressed():
	global snkfill
	print("the device seems to turn off")
	print("well it seems to be off, but you cant be sure if it truly is, how can you make sure it doesnt work?")
	drown_device()

def correct_piece():
	print("you put the correct piece in the puzzle and step away from the table")
	global chk
	chk = True
	lvl_1_choice()

def sink_choice():
	cont = False
	while cont == False:
		global snkfill
		opt8 = input("what will you do? [fill sink/feel around drain/pour water on bomb]: ")
		if opt8 == "fill sink":
			print("you fill the sink with water")
			snkfill = True
			lvl_2b_choice()
		elif opt8 == "feel around drain":
			print("you unplug the drain and feel around inside to see if there is anything of interest, you eventually feel some kind of switch")
			cont = True
			boom()
		elif opt8 == "pour water on bomb":
			print("in hindsight that was kinda stupid")
			cont = True
			boom()
		else:
			print("invalid input")
def drown_device():
	cont = False
	global snkfill
	while cont == False:
		global dintact
		opt9 = input("how can you make sure the device is off? [put it sink/stomp on it/do nothing]: ")
		if opt9 == "put in sink":
			if snkfill == True:
				print("you throw the device in the water of the sink and nothing happens")
				lvl_1_choice()
			else:
				print("there is no water in the sink")
				lvl_1_choice()
		elif opt9 == "stomp on it":
			print("you stomp down on the device, and nothing happens")
		elif opt9 == "do nothing":
			print("you set the device down and leave it be")
			dintact = True
			cont = True
			lvl_1_choice()

def win():
	print("#     #                  #     #                         #     #                 ######                  ### ")
	print(" #   #   ####  #    #    #     #   ##   #    # ######    ##    #  ####  #####    #     # # ###### #####  ###")
	print("  # #   #    # #    #    #     #  #  #  #    # #         # #   # #    #   #      #     # # #      #    # ###")
	print("   #    #    # #    #    ####### #    # #    # #####     #  #  # #    #   #      #     # # #####  #    #  # ")
	print("   #    #    # #    #    #     # ###### #    # #         #   # # #    #   #      #     # # #      #    #     ")
	print("   #    #    # #    #    #     # #    #  #  #  #         #    ## #    #   #      #     # # #      #    # ### ")
	print("   #     ####   ####     #     # #    #   ##   ######    #     #  ####    #      ######  # ###### #####  ### ")
	print("thanks for playing!")

print("                                                      ")
time.sleep(0.3)
print("    &                    &                              ")
time.sleep(0.3)
print("   / \                  / \                               ")
time.sleep(0.3)
print(" _/___\_        _     _/___\_    _ _               ____")
time.sleep(0.3)
print("|__   __|      | |   |__   __|  (_) |         ____/####|")
time.sleep(0.3)
print("   | | _____  _| |_     | | __ _ _| |___    _/    ####/")
time.sleep(0.3)
print("   | |/ _ \ \ / / __|   | |/ _` | | / __|  /   ______/")
time.sleep(0.3)
print("   | |  __/>  <| |_     | | (_| | | \__ \_/   /")
time.sleep(0.3)
print("   |_|\___/_/\_\___|    |_|\__,_|_|_|___/___/")

begin = input("you ready to start? [yes]: ")
if begin == "yes":
	print("you wake up in a room, a room that would otherwise be ordinary if not for the large explosive sitting in the middle of this room, the door seems to be rigged to detonate the bomb when opened, you will need to find a way to disarm the bomb")
	start()
else:
	pass



