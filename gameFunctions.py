def isThereAWin(gameState):
  # checks for a winner
  
  return isThereAWinInAnyRow(gameState) or isThereAWinInAnyColumn(gameState) or isThereAWinInAnyDiagonal(gameState)



def isThereAWinInAnyDiagonal(gameState):
  if gameState[0] == 1 and gameState[4] == 1 and gameState[8] == 1:
    print("top left to bottom right 1")
    return True

  if gameState[2] == 1 and gameState[4] == 1 and gameState[6] == 1:
    print("top right, to bottom left 1")
    return True

  # checking for o wins
  if gameState[0] == -1 and gameState[4] == -1 and gameState[8] == -1:
    print("top left to bottom right -1")
    return True

  if gameState[2] == -1 and gameState[4] == -1 and gameState[6] == -1:
    print("top right to bottom left -1")
    return True

  return False 


def isThereAWinInAnyRow(gameState):
  # checks for a winner in any row
  
  # checking for x wins

  # top row
  if gameState[0] == 1 and gameState[1] == 1 and gameState[2] == 1:
    print("top row 1")
    return True

  # middle row
  if gameState[3] == 1 and gameState[4] == 1 and gameState[5] == 1:
    print("middle row 1")
    return True

  # bottom row
  if gameState[6] == 1 and gameState[7] == 1 and gameState[8] == 1:
    print("bottom row 1")
    return True
  
  # checking for o wins

  # top row
  if gameState[0] == -1 and gameState[1] == -1 and gameState[2] == -1:
    print("top row -1")
    return True

  # middle row
  if gameState[3] == -1 and gameState[4] == -1 and gameState[5] == -1:
    print("middle row -1")
    return True

  if gameState[6] == -1 and gameState[7] == -1 and gameState[8] == -1:
    print("bottom row -1")
    return True

  # no winner in any row
  return False




def isThereAWinInAnyColumn(gameState):
  # checks for a winner in any column
  
  # checking for x wins

  # left column
   if gameState[0] == 1 and gameState[3] == 1 and gameState[6] == 1:
    print("left column 1")
    return True

  # middle row
    if gameState[1] == 1 and gameState[4] == 1 and gameState[7] == 1:
      print("middle column 1")
      return True

  # bottom row
    if gameState[2] == 1 and gameState[5] == 1 and gameState[8] == 1:
      print("right collumn 1")
      return True
  
  # checking for o wins

  # top row
    if gameState[0] == -1 and gameState[3] == -1 and gameState[6] == -1:
      print("left collumn -1")
      return True

  # middle row
    if gameState[1] == -1 and gameState[4] == -1 and gameState[7] == -1:
      print("middle collumn -1")
      return True

    if gameState[2] == -1 and gameState[5] == -1 and gameState[8] == -1:
      print("right collumn -1")
      return True
    
    return False

def isThereADraw(gameState):
  if isThereAWinInAnyColumn(gameState) == False and isThereAWinInAnyDiagonal(gameState) == False and isThereAWinInAnyRow(gameState) == False:
    print("there is a draw")



def printBoard(gameState):
   print("  |   |")
   print("---------")
   print("  |   |")
   print("---------")
   print("  |   | ")

