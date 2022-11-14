# variables
# comparison operators
# if-else statement
import time

print()
print ('''
█████████████████████████████████████████████████████████████
█▄─▄███▄─▄▄─█─▄─▄─█░█─▄▄▄▄███▄─▄▄─█▄─▄████▀▄─██▄─█─▄████▀▄─██
██─██▀██─▄█▀███─███▄█▄▄▄▄─████─▄▄▄██─██▀██─▀─███▄─▄█████─▀─██
▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▄▄▀▀▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▀▀▄▄▀▄▄▀
████████████████████████
█─▄▄▄─█▄─██─▄█▄─▄█░▄▄░▄█
█─██▀─██─██─███─███▀▄█▀█
▀───▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀
''')
print()

play = input("Do you want to play the quiz? (yes/no) ")

# option to start the game or not based on input of user
if play != "yes":
    print("That's too bad...")
    quit()
    

time.sleep(1) # to delay appearance of text
print("Alright! Let's play!")
score = 0 #to record the score of the user

time.sleep(1)
answer = input("What year was Python developed? ") #question 1 with input answer
if answer == "1991":
    print("Nice! You got it correct!")
    score += 1 # plus one point to the user if user answer correct
else:
    print("Oh you got it incorrect") # display this print function if it is wrong answer

time.sleep(1)
answer = input("Yes or No: Is the coding language Python, named after a pie? ")
if answer == "No":
    print("Nice! You got it correct!")
    score += 1
else:
    print("Oh you got it incorrect")

time.sleep(1)
answer = input("True or False: Can Python runs on all major platforms such as Windows, Mac, and Linux? ")
if answer == "True":
    print("Nice! You got it correct!")
    score += 1
else:
    print("Oh you got it incorrect")

time.sleep(1)
answer = input("True or False: Google, Netflix, and Facebook used Python in developing their front-end and back-end web development. ")
if answer == "True":
    print("Nice! You got it correct!")
    score += 1
else:
    print("Oh you got it incorrect")

time.sleep(1)
answer = input("True or False: Python is not a free and open source programming language. ")
if answer == "False":
    print("Nice! You got it correct!")
    score += 1
else:
    print("Oh you got it incorrect")

time.sleep(1)
answer = input("What is the process of identifying and removing errors within a coding program? ")
if answer == "debugging":
    print("Nice! You got it correct!")
    score += 1
else:
    print("Oh you got it incorrect")

time.sleep(1)
answer = input("This 'blank' is used to store data in the memory. It is also considered as a container that holds data that can be changed later in the program. ")
if answer == "variable":
    print("Nice! You got it correct!")
    score += 1
else:
    print("Oh you got it incorrect")

time.sleep(1)
answer = input("This 'blank' is a type of variable whose value cannot be changed. ")
if answer == "constants":
    print("Nice! You got it correct!")
    score += 1
else:
    print("Oh you got it incorrect")

time.sleep(1)
answer = input("What function does accepts the user's input? ")
if answer == "input":
    print("Nice! You got it correct!")
    score += 1
else:
    print("Oh you got it incorrect")

time.sleep(1)
answer = input("These 'blank' is considered as the reserved words in Python. ")
if answer == "keywords":
    print("Nice! You got it correct!")
    score += 1
else:
    print("Oh you got it incorrect")

time.sleep(1)
answer = input("Bonus question: Do you have what it takes to become a successful full stack web developer? (Yes/No) ")
if answer == "Yes":
    print("Nice! One day you will become successful! Keep on grinding!")
    score += 1
else:
    print("You got to believe in yourself!")

# display the total correct answers to the user
# f string and curly brackets
time.sleep(1)
print()
print(f"Hey! You got {score} questions correct out of 11! Thanks for Playing!")
print()