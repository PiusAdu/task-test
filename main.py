from random import choice
done = False
print("WELCOME TO ROCK, PAPER, SCISSORS")
print("---------------------------------")
print("Rules: Rock beats Scissors, Paper beats Rock and Scissors beats Paper")
print("_______________________________________________________________________")
all_choice = ("Rock", "Paper", "Scissors")
CPU_score = 0
user_score = 0
while not done:
    choice_made = None
    CPU_choice = choice(all_choice)
    user_input = input("Enter R as Rock, P as Paper, S as Scissors: ")
    if user_input == "R":
        user_choice = "Rock"
        choice_made = "valid"
    elif user_input == "P":
        user_choice = "Paper"
        choice_made = "valid"
    elif user_input == "S":
        user_choice = "Scissors"
        choice_made = "valid"
    else:
        print("Error, input again")
    if choice_made == "valid":
        print(f"CPU({CPU_choice}), Player({user_choice})")
        if user_choice == CPU_choice:
            print("it's a tie!!!")
        else:
            if user_choice == "Rock":
                if CPU_choice == "Paper": 
                    print("CPU wins")
                    CPU_score += 1
                else:
                    print("you win")
                    user_score += 1
            if user_choice == "Paper":
                if CPU_choice == "Scissors":
                    print("CPU wins")
                    CPU_score += 1
                else:
                    print("you win")
                    user_score += 1
            if user_choice == "Scissors":
                if CPU_choice == "Rock":
                    print("CPU wins")
                    CPU_score += 1
                else:
                    print("you win")
                    user_score += 1
        print(f"Current Score: CPU = {CPU_score}, Player = {user_score}")
    if user_score == 1:
        print("WINNER")
        break
    if CPU_score == 1:
        print("YOU LOSE")
        break
print("Game Over")
print(f"Final Score: CPU({CPU_score}), Player({user_score})")
