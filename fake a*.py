from time import sleep
def in_bounds(grid,r,c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])

grid = [
  [0,0,0,0,0,1,1],
  [1,1,1,1,1,1,0],
  [0,1,0,0,0,1,0],
  [0,1,0,1,0,0,0],
  [0,0,0,1,1,1,0],
  [1,1,0,0,0,0,0],
]
costs = []

start = (0, 0)   # top-left corner
goal  = (5, 6)   # bottom-right-ish


def recrupiz(x,y,goal,price,grid):
  
  if (x,y) == goal:
    print("GOAL FOUND "+str(x)+" "+str(y))
    costs.append(price)
    return 
  angles = []
  if in_bounds(grid,x+1,y):
    print("in bound "+str(x+1)+" "+str(y))
    if grid[x+1][y] == 0:
      angles.append([1,0])
    else:
      print("not bound "+str(x+1)+" "+str(y))
  if in_bounds(grid,x-1,y):
    print("in bound "+str(x-1)+" "+str(y))
    if grid[x-1][y] == 0:
      angles.append([-1,0])
  else:
    print("not bound "+str(x-1)+" "+str(y))
  if in_bounds(grid,x,y+1):
    print("in bound "+str(x)+" "+str(y+1))
    if grid[x][y+1] == 0:
      angles.append([0,1])
  else:
    print("not bound "+str(x)+" "+str(y+1))
  if in_bounds(grid,x,y-1):
    print("in bound "+str(x)+" "+str(y-1))
    if grid[x][y-1] == 0:
      angles.append([0,-1])
  else:
    print("not bound "+str(x)+" "+str(y-1))
      
  grid[x][y] = 2
  for i in range(len(angles)):
    print("probe from "+str(x)+" "+str(y)+" to "+str(x+angles[i][0])+" "+str(y+angles[i][1]))
    recrupiz(x+angles[i][0],y+angles[i][1],goal,price+1,grid)
    
recrupiz(start[0],start[1],goal,0,grid)
print("ugly ver")
for i in range(len(grid)):
  print(grid[i])
print costs
if len(costs) == 0:
  print ("NO SOLUTION FOUND")
else:
  print("CHEAPEST "+str(sorted(costs)[0]))
  
  
