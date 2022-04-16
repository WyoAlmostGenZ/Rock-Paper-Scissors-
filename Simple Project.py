import random

rock_emoji = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_emoji = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_emoji = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock = rock_emoji
rock_txt = "rock"

paper = paper_emoji
paper_txt = "paper"

scissors = scissors_emoji
scissors_txt = "scissors"

rockpaperscissors = [rock_txt, paper_txt, scissors_txt]

cpu_random = random.choice(rockpaperscissors)

my_choice = input("What do u choose: \nrock\npaper\nscissors\n").lower()



if my_choice == "rock":
	print(rock_emoji)
	if cpu_random == "paper":
		print(paper_emoji)
		print("Lose")
	elif cpu_random == "scissors":
		print(scissors_emoji)
		print("Winner")
	else:
		print(rock_emoji)
		print("Tie")

if my_choice == "paper":
	print(paper_emoji)
	if cpu_random == "paper":
		print(paper_emoji)
		print("Tie")
	elif cpu_random == "scissors":
		print(scissors_emoji)
		print("Lose")
	else:
		print(rock_emoji)
		print("Winner")

if my_choice == "scissors":
	print(scissors_emoji)
	if cpu_random == "scissors":
		print(scissors_emoji)
		print("Tie")
	elif cpu_random == "paper":
		print(paper_emoji)
		print("Win ")
	else:
		print(rock_emoji)
		print("You Lose")
else:
	print("type proper u baboon")
