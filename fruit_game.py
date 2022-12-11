import random
from collections import Counter
from playsound import playsound

Fruits = '''apple, banana, mango, coconut, guava, orange, pineapple, apricot, jackfruit, avocado, papaya, blackberry, blueberry, strawberry, pomegranate, grape, tamarind, gooseberry, lemon, watermelon, cherry, pear, berry, peach, lychee, muskmelon, plum, melon, sugarcane, kiwi, olive, persimmon, raspberry, tomato'''

Fruits = Fruits.split(", ")
word = random.choice(Fruits)		
print("**********  Welcome To Guess The Word Game  **********")
if __name__ == '__main__':
	print("Guess the word! HINT: word is a name of a fruit")
	
	for i in word:
		print("_", end = " ")	
	print()

	playing = True
	letterGuessed = ""			
	chances = len(word) + 2
	correct = 0
	flag = 0

try:
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
			# elif guess in letterGuessed:
			# 	print("Your Guessed Letter is not Present in this Fruit, Please! Enter New Letter All the Best...")
			for char in word:
				if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
					print(char, end = ' ')
					correct += 1
				elif (Counter(letterGuessed) == Counter(word)):
					print(f"The word is: {word}")
					flag = 1
					print("\n***********************************\n***********************************\n***********************************\n*** Congratulations... You won! ***\n***********************************\n***********************************\n***********************************\n")
					playsound("A:\MY PYTHON PROJECTS\Won.mp3")
					break
					
				else:
					print("_", end = " ")

		if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
			print()
			print("You lost! Try again..")
			print(f"The word was {format(word)}")
			playsound("A:\MY PYTHON PROJECTS\Lost.mp3")
			
except KeyboardInterrupt:
	print()
	print("Bye! Try again...")
	exit()
