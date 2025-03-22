
import pandas as pd

print("----------------------------------")
df = pd.DataFrame([[1,2,3],[3,4,5],[7,8,9]]) # Sytax is very close to  numpy 
print(df.head()) # You can veiw the first few rows 

print("----------------------------------")
# In this case we can also add column names 
df_a = pd.DataFrame([[1,2,3],[3,4,5],[7,8,9],[1,2,3],[3,4,5],[7,8,9],[1,2,3],[3,4,5],[7,8,9],[1,2,3],[3,4,5],[7,8,9]], columns=["A","B","C"]) # Sytax is very close to  numpy 
print(df_a.head()) # You can veiw the first few rows 
# By Default Head shows the first 5 rows 

print("----------------------------------")
print(df_a.head(2)) # Shows 2 rows 

print("----------------------------------")
print(df_a.head(6)) # Shows 6 rows 

# Likewise the tail commands shows teh last 5 rows 
print("----------------------------------")
print(df_a.tail()) # You can veiw the first few rows 
# By Default Head shows the first 5 rows 

print("----------------------------------")
print(df_a.tail(2)) # Shows 2 rows 

print("----------------------------------")
print(df_a.tail(6)) # Shows 6 rows 
#     A  B  C
# 6   1  2  3
# 7   3  4  5
# 8   7  8  9
# 9   1  2  3
# 10  3  4  5
# 11  7  8  9
# Here 6,7,8,9,10,11 are columns 

print("----------------------------------")
print(df_a.tail(6)) # Shows 6 rows 
#     A  B  C
# 6   1  2  3
# 7   3  4  5
# 8   7  8  9
# 9   1  2  3
# 10  3  4  5
# 11  7  8  9
# Here 6,7,8,9,10,11 are  indexes 

# Printing Indexes
print("----------------------------------")
print(df_a.index) # Remember not a function - df_a is an object
# RangeIndex(start=0, stop=12, step=1)
print(df_a.index.to_list()) # Gives a list of indexes 
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Indexes can be non numeric as well 


print("----------------------------------")
df_c = pd.DataFrame([[1,2,3],[3,4,5],[7,8,9]], \
                    columns=["A","B","C"] , \
                        index=["a","b","c"]) # Sytax is very close to  numpy 
print(df_c) # You can veiw the first few rows 
print(df_c.head(1)) # You can veiw the first few rows 


# Printing Headers 
print("----------------------------------")
print(df_a.columns) # Remember not a function - df_a is an object
# Index(['A', 'B', 'C'], dtype='object')

# Get information about the data frames 
print("----------------------------------")
print(df_a.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 12 entries, 0 to 11
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   A       12 non-null     int64
#  1   B       12 non-null     int64
#  2   C       12 non-null     int64
# dtypes: int64(3)
# memory usage: 416.0 bytes
# None
# As  you can see this is defauled to int64 

print("----------------------------------")
print(df_a.describe())

# ----------------------------------
#                A          B          C
# count  12.000000  12.000000  12.000000
# mean    3.666667   4.666667   5.666667
# std     2.605356   2.605356   2.605356
# min     1.000000   2.000000   3.000000
# 25%     1.000000   2.000000   3.000000
# 50%     3.000000   4.000000   5.000000
# 75%     7.000000   8.000000   9.000000
# max     7.000000   8.000000   9.000000

# As  you can see this is defauled to int64 
print("----------------------------------")
print(df_a.nunique())
# Gives the number of unique values for each column
# A    3
# B    3
# C    3
# dtype: int64

# As  you can see this is defauled to int64 
print("----------------------------------")
print(df_a.shape) # Again an object 
# (12, 3)



