def get_coins(amount,denomination_id=0,coins_collected={"Quarter":0,"Dime":0,"Nickel":0,"Penny":0}):
  
  amount = round(amount * 100)
  denominations = {25:"Quarter",10:"Dime",5:"Nickel",1:"Penny"}
  
  if amount == 0 or denomination_id >= len(denominations):
    if amount != 0:
      coins_collected.update({"Remainder":amount})
    return coins_collected
  else:
    fit = amount // denominations.keys()[::-1][denomination_id]
    coins_collected[denominations[denominations.keys()[::-1][denomination_id]]] += int(fit)
    return get_coins((amount-(fit*denominations.keys()[::-1][denomination_id]))/100,denomination_id+1,coins_collected)
    
print get_coins(5.76)
