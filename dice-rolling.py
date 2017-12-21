import random

option = "Y"
while not option.lower() == "n":
	min = 1
	max = 6
	answer = random.randint(min,max)
	print(answer)
	option = input("Would you like to roll again? (Y/N) :")