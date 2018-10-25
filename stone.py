import random 
while True: 
	print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor") 
	choice = int(input("User turn: ")) 
	while choice > 3 or choice < 1: 
		choice = int(input("enter valid input: ")) 
	if choice == 1: 
		choice_name = 'Rock'
	elif choice == 2: 
		choice_name = 'paper'
	else: 
		choice_name = 'scissor'
	print("Your choice is: " + choice_name) 
	print("Now its computer turn.......") 
	computer_choice = random.randint(1, 3) 
	while computer_choice == choice: 
		computer_choice = random.randint(1, 3) 
	if computer_choice == 1: 
		computer_choice_name = 'Rock'
	elif computer_choice == 2: 
		computer_choice_name = 'paper'
	else: 
		computer_choice_name = 'scissor'
		
	print("Computer choice is: " + computer_choice_name) 

	print(choice_name + " V/s " + computer_choice_name) 

	if((choice == 1 and computer_choice == 2) or
	(choice == 2 and computer_choice ==1 )): 
		print("Paper covers Rocks and Paper wins => ", end = "") 
		result = "Paper"
		
	elif((choice == 1 and computer_choice == 3) or
		(choice == 3 and computer_choice == 1)): 
		print("Rock blunts Scissors and Rock wins ", end = "") 
		result = "Rock"
	else: 
		print("Scissors cut Paper and Scissors wins ", end = "") 
		result = "Scissors"

	if result == choice_name: 
		print("Hurray,You Win!") 
	else: 
		print("Oops,Computer Wins") 
		
	print("Do you want to play again? (Yes/No)") 
	ans = input() 

	if ans == 'no' or ans == 'No': 
		break

print("Thanks for playing the game-Stone Paper Scissors") 

