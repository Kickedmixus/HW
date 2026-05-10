import copy

def make_board():
  return [["░", "░", "░", "░", "░", "░", "░", "░"],["░", "░", "░", "░", "░", "░", "░", "░"],["░", "░", "░", "░", "░", "░", "░", "░"],["░", "░", "░", "░", "░", "░", "░", "░"],
          ["░", "░", "░", "░", "░", "░", "░", "░"],["░", "░", "░", "░", "░", "░", "░", "░"],["░", "░", "░", "░", "░", "░", "░", "░"],["░", "░", "░", "░", "░", "░", "░", "░"]]

def display_board(board):
  for i in range(len(board)):
    t = ""
    for j in range(len(board[i])):
      t += " "+str(board[i][j])
    print t
  print ""

def add_queen(position,area):
  y,x = position
  for i in range(len(area)-y):
    area[y+i][x] = "█"

  for i in range(len(area)-y):
    if 0 <= x+i < len(area) and 0 <= y+i < len(area):
      area[y+i][x+i] = "█" 
    if 0 <= x-i < len(area) and 0 <= y+i < len(area):
      area[y+i][x-i] = "█" 
  
  area[y][x] = "♛"
  
  return area
  
def find_queens(board=make_board(),queens=0,positions=[]):
  print "placed",positions
  display_board(board)
  if queens == len(board):
    return positions
  else:
    for i in range(len(board)):
      multiverse = []
      if board[queens][i] =="░":
        universe = find_queens(add_queen((queens,i),(copy.deepcopy(board))),queens+1,copy.deepcopy(positions)+[(queens,i)])
        if universe is not None:
          multiverse.append(universe)
           
      if len(multiverse) != 0:
        return multiverse[0]
    print "goback"

print find_queens()
