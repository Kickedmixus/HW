from random import randint

def precents(l,r,b):
  temp = []
  print ("calculating precents "+str(l)+","+str(r)+","+str(b)+" total "+str(l+r+b))
  if str(l+r+b) == "1.0" and round(l*100) == l*100 and round(r*100) == r*100 and round(b*100) == b*100:
    for i in range(round(l*100)):
      temp.append("l")
    for i in range(round(r*100)):
      temp.append("r")
    for i in range(round(b*100)):
      temp.append("b")
  else:
    print("<ERROR> precents dont match up")
  return temp[randint(0,99)]
    
def simulate(mapp,times,datacollected):
  if times != 0:
    current = datacollected[len(datacollected)-1]
    print ("on "+current)
    nextt = precents(mapp[current]["l"],mapp[current]["r"],mapp[current]["b"])
    print ("from "+str(current)+" rolling to "+str(nextt))
    return simulate(mapp,times-1,list(datacollected)+list(nextt))
  else:
    return datacollected

mapp = {
  "l":{
    "l":0.7,"r":0.2,"b":0.1
  },
  "r":{
    "l":0.2,"r":0.3,"b":0.5
  },
  "b":{
    "l":0.4,"r":0.6,"b":0
  }
}

times = int(input("simulations? >"))
data = simulate(mapp,times,["l"])
lemons,rasberries,breads,un = 0,0,0,0

for i in range(len(data)):
  if data[i] == "l":
    lemons += 1
  elif data[i] == "r":
    rasberries += 1
  elif data[i] == "b":
    breads += 1
  else:
    un += 1
    
print data

print ("lemons : "+str(lemons)+", rasberries : "+str(rasberries)+", breads : "+str(breads))
print ("lemons : "+str(lemons/len(data))+", rasberries : "+str(rasberries/len(data))+", breads : "+str(breads/len(data)))

def explore(datacollected,terrain):
  if len(terrain) == 1:
    print datacollected
    return datacollected
  else:
    print ("remake "+terrain[0]+" going to "+terrain[1])
    datacollected[terrain[0]][terrain[1]] += 1
    print datacollected
    return explore(datacollected,terrain[1:])
    
newmap = explore({
  "l":{"l":0,"r":0,"b":0},
  "r":{"l":0,"r":0,"b":0},
  "b":{"l":0,"r":0,"b":0}
  },data)

lwhole = newmap["l"]["l"] + newmap["l"]["r"] + newmap["l"]["b"]
rwhole = newmap["r"]["l"] + newmap["r"]["r"] + newmap["r"]["b"]
bwhole = newmap["b"]["l"] + newmap["b"]["r"] + newmap["b"]["b"]

print (str(lwhole)+" "+str(rwhole)+" "+str(bwhole))

solvednewmap = {
  "l":{
    "l":newmap["l"]["l"]/lwhole,
    "r":newmap["l"]["r"]/lwhole,
    "b":newmap["l"]["b"]/lwhole
  },
  "r":{
    "l":newmap["r"]["l"]/rwhole,
    "r":newmap["r"]["r"]/rwhole,
    "b":newmap["r"]["b"]/rwhole
  },
  "b":{
    "l":newmap["b"]["l"]/bwhole,
    "r":newmap["b"]["r"]/bwhole,
    "b":newmap["b"]["b"]/bwhole
  }
}

print solvednewmap
