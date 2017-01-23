
# The first text displayed on the screen after running a program and it explains player how to choose a level:
first_text = '''
Choose a level of the game:
1 - easy
2 - medium
3 - hard
4 - end game

'''
# The text for level 1 (easy):
level_1 = '''
Level 1: Who is who in fairytales?

Every sentence is related to another farytail. Guess the missing names! 

___1___ lost one of her glass slippers when she was running home from the ball.

___2___ took a bite of a poisoned apple and fell down unconscious.

___3___ was sleeping until her true love came and kissed her.

___4___ had very long golden hair and she was shut in a tower with neither stairs nor a door.
_____________________________________________________________________________________________

'''
# The list of correct answers for the level 1:
answers_1 = ['Cinderella', 'Snow White', 'Sleeping Beauty', 'Rapunzel']

# The text for level 2 (medium):
level_2 = '''
Level 2: Capital cities

Guess the right capital city or the right country!

___1___ is the capital of France.

Ankara is the capital of ___2___.

___3___ is the capital of Austria.

___4___ is the capital of United Kingdom.

Moscow is the capital of ___5___.
___________________________________________________

'''
# The list of correct answers for the level 2:
answers_2 = ['Paris', 'Turkey', 'Vienna', 'London', 'Russia']

# The text for level 3 (hard):
level_3 = '''
Level 3:  Intro to programming

Guess the missing words!

Python is not only a snake but also a Programming ___1___.

In Python a variable is a Name that refers to a ___2___.

A ___3___ is a sequence of characters surrounded by quotes.

A function takes in Inputs, does some processing, and produces ___4___.

In an if statement, the code runs only if the value of the test 
expression is ___5___ and not more then once.

A ___6___ Loop executes any number of times, continuing as long 
as the test expression is True.
________________________________________________________________________

'''
# The list of correct answers for the level 3:
answers_3 = ['Language', 'Value', 'String', 'Outputs', 'True', 'While']

# A list of level texts:
list_of_levels = [level_1, level_2, level_3]
# A list of answer lists:
lists_of_answers = [answers_1, answers_2, answers_3]

# This function takes an integer as input and returnes the relevant level text. 
# The integer represents the game level and the player enters it at the begining of the game:
def choose_level_text(level_number):
	return list_of_levels[int(level_number) - 1]

# This function takes an integer as input and returnes the list of answers 
# that belong to the level that is represented by the integer 
# (it is the same number as in the previous function):
def choose_answers(level_number):
	return lists_of_answers[int(level_number) - 1]

# This function plays one level of the game. The code is universal for all three levels. 
# It takes as inputs a string level_text (the text that belongs to the level) 
# and a list of answers that belong to the level:
def play_level(level_text, answers):
	# print the level text so that the player could see the task
	print level_text
	# this variable represents the number of a blank space 
	number = 1 
	while number <= len(answers):
		#the player is asked to enter the answer
		user_input = raw_input("What should go in blank number " + str(number) + "? ")
		# evaluate whether his answer is correct.  
		if user_input.title() == answers[number - 1]:
			# choose the relevant blank space 
			to_replace = '___' + str(number) + '___'
			# the blank space is replaced with the correct answer 
			level_text = level_text.replace(to_replace, answers[number - 1])
			# the player is shown how it looks replaced 
			print level_text
			# and we add 1 to the variable number so that the player could be 
			# asked to guess following word
			number = number + 1 
		else: 
			print 'Try again!'

	print 'CONGRATULATIONS!!! You mastered this level!'
	play_game()


# This function plays the whole game. It has no inputs and it returns the function 
# that runs the choosen level.
def play_game():
	# print the introduction text firstly
	print first_text
	# ask the player to enter a number representing the game level 
	user_input = raw_input("Enter number: " )
	if int(user_input) < 4:
		# call the function for choosing the right level text 
		level_text = choose_level_text(user_input)
		# call the function for choosing the right list of answers 
		answers = choose_answers(user_input)
		# return the code that runs the choosen level
		return play_level(level_text, answers)
	else:
		return end_game()

def end_game():
	print 'You have quit the game. Run the module again, if you want to play again.'


play_game()

