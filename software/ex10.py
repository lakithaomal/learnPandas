import pandas as pd 
import numpy as np
import datetime as dt
# CSV Files 

# Merging and Concatinazation

# CSV Files 
print("-----------------CSV Again ----------------- ")
bios = pd.read_csv('../data/complete/bios.csv')
print(bios.head())
print(bios.info())


# CSV Files 
print("-----------------CSV FILES----------------- ")
coffee = pd.read_csv('../data/warmup/coffee.csv')
print(coffee.info())
# CSV Files are readable, However takes a lot of space 



print("----------------- Value Counts ----------------- ")
print(bios["NOC"].value_counts())

print(bios["NOC"].value_counts().head(20))
print(bios[bios['NOC'] == "Sri Lanka"].sort_values(["name"]).head(50)) 
print(bios[bios['NOC'] == "Sri Lanka"]["born_city"].value_counts()) 
print(bios[bios['NOC'] == "Sri Lanka"]["born_region"].value_counts()) 
print(bios["born_city"].value_counts().head(20))

print("----------------- Group By ----------------- ")
# Should provide a 
# 🔹 What groupby Does:
# Think of it like:

# Split the data into groups.
# Apply a function to each group (e.g., sum, mean, count).
# Combine the results into a new DataFrame.
print(coffee.groupby(['Coffee Type'])['Units Sold'].mean())
# ----------------- Group By ----------------- 
# Coffee Type
# Espresso    37.857143
# Latte       27.857143
# Name: Units Sold, dtype: float64

# Also you can do Aggegate functions too 
print(coffee.info())
coffee["price"] = 10
coffee["revenue"] = coffee["price"]* coffee["Units Sold"]
print(coffee)
print(coffee.groupby(['Coffee Type']).agg({'Units Sold': 'sum', 'price': 'sum', 'revenue': 'sum'}))
#           Day Coffee Type  Units Sold  price  revenue
# 0      Monday    Espresso          25     10      250
# 1      Monday       Latte          15     10      150
# 2     Tuesday    Espresso          30     10      300
# 3     Tuesday       Latte          20     10      200
# 4   Wednesday    Espresso          35     10      350
# 5   Wednesday       Latte          25     10      250
# 6    Thursday    Espresso          40     10      400
# 7    Thursday       Latte          30     10      300
# 8      Friday    Espresso          45     10      450
# 9      Friday       Latte          35     10      350
# 10   Saturday    Espresso          45     10      450
# 11   Saturday       Latte          35     10      350
# 12     Sunday    Espresso          45     10      450
# 13     Sunday       Latte          35     10      350
#              Units Sold  price  revenue
# Coffee Type                            
# Espresso            265     70     2650
# Latte               195     70     1950
print(coffee.groupby(['Coffee Type','Day']).agg({'Units Sold': 'sum', 'price': 'sum', 'revenue': 'sum'}))
#                        Units Sold  price  revenue
# Coffee Type Day                                  
# Espresso    Friday             45     10      450
#             Monday             25     10      250
#             Saturday           45     10      450
#             Sunday             45     10      450
#             Thursday           40     10      400
#             Tuesday            30     10      300
#             Wednesday          35     10      350
# Latte       Friday             35     10      350
#             Monday             15     10      150
#             Saturday           35     10      350
#             Sunday             35     10      350
#             Thursday           30     10      300
#             Tuesday            20     10      200
#             Wednesday          25     10      250


print("----------------- Pivot Tables ----------------- ")
coffee.info()
print(coffee)
pivot = coffee.pivot(columns='Coffee Type', index='Day',values='revenue')
print(pivot)
# Coffee Type  Espresso  Latte
# Day                         
# Friday            450    350
# Monday            250    150
# Saturday          450    350
# Sunday            450    350
# Thursday          400    300
# Tuesday           300    200
# Wednesday         350    250
print(pivot.loc['Monday','Latte'])
print(pivot.sum()) # Gives the sume for each column
# Coffee Type
# Espresso    2650
# Latte       1950
print(pivot.sum(axis=1)) # Gives the sume for each column
# Friday       800
# Monday       400
# Saturday     800
# Sunday       800
# Thursday     700
# Tuesday      500
# Wednesday    600


# Advanced Operations 
print("----------------- Group By ----------------- ")
print(bios.head())
bios.info()
# Adding New Column 
bios['birth_date']  = pd.to_datetime(bios['born_date'])
bios['birth_year']  = bios['birth_date'].dt.year
bios['birth_month'] = bios['birth_date'].dt.month
print(bios.head())
bios.info()
# Grouping by year 
print(bios.groupby(bios['birth_date'].dt.year).count())
# Reset index adds an index which is needed here. # Here name could have been anything
print(bios.groupby([bios['birth_year'],bios['birth_month']])['name'].count().reset_index().sort_values('name',ascending=False).head(30))
#       birth_year  birth_month  name
# 1437      1970.0          1.0   239
# 1461      1972.0          1.0   229
# 1629      1986.0          1.0   227
# 1497      1975.0          1.0   227
# 1617      1985.0          1.0   225
# 1619      1985.0          3.0   222
# 1569      1981.0          1.0   221