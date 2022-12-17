import numpy as np
from flask import Flask, request, render_template


rps_app = Flask(__name__)
total_user_points = []
total_comp_points = []


@rps_app.route('/', methods=['GET'])
def home():
    # num = float(request.form['for_exponent'])
    return render_template('index.html')


@rps_app.route('/quit', methods=['GET'])
def quit():
    # if request.method == 'POST':
    #     quit()

    total_user = sum(total_user_points)
    total_comp = sum(total_comp_points)
    total_points = f'Your points {total_user}, Computer Points {total_comp}'
    return render_template('quit.html', points=total_points)

    # else:
    #     return render_template('index.html')


@rps_app.route('/predict', methods=['POST'])
def rps():
    if request.method == 'POST':
        choices = ["rock", "paper", "scissor"]
        user_points = 0
        comp_points = 0

        # while True:
        comp_num = np.random.randint(0, 3)
        comp_choice = choices[comp_num]

        if request.form['btn'] == 'rock':
            opt = 'rock'
        elif request.form['btn'] == 'paper':
            opt = 'paper'
        else:
            opt = 'scissor'

        user_choice = opt.lower()

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

        total_user_points.append(user_points)
        total_comp_points.append(comp_points)

        if user_points > comp_points:
            result = 'You Won'
        elif user_points == comp_points:
            result = 'Draw'
        elif user_points == 0 and comp_points == 0:
            result = 'No matches played'
        else:
            result = 'You lost'
        # return result, user_points, comp_points
        resullt = f'{result} \n Your Score {user_points} \n Computer score {comp_points}'
        return render_template('index.html', answer=resullt)

    else:
        return render_template('index.html')

# ans = rps('rock')
# print(ans)


if __name__ == "__main__":
    rps_app.run(debug=True)
