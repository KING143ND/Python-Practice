import random
from collections import Counter
from playsound import playsound

Players ='''rohit rahul shikhar virat ishan shubhman rituraj venkatesh deepak shreyas surya rishabh hardik ravindra dinesh akshar bhuvaneshwar jasprit shami shardul siraj washington ravichandran umran arshdeep avesh sanju kuldeep yuzvendra ravi harshal'''

Players = Players.split(" ")
word = random.choice(Players)

print("Welcome To Word Guess Game")

for i in word:
	print("_", end = " ")	


playing = True
letterGuessed = ""			
chances = len(word) + 2
correct = 0
flag = 0


while (chances != 0) and flag == 0:
	chances -= 1
	print(f"Now..You have {chances+1} Chances left!")
	try:
		guess = str(input("\nEnter a letter to guess: "))
	except:
		print("Enter only a letter!")
		continue

	if not guess.isalpha():
		print("Please! Enter only a Letter...")
		continue
	elif not guess.islower():
		print("Please! Enter only a Lowecase Letter...")
		continue
	elif len(guess) > 1:
		print("Please! Enter only a Single Letter...")
		continue
	elif guess in letterGuessed:
		print("You have Already Guessed that Letter... Please! Enter New Letter.")
		continue

	if guess in word:
		print("Your Guessed Letter is Correct, Please! Enter New Letter All the Best...")
		k = word.count(guess)
		for _ in range(k):
			letterGuessed += guess
	for char in word:
				if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
					print(char, end = ' ')
					correct += 1
				elif (Counter(letterGuessed) == Counter(word)):
					print(f"The word is: {word}")
					flag = 1
					print("\n***********************************\n***********************************\n***********************************\n*** Congratulations... You won! ***\n***********************************\n***********************************\n***********************************\n")
					playsound("A:/MY PYTHON PROJECTS/Won.mp3")
					break
					
				else:
					print("_", end = " ")

if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
			print()
			print("You lost! Try again..")
			print(f"The word was {format(word)}")
			playsound("A:/MY PYTHON PROJECTS/Lost.mp3")
			

