from flask import Flask, request, render_template
import re

cal_app = Flask(__name__)
equation = []
visual = []


@cal_app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@cal_app.route('/calculate', methods=['POST'])
def calc():
    result = ''
    if request.method == 'POST':
        if request.form['btn'] == '1':
            equation.append('1')
            visual.append('1')
        elif request.form['btn'] == '2':
            equation.append('2')
            visual.append('2')
        elif request.form['btn'] == '3':
            equation.append('3')
            visual.append('3')
        elif request.form['btn'] == '4':
            equation.append('4')
            visual.append('4')
        elif request.form['btn'] == '5':
            equation.append('5')
            visual.append('5')
        elif request.form['btn'] == '6':
            equation.append('6')
            visual.append('6')
        elif request.form['btn'] == '7':
            equation.append('7')
            visual.append('7')
        elif request.form['btn'] == '8':
            equation.append('8')
            visual.append('8')
        elif request.form['btn'] == '9':
            equation.append('9')
            visual.append('9')
        elif request.form['btn'] == '0':
            if len(equation) != 0:
                if equation[-1] not in '+-*/√':
                    equation.append('0')
                    visual.append('0')
        elif request.form['btn'] == '+':
            if len(equation) != 0:
                if equation[-1].isdigit():
                    equation.append('+')
                    visual.append('+')
        elif request.form['btn'] == '-':
            if len(equation) != 0:
                if equation[-1].isdigit():
                    equation.append('-')
                    visual.append('-')
        elif request.form['btn'] == '/':
            if len(equation) != 0:
                if equation[-1].isdigit():
                    equation.append('/')
                    visual.append('/')
        elif request.form['btn'] == '*':
            if len(equation) != 0:
                if equation[-1].isdigit():
                    equation.append('*')
                    visual.append('*')
        elif request.form['btn'] == '√':
            if len(equation) != 0:
                if equation[-1].isdigit():
                    equation.append('**0.5')
                    visual.append('√')
        elif request.form['btn'] == '=':
            result = ''.join(equation)
            if len(result) != 0:
                result = eval(result)
            # equation.append('=')
        elif request.form['btn'] == 'C':
            equation.clear()
            visual.clear()
        elif request.form['btn'] == 'CE':
            equation.clear()
            visual.clear()
        elif request.form['btn'] == '.':
            strr = ''.join(equation)
            lst = re.split('[+*\-√/]', strr)
            ret = '.' not in lst[-1]
            if equation.count('.') < 1:
                equation.append('.')
                visual.append('.')
            elif ret:
                equation.append('.')
                visual.append('.')
        elif request.form['btn'] == 'x':
            if len(equation) != 0:
                equation.pop(-1)
                visual.pop(-1)

    # eqt = ''.join(equation)
    eqt = ''.join(visual)

    if len(str(result)) == 0:
        return render_template('home.html', eq=eqt)
    else:
        return render_template('home.html', answer=result)


if __name__ == "__main__":
    cal_app.run(debug=True)
