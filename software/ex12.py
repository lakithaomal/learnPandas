import pandas as pd 
import numpy as np
import datetime as dt

# CSV Files 
print("-----------------CSV FILES----------------- ")
results        = pd.read_csv('../data/complete/results.csv')
results_arrow = pd.read_csv('../data/complete/results.csv',engine='pyarrow',dtype_backend='pyarrow')
results.info()
# -----------------CSV FILES----------------- 
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 308408 entries, 0 to 308407
# Data columns (total 11 columns):
#  #   Column      Non-Null Count   Dtype  
# ---  ------      --------------   -----  
#  0   year        305807 non-null  float64
#  1   type        305807 non-null  object 
#  2   discipline  308407 non-null  object 
#  3   event       308408 non-null  object 
#  4   as          308408 non-null  object 
#  5   athlete_id  308408 non-null  int64  
#  6   noc         308407 non-null  object 
#  7   team        121714 non-null  object 
#  8   place       283193 non-null  float64
#  9   tied        308408 non-null  bool   
#  10  medal       44139 non-null   object 
# dtypes: bool(1), float64(2), int64(1), object(7)
# memory usage: 23.8+ MB
results_arrow.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 308408 entries, 0 to 308407
# Data columns (total 11 columns):
#  #   Column      Non-Null Count   Dtype          
# ---  ------      --------------   -----          
#  0   year        305807 non-null  double[pyarrow]
#  1   type        305807 non-null  string[pyarrow]
#  2   discipline  308407 non-null  string[pyarrow]
#  3   event       308408 non-null  string[pyarrow]
#  4   as          308408 non-null  string[pyarrow]
#  5   athlete_id  308408 non-null  int64[pyarrow] 
#  6   noc         308407 non-null  string[pyarrow]
#  7   team        121714 non-null  string[pyarrow]
#  8   place       283193 non-null  double[pyarrow]
#  9   tied        308408 non-null  bool[pyarrow]  
#  10  medal       44139 non-null   string[pyarrow]
# dtypes: bool[pyarrow](1), double[pyarrow](2), int64[pyarrow](1), string[pyarrow](7)
# memory usage: 37.5 MB

# String Types are availabe for arrow instead of objects in arrow 
# By using strings or custom data types makes it more efficient 


print("-----------------CSV Again ----------------- ")
bios = pd.read_csv('../data/complete/bios.csv')
print(bios.head())
print(bios.info())
# Filter bios for Olympians born in New Hampshire or San Francisco
olympians = bios[(bios['born_region'] == 'New Hampshire') | (bios['born_city'] == 'San Francisco')]
print(olympians.head(23))
# Toy DataFrame for pivot table practice
data = {
    'Date': pd.date_range(start='1/1/2022', periods=6, freq='D'),
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia'],
    'Temperature': [30, 45, 28, 35, 40, 38],
    'Humidity': [80, 70, 75, 60, 65, 72]
}

df = pd.DataFrame(data)
print(df)

# Creating a pivot table
pivot_table = pd.pivot_table(df, values='Temperature', index='City', columns='Date')
print(pivot_table)


import matplotlib.pyplot as plt

# Plotting histogram of heights
plt.figure(figsize=(10, 6))
plt.hist(bios['height_cm'].dropna(), bins=30, log=True, edgecolor='black')
plt.title('Histogram of Heights')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency (log scale)')
plt.grid(True)
plt.show()