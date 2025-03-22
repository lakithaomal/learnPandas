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
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 14 entries, 0 to 13
# Data columns (total 3 columns):
#  #   Column       Non-Null Count  Dtype 
# ---  ------       --------------  ----- 
#  0   Day          14 non-null     object
#  1   Coffee Type  14 non-null     object
#  2   Units Sold   14 non-null     int64 
# dtypes: int64(1), object(2)
# memory usage: 464.0+ bytes
# None

print("----------------- loc functions with modifications ----------------- ")
coffee.loc[1:4,"Units Sold"] = 100
print(coffee)

print("----------------- at and iat  ----------------- ")
# print(coffee.at[1,1]) Does not work 
# But print(coffee.iat[1,1]) Does works
print(coffee.iat[1,1])
print(coffee.at[1,"Day"])
# For these only specific items can would work - slightly more efficiet


print("----------------- Grabbing Columns  ----------------- ")
print(coffee["Units Sold"])
# ----------------- Grabbing Columns  ----------------- 
# 0      25
# 1     100
# 2     100
# 3     100
# 4     100
# 5      25
# 6      40
# 7      30
# 8      45
# 9      35
# 10     45
# 11     35
# 12     45
# 13     35
# Name: Units Sold, dtype: int64


print("----------------- Sorting  ----------------- ")
print(coffee.sort_values("Units Sold").head()) # Default is asceding 
# ----------------- Sorting  ----------------- 
#           Day Coffee Type  Units Sold
# 0      Monday    Espresso          25
# 5   Wednesday       Latte          25
# 7    Thursday       Latte          30
# 9      Friday       Latte          35
# 11   Saturday       Latte          35

print(coffee.sort_values("Units Sold",ascending=False).head()) # Default is asceding 
#          Day Coffee Type  Units Sold
# 1     Monday       Latte         100
# 2    Tuesday    Espresso         100
# 3    Tuesday       Latte         100
# 4  Wednesday    Espresso         100
# 8     Friday    Espresso          45

print(coffee.sort_values(["Units Sold","Coffee Type"],ascending=False).head()) # Default is asceding 
# Asigning Secondary sort variable
#          Day Coffee Type  Units Sold
# 1     Monday       Latte         100
# 3    Tuesday       Latte         100
# 2    Tuesday    Espresso         100
# 4  Wednesday    Espresso         100
# 8     Friday    Espresso          45


print(coffee.sort_values(["Units Sold","Coffee Type"],ascending=[0,1]).head()) # Default is asceding 
# Here ascending is  false for units sold but true for coffee type
#          Day Coffee Type  Units Sold
# 2    Tuesday    Espresso         100
# 4  Wednesday    Espresso         100
# 1     Monday       Latte         100
# 3    Tuesday       Latte         100
# 8     Friday    Espresso          45

print("----------------- Iterating Using For  ----------------- ")
# Iterrows  is a special method used for looping - Not optimized 
# Try to use built in methods 
for index, row in coffee.iterrows():
    print(index)
    print(row['Units Sold'])
    print()
