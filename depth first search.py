from turtle import *
from random import randint
from math import *
from time import sleep
Screen().bgcolor("black")
hideturtle()
speed(0)

class Node:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children
    def get(self):
        return self.value
def distance(x1,y1,x2,y2):
  print (x1,y1)
  print (x2,y2)
  return sqrt((x2-x1)^2+(y2-y1)^2)


head = Node(1,[Node(12,[Node(4,[Node(2,[]),Node(3,[])]),Node(7,[Node(5,[]),Node(6,[])])]),Node(8,[Node(9,[]),Node(0,[Node(10,[]),Node(11,[])])])])


def drawsphere(num,x,y):
  
  pencolor("white")
  penup()
  
  penup()
  pensize(10)
  goto(x,y-7)
  pendown()
  circle(7,360)
  
  penup()
  pensize(15)
  goto(x,y-2)
  pendown()
  circle(2,360)
  
  pencolor("black")
  
  pensize(1)
  penup()
  goto(x,y-10)
  pendown()
  circle(10,360)
  penup()
  
  goto(x-5,y-5)
  pendown()
  write(num)
  penup()
  
  pensize(1)

counter = 0


def dfs(head):
  
  global counter
  
  for move in range(len(head.children)):
    dfs(head.children[move])
    print move
    print head.children[move].data
  
  head.data = counter
  counter += 1

def bfsv(head,x,y):
  for i in range(len(head.children)):
    fakex = x+(randint(1,25)*2.5)
    goto(x,y+25)
    pencolor("white")
    pendown()
    goto(fakex,y)
    drawsphere(head.children[i].data,fakex,y)
    bfsv(head.children[i],fakex,y-25)
    penup()
  
bfsv(Node(None,[head]),-150,175)
penup()
dfs(head)
bfsv(Node(None,[head]),-150,0)
penup()

print head.data
