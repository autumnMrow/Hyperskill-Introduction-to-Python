# greet the user and concatenate user inputs in resulting outputs
def greet(bot_name, birth_year):
    print('Hiii, Im ' + bot_name + '. An early Hyperskill project by Autumn Nutini.')
    print('I was created in ' + birth_year + '.')

# greet the user and concatenate user inputs in resulting outputs
def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')

# algorithm to get the users age given a set of inputs
def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")

def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0

    while curr <= num:
        print(curr, '!')
        curr = curr + 1

# Asks the user a question
def test():
    print("""Let's test your programming knowledge.
    Why do we use methods?
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.
""")
    
# User enters integer and and loops until correct
    answer = int(input())
    while answer != 2:
        print("Please, try again.")
        answer = int(input())

# visual response to user before exit program
def end():
    print('Congratulations, have a nice day!')

greet('auDumb🍂Bot', 'June 2023 :D')
remind_name()
guess_age()
count()
test()
end()
