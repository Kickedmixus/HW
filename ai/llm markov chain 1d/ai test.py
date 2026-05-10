from random import *
from data import *

wordbank = []
for i in range(len(lang)):
  wordbank += lang[i].split()
wordbank = list(set(wordbank))
print wordbank

def precents(w):
    numbers = list(range(len(w)))
    w = [weight * 100 for weight in w]
    total = sum(w)
    r = random() * total
    upto = 0
    for i, weight in enumerate(w):
        if upto + weight >= r:
            return i
        upto += weight
    return numbers[-1]

def mapcreator(wordbank):
  array = []
  for x in range(len(wordbank)):
    array.append([0]*len(wordbank))
  print array
  return array
    
def simulate(box,times,on):
  if times != 0:
    nextt = precents(box[on])
    print wordbank[nextt]
    return simulate(box,times-1,nextt)

def mapsenbox(box,lang):
  lang = lang.split()
  for i in range(len(lang)-1):
    box[wordbank.index(lang[i])][wordbank.index(lang[i+1])] += 1
  return box

def maplangbox(box,lang):
  for i in range(len(lang)):
    box = mapsenbox(box,lang[i])
  return box

def solvebox(box):
  for x in range(len(box)):
    total = 0
    for y in range(len(box[x])):
      total += box[x][y]
    for y in range(len(box[x])):
      if box[x][y] != 0:
        box[x][y] = box[x][y]/total
  return box

box = mapcreator(wordbank)
print box
box = maplangbox(box,lang)
print box
box = solvebox(box)
print box
starter = "you"
print starter
simulate(box,20,wordbank.index(starter))
