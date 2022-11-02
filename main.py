coffee_prices =[('cappucino', 1.5,),
               ('expresso',1.2),
               ('mocha',1.9)]

#retrieve the coffee names and price from the above tuple

for coffee, price in coffee_prices:
  print(f"Coffee type {coffee} and price {price}")

#create a function for retrieving the highest priced coffee and the name
def highest_priced(coffee_prices):
  highest_priced = 0
  most_expensive_coffee = ''
  for coffee, price in coffee_prices:
    if price > highest_priced:
      highest_priced = price
      most_expensive_coffee = coffee
    else: 
      pass
  return (most_expensive_coffee, highest_priced)
print(highest_priced(coffee_prices))
    
    
  