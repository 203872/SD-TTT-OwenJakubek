# OWEN JAKUBEK
# Works Cited
# None

##### imports

import gameFunctions
import ioFunctions
import os

##### global constants

##### global variables


##### functions
def clear_screen():
  os.system("clear")






def main():
  # main game logic

  def updateboard():
    if (pos1 == 1):
      print("\033[" + str(0) + ";" + str(0) + "H", end="")
      print("X")
    elif (pos1 == -1):
      print("\033[" + str(0) + ";" + str(0) + "H", end="")
      print("O")
    if (pos2 == 1):
      print("\033[" + str(0) + ";" + str(5) + "H", end="")
      print("X")
    elif (pos2 == -1):
      print("\033[" + str(0) + ";" + str(5) + "H", end="")
      print("O")
    if (pos3 == 1):
      print("\033[" + str(0) + ";" + str(9) + "H", end="")
      print("X")
    elif (pos3 == -1):
      print("\033[" + str(0) + ";" + str(9) + "H", end="")
      print("O")
    if (pos4 == 1):
      print("\033[" + str(3) + ";" + str(0) + "H", end="")
      print("X")
    elif (pos4 == -1):
      print("\033[" + str(3) + ";" + str(0) + "H", end="")
      print("O")
    if (pos5 == 1):
      print("\033[" + str(3) + ";" + str(5) + "H", end="")
      print("X")
    elif (pos5 == -1):
      print("\033[" + str(3) + ";" + str(5) + "H", end="")
      print("O")
    if (pos6 == 1):
      print("\033[" + str(3) + ";" + str(9) + "H", end="")
      print("X")
    elif (pos6 == -1):
      print("\033[" + str(3) + ";" + str(9) + "H", end="")
      print("O")
    if (pos7 == 1):
      print("\033[" + str(5) + ";" + str(0) + "H", end="")
      print("X")
    elif (pos7 == -1):
      print("\033[" + str(5) + ";" + str(0) + "H", end="")
      print("O")
    if (pos8 == 1):
      print("\033[" + str(5) + ";" + str(5) + "H", end="")
      print("X")
    elif (pos8 == -1):
      print("\033[" + str(5) + ";" + str(5) + "H", end="")
      print("O")
    if (pos9 == 1):
      print("\033[" + str(5) + ";" + str(9) + "H", end="")
      print("X")
    elif (pos9 == -1):
      print("\033[" + str(5) + ";" + str(9) + "H", end="")
      print("O")




  print("hello, game is started...")

  # local constants
  playercounter = 0
  winvalue = 0


  # general constants
  SENTINEL = -1

  # local variables
  playerletter = 0

  pos1 = 0
  pos2 = 0
  pos3 = 0
  pos4 = 0
  pos5 = 0
  pos6 = 0
  pos7 = 0
  pos8 = 0
  pos9 = 0

  # game variables
  gameInPlay = True
  prompt = "Enter a value between 1 and 9 ( 0 to quit): "
  
  gameState = [
    0, 0, 0, 
    0, 0, 0,
    0, 0, 0
  ]
  
  
  while gameInPlay:
    print("\033[" + str(7) + ";" + str(0) + "H", end="")
    print("in play")
    userInput = ioFunctions.getIntegerInput(prompt)
    userInput -= 1
    # user wants to exit     
    if userInput == SENTINEL:
      break
    elif not (userInput > -1 and userInput < 10):
      print("invalid input " + str(userInput))
    else:
      playercounter += 1
      clear_screen()
      if (playercounter % 2 == 0):
        playerletter = 4
      elif (playercounter % 2 != 0):
        playerletter = 8
      if (playerletter == 4):
        gameState[userInput] = 1
      elif (playerletter == 8):
        gameState[userInput] = -1
      gameFunctions.printBoard(gameState)
      if (playerletter == 4 and userInput == 0):
        pos1 = 1
      if (playerletter == 8 and userInput == 0):
        pos1 = -1
      if (playerletter == 4 and userInput == 1):
        pos2 = 1
      if (playerletter == 8 and userInput == 1):
        pos2 = -1
      if (playerletter == 4 and userInput == 2):
        pos3 = 1
      if (playerletter == 8 and userInput == 2):
        pos3 = -1
      if (playerletter == 4 and userInput == 3):
        pos4 = 1
      if (playerletter == 8 and userInput == 3):
        pos4 = -1
      if (playerletter == 4 and userInput == 4):
        pos5 = 1
      if (playerletter == 8 and userInput == 4):
        pos5 = -1
      if (playerletter == 4 and userInput == 5):
        pos6 = 1
      if (playerletter == 8 and userInput == 5):
        pos6 = -1
      if (playerletter == 4 and userInput == 6):
        pos7 = 1
      if (playerletter == 8 and userInput == 6):
        pos7 = -1
      if (playerletter == 4 and userInput == 7):
        pos8 = 1
      if (playerletter == 8 and userInput == 7):
        pos8 = -1
      if (playerletter == 4 and userInput == 8):
        pos9 = 1
      if (playerletter == 8 and userInput == 8):
        pos9 = -1

      updateboard()

      if gameFunctions.isThereAWin(gameState):
        print("there is a winner")
        if winvalue == 1:
          print("it was x")
        
        break
      elif playercounter == 9:
          print("Draw")


  print("goodbye, game is over")

##### main

if __name__ == "__main__":
  main()