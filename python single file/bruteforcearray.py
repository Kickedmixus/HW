import copy
import time

grid = [
  ["%",8,1,7,3],
  [3,1,3,6,4],
  [8,3,1,6,9],
  [2,0,4,6,8],
  [5,0,1,6,"&"],
  ]
  
def display_board(board):
  for i in range(len(board)):
    t = ""
    for j in range(len(board[i])):
      t += " "+str(board[i][j])
    print t
  print ""
  
def explore(grid,position,fromm,holding):
  y,x = position
  if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
    if grid[y][x] == "&":
      print "found solution"
      print holding
      total = 0
      for i in range(len(holding)):
        total += holding[i]
      return [total,grid]
    elif grid[y][x] != "@":
      new_holding = copy.deepcopy(holding)
      #print new_holding
      new_holding.append(grid[y][x])
      new_grid = copy.deepcopy(grid)
      new_grid[fromm[0]][fromm[1]] = "@"
      return search_board(new_grid,position,new_holding)

def search_board(grid,position=(0,0),holding=[]):
  y,x = position
  directions = []
  directions.append(explore(grid,(y+1,x),position,holding))
  directions.append(explore(grid,(y,x+1),position,holding))
  directions.append(explore(grid,(y-1,x),position,holding))
  directions.append(explore(grid,(y,x-1),position,holding))
  time.sleep(0.0001)
  #print directions
  return directions
  
solutions = search_board(grid)

first = []
second = []
for i in range(len(solutions)):
  if solutions[i][0] < first:
    second = first
    first = solutions[i]
  elif solutions[i][0] < second:
    second = solutions[i]
    
print "FIRST PLACE",str(first[0])
display_board(first[1])
print "SECOND PLACE",str(second[0])
display_board(second[1])
