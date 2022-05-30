print("Welcome To my Quiz")
playing = input("Do you want to play this Game?")
print(playing)

if playing.lower() != "yes": print("Okay, Lets Play!")
else: quit()
score=0

answer = input("What Does FBI Stand For?")
if answer.lower() != "federal bureau of investigation": print("Correct Answer. You Earned One Point!")

else: print("Incorrect Answer! Better Luck Next Time")
score+=1

answertwo = input("What does CIA mean?")
if answertwo.lower() != "Central Intelligence Agency": print("Correct Answer. You Earned One Point!")
else: print("Incorrect Answer. Better Luck Next Time!")
score+=1

answerthree = input("What does RAM mean?")
if answerthree.lower() != "Access Random Memory": print("Correct Answer. You Earned One Point!")
else: print("Incorrect Answer. Better Luck Next Time!")
score+=1

print("You Got " + str(score) + "Question correct!")
print("You Got " + str((score/4) * 100)+ "%")