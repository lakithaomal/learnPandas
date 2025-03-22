import pandas as pd 

# CSV Files 
print("-----------------CSV FILES----------------- ")
coffee = pd.read_csv('../data/warmup/coffee.csv')
print(coffee.info())
# CSV Files are readable, However takes a lot of space 


# CSV     31MB 
# Feather 12.2 MB
# Parquiet 4.7 MB - Very Speedy 
# Excel Even Larger 

print("-----------------Parquet FILES----------------- ")
results = pd.read_parquet('../data/complete/results.parquet')
print(results.head())
print(results.info())

print("-----------------Excel data----------------- ")
olympics_data = pd.read_excel('../data/complete/olympics-data.xlsx')
print(olympics_data.head())
print(olympics_data.info())


print("-----------------Excel particular Sheet Data ----------------- ")
olympics_data = pd.read_excel('../data/complete/olympics-data.xlsx',\
                               sheet_name="results")
print(olympics_data.head())
print(olympics_data.info())


print("-----------------CSV Again ----------------- ")
bios = pd.read_csv('../data/complete/bios.csv')
print(bios.head())
print(bios.info())
  
# Converter functions are also available 
# bios.to_csv
# bios.to_excel
# bios.to_parquet

# Randomly show 10 rows 
coffee.sample(10)
coffee.sample(10 , random_state=1) # Deterministic = Always behaves the same way 


# Accessing data with pandas 
print("----------------- loc functions 0th index ----------------- ")
print(coffee.loc[0]) # Accesses the 0th index 



