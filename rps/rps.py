import random as rd

choices = ["rock", "paper", "scissor"]
user_points = 0
comp_points = 0

while True:
    comp_num = rd.randint(0, 2)
    comp_choice = choices[comp_num]
    user_choice = input("Choose Rock, Paper, Scissor or press Q to quit : ")
    use_choice = user_choice.lower()

    if use_choice.lower() == "q":
        print("Your points", user_points)
        print("Computer's points", comp_points)
        if user_points > comp_points:
            print('You Won')
        elif user_points == 0 and comp_points == 0:
            print('No matches played')
        elif user_points == comp_points:
            print('Draw')
        else:
            print('You lost')
        quit()

    elif "rock" in use_choice or "paper" in use_choice or "scissor" in use_choice:
        if "rock" in use_choice:
            user_choice = "rock"
        elif "paper" in use_choice:
            user_choice = "paper"
        else:
            user_choice = "scissor"
        print('Computer picked : ', comp_choice)

        if user_choice.lower() == comp_choice:
            print("Draw")

        elif user_choice == "rock" and comp_choice == "paper":
            print("Computer got a point")
            comp_points += 1

        elif user_choice == "rock" and comp_choice == "scissor":
            print("You got a point")
            user_points += 1

        elif user_choice == "paper" and comp_choice == "rock":
            print("You got a point")
            user_points += 1

        elif user_choice == "paper" and comp_choice == "scissor":
            print("Computer got a point")
            comp_points += 1

        elif user_choice == "scissor" and comp_choice == "rock":
            print("Computer got a point")
            comp_points += 1

        elif user_choice == "scissor" and comp_choice == "paper":
            print("You got a point")
            user_points += 1

    else:
        print('Please choose rock, paper or scissor next time')
        continue
