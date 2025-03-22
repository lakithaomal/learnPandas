import pandas as pd 
import numpy as np
import datetime as dt
# CSV Files 

# CSV Files 

print("-----------------CSV Again ----------------- ")
bios = pd.read_csv('../data/complete/bios.csv')
print(bios)
print(bios.head())
print(bios.info())

bios_new = bios.copy()

bios_new["first_name"] = bios_new['name'].str.split(' ').str[0]
# Splitting and adding a new column name 
print(bios_new)
print(bios_new.head())
print(bios_new.info())

# Query All the Keiths 
print(bios_new.query('first_name == "Keith"'))


# Not na only takes rows which are not nans 
# Errors Coerce = Helps Error gracefully handling 
bios_new["born_date"] = pd.to_datetime(bios_new['born_date'],errors='coerce')
# Splitting and adding a new birth year = Make sure its int
print(bios_new)
print(bios_new.head())
print(bios_new.info())


# # Query Every one born after 
bios_new["born_year"] = bios_new['born_date'].dt.year

print(bios_new.query('born_year > 2000'))


# Lambda Functions 
bios_new['height_category'] = \
      bios['height_cm'].apply(lambda x: 'Kota' if x <165 else 'Samanya' if x < 185 else 'Diga' )

print(bios_new)
print(bios_new.head())
print(bios_new.info())


# We  can also use normal functions - The row should be the input 
def categorize_athlete(row):
    if row['height_cm']< 175 and row['weight_kg']<70 :
        return 'Leight Weight'
    elif row['height_cm']< 185 and row['weight_kg']<=80 :
        return 'Middle Weight'
    else:
        return 'Heavy Weight'

# Make sure to add the axis as 1 - In this case take in rows 
bios_new['Category'] = bios_new.apply(categorize_athlete, axis=1)

print(bios_new)
print(bios_new.head())
print(bios_new.info())




# Index = False gets rid of the index on the .csv
bios_new.to_csv('../data/complete/bios_new.csv', index=False)