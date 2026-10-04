import random
com = random.choice(["rock","paper","scissors"])

while True:
     hum = input("What's your choice: ").lower()

     if hum == com:
         print("It's a Tie")

     elif hum == "rock" and com == "scissors":
         print("Congrats You Won!")
         break

     elif hum == "scissors" and com == "paper":
         print("Congrats You Won!")
         break

     elif hum == "paper" and com == "rock":
         print("Congrats You Won!")
         break

     else:
         print("Computer Wins")