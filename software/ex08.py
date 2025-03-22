import pandas as pd 
import numpy as np
import datetime as dt
# CSV Files 

# Merging and Concatinazation

print("-----------------CSV Again ----------------- ")
bios = pd.read_csv('../data/complete/bios.csv')
print(bios)
print(bios.head())
print(bios.info())

nocs = pd.read_csv('../data/complete/noc_regions.csv')
print(nocs)
print(nocs.head())
print(nocs.info())

pd.merge(bios,nocs)

# Left On - the column on the left data frame ,,
# Right on column on the right data frame,
# how - Left Keep all on the left.
# how - Right Keep all on the right.
# how - outher on Keep all
# how - oinner on Keep only common 

# Suffixes are added to avoid having  NOC_x ,  NOC_y or it having automatically renaming 
# So 
bios_new = pd.merge(bios,nocs, left_on='born_country', right_on='NOC', how='left',suffixes=["A","B"])
print(bios_new)
print(bios_new.head())
print(bios_new.info())
# [145500 rows x 13 columns]
#    athlete_id                   name   born_date  ... NOCB  region notes
# 0           1  Jean-François Blanchy  1886-12-12  ...  FRA  France   NaN
# 1           2         Arnaud Boetsch  1969-04-01  ...  FRA  France   NaN
# 2           3           Jean Borotra  1898-08-13  ...  FRA  France   NaN
# 3           4        Jacques Brugnon  1895-05-11  ...  FRA  France   NaN
# 4           5           Albert Canet  1878-04-17  ...  GBR      UK   NaN

# [5 rows x 13 columns]
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 145500 entries, 0 to 145499
# Data columns (total 13 columns):
#  #   Column        Non-Null Count   Dtype  
# ---  ------        --------------   -----  
#  0   athlete_id    145500 non-null  int64  
#  1   name          145500 non-null  object 
#  2   born_date     143693 non-null  object 
#  3   born_city     110908 non-null  object 
#  4   born_region   110908 non-null  object 
#  5   born_country  110908 non-null  object 
#  6   NOCA          145499 non-null  object 
#  7   height_cm     106651 non-null  float64
#  8   weight_kg     102070 non-null  float64
#  9   died_date     33940 non-null   object 
#  10  NOCB          110639 non-null  object 
#  11  region        110636 non-null  object 
#  12  notes         257 non-null     object 
# dtypes: float64(2), int64(1), object(10)
# memory usage: 14.4+ MB
# None

print("----------------- Countyr Filtering ----------------- ")
usa = bios[bios['born_country'] == "USA"].copy()
gbr = bios[bios['born_country'] == "GBR"].copy()
print(usa.head())
print(usa.info())
print()
print(gbr.head())
print(gbr.info())

print("----------------- Concatinating ----------------- ")
# Merged looks for a KEY where rows are merged side by side 
# while concat adds to below 
# Or concat outer concat is default 
# On concat - axis 1 stack rows 
# On concat - axis 0 ctack columns   
concat_df = pd.concat([usa,gbr])
print(concat_df)
print(concat_df.head())
print(concat_df.info())