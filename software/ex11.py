import pandas as pd 
import numpy as np
import datetime as dt

# CSV Files 
print("-----------------CSV FILES----------------- ")
coffee = pd.read_csv('../data/warmup/coffee.csv')
print(coffee.info())
# CSV Files are readable, However takes a lot of space 

# CSV Files 
print("-----------------CSV Again ----------------- ")
bios = pd.read_csv('../data/complete/bios.csv')
print(bios.head())
print(bios.info())

coffee["price"] = 10
coffee["revenue"] = coffee["price"]* coffee["Units Sold"]
print(coffee)


print("----------------- Shifting ----------------- ")
coffee['yesterday']  =  coffee['revenue'].shift(2) 
# Adding a column by the values of ones 2 indexes behind
print(coffee.head())
#           Day Coffee Type  Units Sold  price  revenue  yesterday
# 0      Monday    Espresso          25     10      250        NaN
# 1      Monday       Latte          15     10      150        NaN
# 2     Tuesday    Espresso          30     10      300      250.0
# 3     Tuesday       Latte          20     10      200      150.0
# 4   Wednesday    Espresso          35     10      350      300.0
# 5   Wednesday       Latte          25     10      250      200.0
# 6    Thursday    Espresso          40     10      400      350.0
# 7    Thursday       Latte          30     10      300      250.0

# Gets the highest height athletes 
print("----------------- Ranking ----------------- ")
bios.info()
print(bios.head())

bios['height_rank'] = bios['height_cm'].rank()
bios.info()
print(bios.head())
print(bios.sort_values(['height_rank'],ascending=False))

# To Add rank 1 for the tallest athlete
bios['height_rank'] = bios['height_cm'].rank(ascending=False)
bios.info()
print(bios.head())
print(bios.sort_values(['height_rank']))


# Gets the highest height athletes 
print("----------------- Rolling Functions ----------------- ")
print(coffee)
coffee['cumilitive_revenue'] = coffee['revenue'].cumsum()
# Cumilative sum is very obvoius 
print(coffee)

print(coffee)
coffee['3_day_revenue'] = coffee['revenue'].rolling(3).sum()
# Sum of last 3 days of coffee 
print(coffee)





