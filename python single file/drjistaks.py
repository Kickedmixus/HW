def in_bounds(grid,r,c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])
  
def passable(grid,r,c):
  return grid[r][c] != -1
  
def neighbors(grid, node):
  r,c = node
  result = []
  for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
    if in_bounds(grid, nr, nc) and passable(grid,nr,nc):
      result.append((nr,nc))
  return result
  
def pick_min(unvisited,dist):
  best = None
  best_val = 10**12
  for n in unvisited:
    val = dist.get(n, 10**12)
    if val < best_val:
      best, best_val = n, val
      
  return best
  
def reconstruct_path(prev,current):
  path = [current]
  while current in prev:
    current = prev[current]
    path.append(current)
  path.reverse()
  return path
  
def drip(grid, start, dist):
  if not (in_bounds(grid,*start) and in_bounds(grid,*goal)):
    return [], None
  if not (passable(grid,*start) and passable(grid,*goal)):
    return [],None
  dist = {start: 0}
  prev = {}
  visited = set()
  unvisited = [start]
  
  while unvisited:
    current = pick_min(unvisited,dist)
    if current is None: break
    if current == goal:
      path = reconstruct_path(prev, current)
      return path, dist[current]
      
    unvisited.remove(current)
    visited.add(current)
    
    for nb in neighbors(grid, current):
      if nb in visited:
        continue
      
      tentative = dist[current] + grid[nb[0]][nb[1]]
      if tentative < dist.get(nb, 10**12):
        dist[nb] = tentative
        prev[nb] = current
        if nb not in unvisited:
          unvisited.append(nb)
          
  return [], None
  
def draw_grid(grid, path, start, goal):
  path_set = set(path)
  for r in range(len(grid)):
    row = []
    for c in range(len(grid[0])):
      pos = (r,c)
      if pos == start:
        row.append(' S ')
      elif pos == goal:
        row.append(' G ')
      elif grid[r][c] == -1:
        row.append(' # ')
      elif pos in path_set:
        row.append(' * ')
      else:
        val = grid[r][c]
        row.append(" "+str(val)+"|")
    print(''.join(row))
    
grid = [
  [1,  1,  1,  1,  1,  1],
  [1, -1,  5,  9,  9,  1],
  [1,  1,  1, -1,  5,  1],
  [9,  9,  1,  1,  1,  1],
  [1, -1, -1,  9,  1,  1],
  [1,  1,  1,  1,  1,  1],
]

start = (0, 0)
goal  = (5, 5)

path, total_cost = drip(grid, start, goal)
if path:
  print("Path found!")
  print("Total step cost:", total_cost)
  draw_grid(grid, path, start, goal)
  print("Path coords:", path)
else:
  print("No path found.")
