import random

target = random.randint(1,100)
while True:
	guess = int(input("Guess a number?: "))
	if guess == target:
		print("Well done! The number was ",target,".")
		break
	elif guess > target:
		print("Your guess was too high!")
	elif guess < target:
		print("Your guess was too low!")