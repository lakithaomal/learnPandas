import pandas as pd 

# CSV Files 

print("-----------------CSV Again ----------------- ")
bios = pd.read_csv('../data/complete/bios.csv')
print(bios.head())
print(bios.info())


print("----------------- Filtering and sorting ----------------- ")
print(bios.loc[bios['height_cm']>215].head())
print(bios.loc[bios['height_cm']>215,['name','born_country','height_cm']].sort_values('height_cm').head())
print(bios[bios['height_cm']>215].head()) # This works too 
print(bios[(bios['height_cm']>210) & (bios['born_country'] == 'USA')].sort_values('height_cm')) # This works too 

print("----------------- Filtering and sorting with string methods ----------------- ")
# .str.contains("Keith") Checks on a column
print(bios[bios['name'].str.contains("Keith")].head())
print(bios[bios['name'].str.contains("Keith",case=False)].head())
# Using Regular Expressions "Keith|Patric"
print(bios[bios['name'].str.contains("Keith|Patric",case=False)].head())
# [5 rows x 10 columns]
#      athlete_id               name   born_date  ... height_cm weight_kg   died_date
# 6             7      Patrick Chila  1969-11-27  ...     180.0      73.0         NaN
# 119         120   Patrick Wheatley  1899-01-20  ...       NaN       NaN  1967-11-05
# 165         166     Patricia Offel  1971-12-19  ...       NaN       NaN         NaN
# 319         320  Patrick De Koning  1961-04-23  ...     178.0      92.0         NaN
# 405         406   Patricia Obregón  1952-02-18  ...       NaN       NaN  2020-10-06
print(bios[bios['name'].str.contains("Keith|Patric",case=False,regex=False)].head())
# Now its searching for "Keith|Patric"
# Empty DataFrame
# Columns: [athlete_id, name, born_date, born_city, born_region, born_country, NOC, height_cm, weight_kg, died_date]
# Index: []
# print(bios[bios['born_country'].isin(["USA"]),['born_country']].head())
print(bios[bios['born_country'].isin(["USA"])][['name','born_country']].head())

print(bios[(bios['born_country'].isin(["USA","FRA","GBR"]))& (bios['name'].str.startswith("La"))].head())

print("----------------- Filtering with Querys ----------------- ")
print(bios.query("born_country =='USA'").head())
print(bios.query("born_country =='USA' and born_city == 'Seattle'").head())


