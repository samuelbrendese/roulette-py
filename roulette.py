import random
# n is a random number between 0 - 36 for the roulette board
n = random.randint(0,36)

# Message prompting the user to input the string "start" which will begin the game
startIn = input("Hello. Please type -  start  - and hit enter to start: \n")

# Converts input string to lowercase for validation.
start = startIn.lower()

# If the input does not convert to "start", then the game will not begin
if start != "start":
    print("Incorrect input, please try again")

# Remaining if statements determine if the resulting number is red or black
if n % 2 == 0 and (n > 0 and n < 11):
	print ("Your number was: %d Black" % (n))


if n % 2 == 1 and (n > 0 and n < 11):
	print("Your number was: %d Red" % (n))


if n % 2 == 0 and (n > 18 and n < 29):
	print("Your number was: %d Black" % (n))


if n % 2 == 1 and (n > 18 and n < 29):
	print("Your number was: %d Red" % (n))


if n % 2 == 0 and (n > 10 and n < 19):
	print("Your number was: %d Red" % (n))


if n % 2 == 1 and (n > 10 and n < 19):
	print("Your number was: %d Black" % (n))


if n % 2 == 0 and (n > 28 and n < 37):
	print("Your number was: %d Red" % (n))


if n % 2 == 1 and (n > 28 and n < 37):
	print("Your number was: %d Black" % (n))


if n == 0:
	print("Your number was: %d green" % (n))

# Ending statement before program closes
print("Thank you for playing!")