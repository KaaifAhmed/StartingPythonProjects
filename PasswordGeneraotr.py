import random as rd
import string as st

alpha = st.ascii_letters

symb = input('Do you want to include symbols?(Yes/No) : ').lower()
lent = input('What should be the required length of the password? : ')
passwrd = ''
smbol = 0

if symb == 'yes':
    smbol = '~`! @#$%^&*()_-+={[}]|\:;"<,>.?/'

for i in range(int(lent)):
    o = rd.randint(0, 2)

    if smbol != 0:
        if o == 1:
            p = rd.choice(alpha)
        elif o == 2:
            p = rd.choice(smbol)
        else:
            p = rd.randint(1, 9)
    else:
        if o == 1:
            p = rd.choice(alpha)
        else:
            p = rd.randint(1, 9)

    passwrd = passwrd + str(p)


print(passwrd)
