import random

#generate wordlist
wordlist = ["undergraduate","simulator","adventure"]
index = random.randint(0,len(wordlist)-1)
lives = 3

#generate answer for this round
solution = list(wordlist[index])
master = "".join(solution)
wordlength = len(solution)
display = list("_ " * (wordlength - 1) + "_")
guessed = []

#play game
while "_" in display:
	print("".join(display))
	message = "\nYou have " + str(lives) + " lives. Previously guessed letters were [" + ",".join(guessed)+ "]. Guess a letter!: "
	guess = input(message).lower()
	if len(guess) != 1 or not guess.isalpha():
		print("\nPlease enter a valid guess of only a single letter!")
		continue
	elif guess in guessed:
		print("\nYou have guessed this letter before! Please enter a new guess!")
		continue
	else:
		guessed.append(guess)
	if not guess in solution:
		lives -= 1
		print("\nSorry, that was the wrong letter!")
		if lives == 0:
			print("\nSorry, you ran out of lives. Better luck next time!\nThe word was \"" + master + "\".")
			quit()
	else:
		while guess in solution:
			display[solution.index(guess)*2] = solution[solution.index(guess)]
			solution[solution.index(guess)] = " "

print("\nGreat job, you solved it!\nThe word was \"" + master + "\".")
