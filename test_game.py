print("Welcome to the test!")

playing = input("Are you ready to start the game? ")

if playing.lower() != "yes":
    quit()

print("Cool! let's begin :)")
score = 0

answer = input("What is the first programming language in demand? ")
if answer.lower() == "python":
    print('Excellent, you are correct!')
    score += 1
else:
    print("Hardluck, wrong answer!")

answer = input("When was the first version of python released? ")
if answer.lower() == "1991":
    print('You are doig good so far, its correct!')
    score += 1
else:
    print("Be serious, this is wrong!")

answer = input("What does this '#' used for in python? ")
if answer.lower() == "comments":
    print('Nice one, thats correct')
    score += 1
else:
    print("Put more effect please, this wrong")

answer = input("Who created python? ")
if answer.lower() == "Guidon van Rossum":
    print('Good job, you nailed it!')
    score += 1
else:
    print("Thats not coorect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
