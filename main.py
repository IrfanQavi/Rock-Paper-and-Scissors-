import random
userinput = input("Rock, Paper, or Scissors?")
computerinput = random.randint(1, 3)

match(computerinput):
  case 1:
    computerinput = "Rock"
  
  case 2:
    computerinput = "Paper"
    
  case 3:
    computerinput = "Scissors"
  
if computerinput == userinput:
  print("We had a tie.")
elif computerinput == "Rock" and userinput == "Paper":
  print("You won!")
elif computerinput == "Rock" and userinput == "Scissors":
  print("I won!")
elif computerinput == "Scissors" and userinput == "Rock":
  print("You won!")
elif computerinput == "Scissors" and userinput == "Paper":
  print("I won!")
elif computerinput == "Paper" and userinput == "Scissors":
  print("You won!")
elif computerinput == "Paper" and userinput == "Rock":
  print("I won!")
