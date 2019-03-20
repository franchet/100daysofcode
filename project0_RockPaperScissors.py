# Day 0 of my 100 Days of Code Challenge
# Today I will make a rock, paper, scissors game in Python

import random  # import random for cpu random guess
import time  # import time to pause between each round etc...

cpu_score = 0  # init variable to store cpu's score
user_score = 0  # init variable to store player's score
user_guess = None  # init variable to user's guess
user_name = input("What is your name?: ")  # collects the user's name
winning_score = int(input("How many rounds do you want to play?: "))

while user_score < winning_score and cpu_score < winning_score:
    cpu_guess = random.choice(["rock", "paper", "scissors"])
    user_guess = input("Rock, paper or scissors: ")
    time.sleep(1)
    if user_guess == cpu_guess:
        print(f"You played {user_guess} and the computer played {cpu_guess}")
        print("It's a tie, Try again ...")
        print(f"the scores are {user_name}: {user_score} and Cpu: {cpu_score}")
    elif user_guess == "rock" and cpu_guess == "paper":
        print(f"You played {user_guess} and the computer played {cpu_guess}")
        print("Paper covers Rock, you lose! Try again ...")
        cpu_score += 1
        print(f"the scores are {user_name}: {user_score} and Cpu: {cpu_score}")
    elif user_guess == "rock" and cpu_guess == "scissors":
        print(f"You played {user_guess} and the computer played {cpu_guess}")
        print("Rock breaks Scissors, you win! Let's play again ...")
        user_score += 1
        print(f"the scores are {user_name}: {user_score} and Cpu: {cpu_score}")
    elif user_guess == "paper" and cpu_guess == "rock":
        print(f"You played {user_guess} and the computer played {cpu_guess}")
        print("Paper covers Rock, you win! Let's play again ...")
        user_score += 1
        print(f"the scores are {user_name}: {user_score} and Cpu: {cpu_score}")
    elif user_guess == "paper" and user_guess == "scissors":
        print(f"You played {user_guess} and the computer played {cpu_guess}")
        print("Scissors cuts Paper, you lose! Try again ...")
        cpu_score += 1
        print(f"the scores are {user_name}: {user_score} and Cpu: {cpu_score}")
    elif user_guess == "scissors" and cpu_guess == "rock":
        print(f"You played {user_guess} and the computer played {cpu_guess}")
        print("Rock breaks scissors, you lose! Try again ...")
        cpu_score += 1
        print(f"the scores are {user_name}: {user_score} and Cpu: {cpu_score}")
    elif user_guess == "scissors" and cpu_guess == "paper":
        print(f"You played {user_guess} and the computer played {cpu_guess}")
        print("Scissors cuts paper, you win! Let's play again ...")
        user_score += 1
        print(f"the scores are {user_name}: {user_score} and Cpu:{cpu_score}")


print(f"The final scores are {user_name}: {user_score} and CPU: {cpu_score}")
if user_score > cpu_score:
    print(f"{user_name} Wins That Round. Man is greater than Machine.")
elif user_score == cpu_score:
    print("There are no winners in this round. You both live to fight another day!.")
else:
    print("The CPU won this round. Machine triumphs over Man!")
