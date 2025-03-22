import pandas as pd 
import numpy as np
# CSV Files 

# CSV Files 
print("-----------------CSV FILES----------------- ")
coffee = pd.read_csv('../data/warmup/coffee.csv')
print(coffee.head())

print("----------------- Adding New Columns based on conditions ----------------- ")
# This is expecting a numpy array
coffee['Price'] = 5
print(coffee.head())
#          Day Coffee Type  Units Sold  Price
# 0     Monday    Espresso          25      5
# 1     Monday       Latte          15      5
# 2    Tuesday    Espresso          30      5
# 3    Tuesday       Latte          20      5
# 4  Wednesday    Espresso          35      5

coffee['New_Price'] = np.where(coffee['Coffee Type'] == 'Espresso', 10,20 )
print(coffee.head())
#          Day Coffee Type  Units Sold  Price  New_Price
# 0     Monday    Espresso          25      5         10
# 1     Monday       Latte          15      5         20
# 2    Tuesday    Espresso          30      5         10
# 3    Tuesday       Latte          20      5         20
# 4  Wednesday    Espresso          35      5         10

print(np.where(coffee['Coffee Type'] == 'Expresso', 10,20 ))
# [20 20 20 20 20 20 20 20 20 20 20 20 20 20]


print("----------------- Dropping Columns ----------------- ")
coffee.drop(0) # Just returns - Doesnt do anything to Coffee
print(coffee.head())
#          Day Coffee Type  Units Sold  Price  New_Price
# 0     Monday    Espresso          25      5         10
# 1     Monday       Latte          15      5         20
# 2    Tuesday    Espresso          30      5         10
# 3    Tuesday       Latte          20      5         20
# 4  Wednesday    Espresso          35      5         10


coffee.drop(0, inplace=True) 
print(coffee.head())
#           Day Coffee Type  Units Sold  Price  New_Price
# 1      Monday       Latte          15      5         20
# 2     Tuesday    Espresso          30      5         10
# 3     Tuesday       Latte          20      5         20
# 4   Wednesday    Espresso          35      5         10
# 5   Wednesday       Latte          25      5         20
print("----------------- Dropping Columns ----------------- ")
coffee.drop(columns='Price',inplace=True) 
print(coffee.head())
#           Day Coffee Type  Units Sold  New_Price
# 1      Monday       Latte          15         20
# 2     Tuesday    Espresso          30         10
# 3     Tuesday       Latte          20         20
# 4   Wednesday    Espresso          35         10
# 5   Wednesday       Latte          25         20


# 
print("-----------------CSV FILES----------------- ")
coffeeX = pd.read_csv('../data/warmup/coffee.csv')
print(coffee.head())

coffeeY = coffeeX 

coffeeX['LK']= 5 
print(coffeeX.head())
#          Day Coffee Type  Units Sold  LK
# 0     Monday    Espresso          25   5
# 1     Monday       Latte          15   5
# 2    Tuesday    Espresso          30   5
# 3    Tuesday       Latte          20   5
# 4  Wednesday    Espresso          35   5
print(coffeeY.head())
#          Day Coffee Type  Units Sold  LK
# 0     Monday    Espresso          25   5
# 1     Monday       Latte          15   5
# 2    Tuesday    Espresso          30   5
# 3    Tuesday       Latte          20   5
# 4  Wednesday    Espresso          35   5

# Again We have the pointer problem =  
# you need to do 
coffeeY = coffeeX.copy()
coffeeX['LK2']= 10 
print(coffeeX.head())
#          Day Coffee Type  Units Sold  LK  LK2
# 0     Monday    Espresso          25   5   10
# 1     Monday       Latte          15   5   10
# 2    Tuesday    Espresso          30   5   10
# 3    Tuesday       Latte          20   5   10
# 4  Wednesday    Espresso          35   5   10
print(coffeeY.head())
#          Day Coffee Type  Units Sold  LK
# 0     Monday    Espresso          25   5
# 1     Monday       Latte          15   5
# 2    Tuesday    Espresso          30   5
# 3    Tuesday       Latte          20   5
# 4  Wednesday    Espresso          35   5


coffeeY.rename(columns={'LK':'Price'},inplace=True) # make sure to use inplace
print(coffeeY.head())

coffeeY['Revenue'] = coffeeY['Price'] * coffeeY['Units Sold'] 
print(coffeeY.head())