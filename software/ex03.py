import pandas as pd 

# CSV Files 
print("-----------------CSV FILES----------------- ")
coffee = pd.read_csv('../data/warmup/coffee.csv')
print(coffee.head())
# -----------------CSV FILES----------------- 
#          Day Coffee Type  Units Sold
# 0     Monday    Espresso          25
# 1     Monday       Latte          15
# 2    Tuesday    Espresso          30
# 3    Tuesday       Latte          20
# 4  Wednesday    Espresso          35
print(coffee.info())
# CSV Files are readable, However takes a lot of space 


# Accessing data with pandas 
print("----------------- loc functions 0th index ----------------- ")
print(coffee.loc[0]) # Accesses the 0th index 
# ----------------- loc functions 0th index ----------------- 
# Day              Monday
# Coffee Type    Espresso
# Units Sold           25
# Name: 0, dtype: object

# Accessing data with pandas 
print("----------------- loc functions various indices ----------------- ")
print(coffee.loc[[0,3,4,4]]) # Accepts list or single index 
# ----------------- loc functions 0th index ----------------- 
#          Day Coffee Type  Units Sold
# 0     Monday    Espresso          25
# 3    Tuesday       Latte          20
# 4  Wednesday    Espresso          35
# 4  Wednesday    Espresso          35

# Accessing data with pandas 
print("----------------- loc functions various indices and custom columns ----------------- ")
print(coffee.loc[[0,2,4],["Day","Coffee Type"]]) # Accepts list or single index 
# ----------------- loc functions various indices and custom columns ----------------- 
#          Day Coffee Type
# 0     Monday    Espresso
# 2    Tuesday    Espresso
# 4  Wednesday    Espresso


# Accessing data with pandas 
print("----------------- loc functions with slice syntax and custom columns ----------------- ")
print(coffee.loc[2:4,["Day","Coffee Type"]]) # Accepts list or single index or  - The upper index is inclusive
# ----------------- loc functions with slice syntax and custom columns ----------------- 
#          Day Coffee Type
# 2    Tuesday    Espresso
# 3    Tuesday       Latte
# 4  Wednesday    Espresso

print("----------------- iloc functions with slice syntax and custom columns ----------------- ")
# This does not work with iloc - it only takes indexes : The end is exclusive - The upper index is not inclusive
# print(coffee.iloc[2:4,["Day","Coffee Type"]])
print(coffee.iloc[2:4,1:3])
# ----------------- iloc functions with slice syntax and custom columns ----------------- 
#   Coffee Type  Units Sold
# 2    Espresso          30
# 3       Latte          20

print("----------------- changing indices ----------------- ")
coffee.index = coffee["Coffee Type"]
print(coffee.head())
# ----------------- changing indices ----------------- 
#                    Day Coffee Type  Units Sold
# Coffee Type                                   
# Espresso        Monday    Espresso          25
# Latte           Monday       Latte          15
# Espresso       Tuesday    Espresso          30
# Latte          Tuesday       Latte          20
# Espresso     Wednesday    Espresso          35
print("----------------- changing indices ----------------- ")
coffee.index = coffee.Day
print(coffee.head())
# ----------------- changing indices ----------------- 
#                  Day Coffee Type  Units Sold
# Day                                         
# Monday        Monday    Espresso          25
# Monday        Monday       Latte          15
# Tuesday      Tuesday    Espresso          30
# Tuesday      Tuesday       Latte          20
# Wednesday  Wednesday    Espresso          35
print("----------------- loc functions various indices and custom columns ----------------- ")
# print(coffee.loc[1:3,:]) At this point it does not work 
print(coffee.loc["Monday"])
#            Day Coffee Type  Units Sold
# Day                                   
# Monday  Monday    Espresso          25
# Monday  Monday       Latte          15
print("----------------- loc functions various indices and custom columns ----------------- ")
print(coffee.loc["Monday": "Friday"])
#                  Day Coffee Type  Units Sold
# Day                                         
# Monday        Monday    Espresso          25
# Monday        Monday       Latte          15
# Tuesday      Tuesday    Espresso          30
# Tuesday      Tuesday       Latte          20
# Wednesday  Wednesday    Espresso          35
# Wednesday  Wednesday       Latte          25
# Thursday    Thursday    Espresso          40
# Thursday    Thursday       Latte          30
# Friday        Friday    Espresso          45
# Friday        Friday       Latte          35
print("----------------- loc functions various indices and custom columns ----------------- ")
print(coffee.loc["Monday": "Friday","Day"])

print("----------------- iloc functions various indices and custom columns ----------------- ")
print(coffee.iloc[1:4]) # Now this will work - Only knows indexes as seen from externally 
#              Day Coffee Type  Units Sold
# Day                                     
# Monday    Monday       Latte          15
# Tuesday  Tuesday    Espresso          30
# Tuesday  Tuesday       Latte          20

print("----------------- iloc functions various indices and custom columns ----------------- ")
print(coffee.iloc[1:4,2:])
