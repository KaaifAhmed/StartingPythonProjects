import random


no_of_choices = input('How many choices do you have? : ')
choices = []

for i in range(int(no_of_choices)):
    choice = input(f'Enter choice # {i + 1} ')
    choices.append(choice)

selected_choice = random.choice(choices)
print(selected_choice)
