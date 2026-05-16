def find_mb(x,y):
  if len(x) != len(y) or 0 in x or 0 in y:
    print ("invalid inputs on find_slope")
  else:
    ratios = 0
    b = y[0]
    for i in range(len(x)):
      y[i] -= b
      ratios += y[i]/x[i]
    
    return {"m":ratios/len(x),"b":b}
    
def predict_y(func,x):
  return (func["m"]*x)+func["b"]
  
def predict_x(func,y):
  return func["m"]/(y-func["b"])


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [52, 55, 61, 65, 68, 74, 78, 83, 87, 91]

func = find_mb(x,y)
print func

print predict_y(func,7.5)

