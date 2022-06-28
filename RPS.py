
import os

def startScreen():
  os.system("clear")
  
  firstChoice = input("Who is going to go first? (Player 1 / Player 2): ")
  firstChoice = firstChoice.upper()
    
  while firstChoice != "PLAYER 1" and firstChoice != "PLAYER 2":
    os.system("clear")
    input("Invalid Option. Please pick a valid option.")
    firstChoice = input("Who is going to go first? (Player 1 / Player 2): ")
    firstChoice = firstChoice.upper()
        
  return firstChoice

def beginGame(firstChoice):
  os.system("clear")
    
  if firstChoice == "PLAYER 1":
    print ("Player One's Go:")
    print ()
    p1Choice = input("What is your choice? (R/P/S): ")
    p1Choice = p1Choice.upper()
        
    while p1Choice != "R" and p1Choice != "P" and p1Choice != "S":
      os.system("clear")
      input("Invalid Option. Please pick a valid option.")
      p1Choice = input("What is your choice? (R/P/S): ")
      p1Choice = p1Choice.upper()
        
    os.system("clear")
    print ("Player Two's Go:")
    print ()
    p2Choice = input("What is your choice? (R/P/S):")
    p2Choice = p2Choice.upper()
        
    while p2Choice != "R" and p2Choice != "P" and p2Choice != "S":
      os.system("clear")
      input("Invalid Option. Please pick a valid option.")
      p2Choice = input("What is your choice? (R/P/S): ")
      p2Choice = p2Choice.upper()

  if firstChoice == "PLAYER 2":
    print ("Player Two's Go:")
    print ()
    p2Choice = input("What is your choice? (R/P/S): ")
    p2Choice = p2Choice.upper()
        
    while p2Choice != "R" and p2Choice != "P" and p2Choice != "S":
      os.system("clear")
      input("Invalid Option. Please pick a valid option.")
      p2Choice = input("What is your choice? (R/P/S): ")
      p2Choice = p2Choice.upper()

    os.system("clear")
    print ("Player One's Go:")
    print ()
    p1Choice = input("What is your choice? (R/P/S):")
    p1Choice = p1Choice.upper()
        
    while p1Choice != "R" and p1Choice != "P" and p1Choice != "S":
      os.system("clear")
      input("Invalid Option. Please pick a valid option.")
      p1Choice = input("What is your choice? (R/P/S): ")
      p1Choice = p1Choice.upper()
            
  return p1Choice, p2Choice
    
def decideWinner(p1Choice, p2Choice):
  if p1Choice == p2Choice:
    winner = "It's a draw!"
        
  elif p1Choice == "R" and p2Choice == "P":
    winner = "Player 2 Wins!"
    
  elif p1Choice == "P" and p2Choice == "R":
    winner = "Player 1 Wins!"
    
  elif p1Choice == "S" and p2Choice == "P":
    winner = "Player 1 Wins!"
    
  elif p1Choice == "P" and p2Choice == "S":
    winner = "Player 2 Wins!"
    
  elif p1Choice == "S" and p2Choice == "R":
    winner = "Player 2 Wins!"
        
  elif p1Choice == "R" and p2Choice == "S":
    winner = "Player 1 Wins!"
    
  return winner

def displayResults(winner, p1Choice, p2Choice):
    
  ##### Convert P1 Choices
    
  if p1Choice == "R":
    p1Choice = "Rock"
    
  if p1Choice == "P":
    p1Choice = "Paper"
    
  if p1Choice == "S":
    p1Choice = "Scissors"
    
  ##### Convert P2 Choices
    
  if p2Choice == "R":
    p2Choice = "Rock"
    
  if p2Choice == "P":
    p2Choice = "Paper"
  
  if p2Choice == "S":
    p2Choice = "Scissors"

  os.system("clear")
    
  print(winner)
    
  print("Player 1 chose:", p1Choice)
  print("Player 2 chose:", p2Choice)
    
  restart = input("Would you like to restart? (Y/N): ")
  restart = restart.upper()
    
  while restart != "Y" and restart != "N":
    os.system("clear")
    input("Invalid Option. Please pick a valid option.")
    restart = input("Would you like to restart? (Y/N): ")
    restart = restart.upper()
    
  if restart == "Y":
    firstChoice = startScreen()
    
  if restart == "N":
    exit()

## MAIN PROGRAM

firstChoice = startScreen()

p1Choice, p2Choice = beginGame(firstChoice)

winner = decideWinner(p1Choice, p2Choice)

displayResults(winner, p1Choice, p2Choice)
