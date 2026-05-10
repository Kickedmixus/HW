from turtle import *
from math import *
from time import sleep
hideturtle()
speed(0)




mapp = {}

visited = []

graph = {
  "A":[{"B":3,"C":3},[-175,0]],
  "B":[{"A":3,"D":3.5,"E":2.8},[-100,50]],
  "C":[{"A":3,"E":2.8,"F":3.5} ,[-100,-50]],
  "D":[{"B":3.5,"E":3.8,"G":10},[100,50]],
  "E":[{"B":2.8,"C":2.8,"D":3.1,"G":7},[100,-50]],
  "F":[{"G":2.5,"C":3.5},[-50,0]],
  "G":[{"F":2.5,"E":7,"D":10},[0,100]]
}

def distance(x1,y1,x2,y2):
  print (x1,y1)
  print (x2,y2)
  return sqrt((x2-x1)^2+(y2-y1)^2)

index = graph.keys()

unvisited = index

for i in range(len(graph)):
  penup()
  home()
  goto(graph[index[i]][1][0],graph[index[i]][1][1])
  pendown()
  print ("rendering circle "+index[i]+" at "+str(graph[index[i]][1][0])+","+str(graph[index[i]][1][1]))
  circle(10,360)
  penup()
  goto(graph[index[i]][1][0]+10,graph[index[i]][1][1]-10)
  pendown()
  write(index[i])
  
for starter in range(len(graph)):
  for ender in range(len(graph[index[starter]][0])):
    penup()
    home()
    endpoint = graph[index[starter]][0].keys()[ender]
    #starter
    goto(graph[index[starter]][1][0],graph[index[starter]][1][1]+10)
    pendown()
    setheading(towards(graph[endpoint][1][0],graph[endpoint][1][1]+10))
    print(distance(graph[index[starter]][1][0],graph[index[starter]][1][1]+10,graph[endpoint][1][0],graph[endpoint][1][1]+10))
    #forward(distance(graph[index[starter]][1][0],graph[index[starter]][1][1]+10,graph[endpoint][1][0],graph[endpoint][1][1]+10))
    #ender
    print ("rendering line "+index[starter]+","+endpoint)
    goto(graph[endpoint][1][0],graph[endpoint][1][1]+10)
    penup()

def pather(current,cost,history,goal):
  history = list(history)
  if current == goal:
    mapp.update({cost:history})
    return [cost,history]
  for i in range(len(graph[current][0])):
    nextnode = graph[current][0].keys()[i]
    print ("creating branch >"+nextnode)
    if nextnode in history:
      print ("pruned f>"+current+" t>"+nextnode)
    else:
      print ("sent new pather f>"+current+" t>"+nextnode+" p>"+str(cost+graph[current][0][nextnode]))
      history.append(current)
      pather(nextnode,cost+graph[current][0][nextnode],history,goal)
      







into = input("goal? >")
pather("A", 0, [], into)
sleep(1)

#print mapp[min(mapp.keys())]
#print min(mapp.keys())
#print visited
#print unvisited

def pickle(inp):
  for i in range(len(index)):
      uber1 = pather(inp, 0, [],"A")

  
  uber = {

  return uber


