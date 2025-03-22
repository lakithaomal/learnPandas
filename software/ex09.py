import pandas as pd 
import numpy as np
import datetime as dt
# CSV Files 

# Merging and Concatinazation

# CSV Files 
print("-----------------CSV FILES----------------- ")
coffee = pd.read_csv('../data/warmup/coffee.csv')
print(coffee)
coffee.info()
# -----------------CSV FILES----------------- 
#           Day Coffee Type  Units Sold
# 0      Monday    Espresso          25
# 1      Monday       Latte          15
# 2     Tuesday    Espresso          30
# 3     Tuesday       Latte          20
# 4   Wednesday    Espresso          35
# 5   Wednesday       Latte          25
# 6    Thursday    Espresso          40
# 7    Thursday       Latte          30
# 8      Friday    Espresso          45
# 9      Friday       Latte          35
# 10   Saturday    Espresso          45
# 11   Saturday       Latte          35
# 12     Sunday    Espresso          45
# 13     Sunday       Latte          35
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
# None - HAPPENS BECAUSE OF PRINTING 


#  Im going to assign some null values 
print("----------------- Adding NANS ----------------- ")
coffee.loc[[0,1], 'Units Sold'] = np.nan
print(coffee)
coffee.info()

# Filling out the nans 
print("----------------- Replacing NANS ----------------- ")
coffee.fillna(100, inplace=True)
print(coffee)
coffee.info()

# Filling out the nans 

coffee.loc[[0,1], 'Units Sold'] = np.nan
print("----------------- Replacing NANS ----------------- ")
coffee.fillna(coffee['Units Sold'].mean(), inplace=True)
print(coffee)
coffee.info()



coffee.loc[3:5, 'Units Sold'] = np.nan
print(coffee)
coffee.info()
print("----------------- Replacing NANS ----------------- ")
# This wont work coffee.fillna(coffee['Units Sold'].interpolate(), inplace=True)
coffee['Units Sold']  =  coffee['Units Sold'].interpolate()
# Interpolate Gives out the whole list 
print(coffee)
coffee.info()


coffee.loc[3:5, 'Units Sold'] = np.nan
print(coffee)
coffee.info()
print("----------------- Dropping NANS ----------------- ")
coffee.dropna(inplace=True)
# Interpolate Gives out the whole list 
print(coffee)
coffee.info()


coffee.loc[3:5, 'Units Sold'] = np.nan
print(coffee)
coffee.info()
print("----------------- Dropping NANS Custom ----------------- ")
coffee.dropna(subset = ['Units Sold'], inplace=True)
# Interpolate Gives out the whole list - Only drops nans on Units Sold 
print(coffee)
coffee.info()

# Indexes 3:5 are dropped
coffee.loc[5:7, 'Units Sold'] = np.nan
print(coffee)
coffee.info()
print("----------------- Get NANS  ----------------- ")
print(coffee[coffee['Units Sold'].isna()])
# Interpolate Gives out the whole list - Only drops nans on Units Sold 
print("----------------- Get Not NANS  ----------------- ")
print(coffee[coffee['Units Sold'].notna()])
