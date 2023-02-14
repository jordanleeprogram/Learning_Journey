print("Hello, and welcome to the quiz!!!")

player_name = input("Firstly, what is your name?  ")

print("Hello " + player_name)

answer = input("Are you ready to begin? ")

if answer.lower() != "yes":
    print("That's a shame! Maybe next time?")
    quit()

print("Great! Then let's begin!")

score = 0

print("Here is your first question:")


answer = input("1. What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct, " + player_name + " You got 1 point.")
    score += 1
else:
    print("Incorrect! Unlucky, " + player_name + " You didn't get a point this  time.")


answer = input("2. What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct, " + player_name + " You got another point.")
    score += 1
else:
    print("Incorrect! Unlucky, " + player_name + " You didn't get a point this  time.")


answer = input("3. What is the name of a datatype which is number with a decimal point? ")
if answer.lower() == "float":
    print("Correct, " + player_name + " You got another point.")
    score += 1
else:
    print("Incorrect! Unlucky, " + player_name + " You didn't get a point this  time.")


answer = str(input("4. What is the number '9' in binary code? "))
if answer.lower() == "1001":
    print("Correct, " + player_name + " You got another point.")
    score += 1
else:
    print("Incorrect! Unlucky, " + player_name + " You didn't get a point this  time.")


answer = input("5. What is the word for the way in which a programming language is written? ")
if answer.lower() == "syntax":
    print("Correct, " + player_name + " You got another point.")
    score += 1
else:
    print("Incorrect! Unlucky, " + player_name + " You didn't get a point this  time.")


answer = input("6.What does LAN stand for in terms of a computer network? ")
if answer.lower() == "local area network":
    print("Correct, " + player_name + " You got 1 point.")
    score += 1
else:
    print("Incorrect! Unlucky, " + player_name + " You didn't get a point this  time.")

answer = input("7. What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct, " + player_name + " You got 1 point.")
    score += 1
else:
    print("Incorrect! Unlucky, " + player_name + " You didn't get a point this  time.")


answer = input("8. What does HTML stand for? ")
if answer.lower() == "hypertext markup language":
    print("Correct, " + player_name + " You got another point.")
    score += 1
else:
    print("Incorrect! Unlucky, " + player_name + " You didn't get a point this  time.")


answer = input("9. What is the name of a program which converts a programming language into a readable language for the computer? (i.e binary) ")
if answer.lower() == "compiler":
    print("Correct, " + player_name + " You got another point.")
    score += 1
else:
    print("Incorrect! Unlucky, " + player_name + " You didn't get a point this  time.")


answer = input("10. What is the name of a datatype with two possible values (True or False/ On or Off/ Yes or No?)")
if answer.lower() == "boolean":
    print("Correct, " + player_name + " You got another point.")
    score += 1
else:
    print("Incorrect! Unlucky, " + player_name + " You didn't get a point this  time.")


print("That's the quiz over! Well done " + player_name + " You finished with " + str(score) + " points.")
print("You percentage was: " + str((score/10) * 100) + "%")
