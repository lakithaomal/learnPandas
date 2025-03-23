# learnPandas
These exercises are based on [this](https://www.youtube.com/watch?v=2uvysYbKdjM&t=17s) youtube video. 

# Create a custon virtual environment
-  `python3 -m venv vEnvPandas` Creates an environment under the name vEnvPandas 
- `source vEnvPandas/bin/activate` Activates the Environment
- `pip3 install -r requirments.txt` installs the dependancies
The requirments file was downlaoded from [here](https://github.com/KeithGalli/complete-pandas-tutorial/blob/master/requirements.txt)

## Data Frames 
The main data structure of the python pandas libary. These can be thought of specialized tables. 


## Q 
Can dataframes be 1d or 3d.  
Varios ways to do for loops 
lists going from 10 : 100 
Watch the video on a regex https://www.youtube.com/watch?v=vsa9GGzMFXQ

## 🔥 Lambda Functions in Python

### ➤ Basic Syntax
```python
lambda arguments: expression
```

Example:
```python
square = lambda x: x * x
print(square(4))  # Output: 16
```

---

## ⚡ Lambda with `if-else` (Ternary Format)

### ➤ Single `if-else`
```python
lambda x: 'Even' if x % 2 == 0 else 'Odd'
```

Example:
```python
check = lambda x: 'Even' if x % 2 == 0 else 'Odd'
print(check(5))  # Output: Odd
```

---

## 🚀 Multiple `if-elif-else` in Lambda (Nested)
```python
lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C' if x >= 70 else 'F'
```

Example:
```python
grade = lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C' if x >= 70 else 'F'
print(grade(85))  # Output: B
```

---

## ⚠️ Limitations
- Lambda can only have **one expression**.
- Avoid **complex logic** – use `def` for better readability.

---

## 🧩 In Pandas Example
```python
df['result'] = df['score'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')
```

## Help 
- Pandas Show Versions `pd.show_versions()`
- Version and Library information  `pd.show_versions()`
- Creating Data Frames 
```
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data,index=labels)
print(df)
s = pd.Series([1, 3, 5, np.nan, 6, 8])
```
- Information on data frames `df.info()`, `df.describe()` or `df.head()`
- Info on functions  `pd.DataFrame.drop.__doc__`
- Note: Numpy has no loc or iloc
- Get Specific rows `df.iloc[:3]`
- Get specific columns `df.loc[:, ['animal', 'age']]` or `df[['animal', 'age']]`
- More on getting specific data: `df.loc[df.index[[3, 4, 8]]['animal', 'age']]` or `df[['animal','age']].iloc[[3,4,8]]`
- Specific Rows based on conditions
  - `df[df['visits'] > 3]`
  - `df[df['age'].isnull()]`
  - `df[df['age'].isnull()]` or `df[df['age'].isna()]`
  - `df[(df['animal']=='cat') & (df['age']<3)]` or `df[df['age'].between(2, 4)]`
  - `df['animal'] = df['animal'].replace('snake', 'python')`
  
- Changing Values
  -  `df.loc['f', 'age'] = 1.5`
  -  `df['priority2'] = df['priority'] =='yes'`
- Summaries
  - `df['visits'].sum()`
  - `df.groupby('animal')['age'].mean()`
  - `df['animal'].value_counts()`
- Appending `df.loc['k'] = [5.5, 'dog', 'no', 2]`, `df.loc[len(df)] = [5, 6]` or `df = pd.concat([df, new_row], ignore_index=True)`
- Deleting `df = df.drop('k')` or `df.drop(['priority'],axis=1,inplace=True)`
- Sorting `df.sort_values(['age','visits'],ascending=[0,1])` Ascending is 1
- Renaming `df.rename({'priority2':'priority'},axis=1)`
- Pivot Tables `dfNew= df.pivot_table(index='animal', columns='visits',values='age',aggfunc='mean')`

# Additional Summary from exercises 
- Creating an Array `df_a = pd.DataFrame([[1,2,3],[3,4,5],[7,8,9],[1,2,3],[3,4,5],[7,8,9],[1,2,3],[3,4,5],[7,8,9],[1,2,3],[3,4,5],[7,8,9]], columns=["A","B","C"]) # Sytax is very close to  numpy `
- Summarizing DataFrames: `df.head()`, `df.tail()`, `df.index`: gives a Range object, `df.columns`: gives a Index object,`df_a.info()` Columns, Non Null Count and Dtype, `df.descibe()` min,max, std, mean, count and quantiles for each column , `df_a.nunique()` unique values per given column and `df.shape` gives the shape for the data frame.
- Different ways to read data
  - `results = pd.read_parquet('../data/complete/results.parquet')`
  - `olympics_data = pd.read_excel('../data/complete/olympics-data.xlsx')`
  - `bios = pd.read_csv('../data/complete/bios.csv')` 
- Randomly show variables `coffee.sample(10)`
- Access Data
  - `coffee.loc[0]`: Get the index valued '0'
  -  Multiple indexes named with a list `coffee.loc[[0,3,4,4]]`
  -  Slicing: Label-based indexing (loc): `coffee.loc[2:4,["Day","Coffee Type"]])` All inclusive - just picks them - If the indexes are not numbers will not work - 
  - Integer-based indexing (iloc): `coffee.iloc[2:4,1:3]` Upper end not inclusive like numpy
# Summary of `.loc` and `.iloc` in Pandas

| Feature       | `.loc`                                         | `.iloc`                                        |
|---------------|-----------------------------------------------|------------------------------------------------|
| Index Type    | Label-based indexing                          | Integer-based indexing                         |
| Usage         | `df.loc[row_label, column_label]`             | `df.iloc[row_position, column_position]`       |
| Includes      | The stop label is **inclusive**               | The stop index is **exclusive**                |
| Data Types    | Accepts labels, booleans, and slices          | Accepts integers, lists of integers, and slices|
| Example       | `df.loc['row1', 'col1']`                      | `df.iloc[0, 0]`                                |
| Multiple Rows | `df.loc[['row1', 'row2']]`                    | `df.iloc[[0, 1]]`                              |

## Quick Tips
- Use `.loc` when you know **row/column names**.
- Getting Cells using at `coffee.at[1,"Day"]` Label based
- Getting Cells using iat `coffee.iat[1,1]` : Index based  

- Assigning Values `coffee.loc[1:4,"Units Sold"] = 100` using Label Based

# Helpful 
- Sorting Values: `coffee.sort_values(["Units Sold","Coffee Type"],ascending=[0,1]).head()`
- For Loops for Data Frams
  ```
  for index, row in coffee.iterrows():
    print(index)
    print(row['Units Sold'])
    print()
  ```
- Filtering
  - `bios.loc[bios['height_cm']>215,['name','born_country','height_cm']]` very useful when filtering both rows and columns 
  - `bios[(bios['height_cm']>210) & (bios['born_country'] == 'USA')]`
  - `bios[bios['name'].str.contains("Keith|Patric",case=False)` using regular expressions
  -  Is In `bios[(bios['born_country'].isin(["USA","FRA","GBR"]))& (bios['name'].str.startswith("La"))`
  -  Queries `bios.query("born_country =='USA' and born_city == 'Seattle'")`
- Modifications 
    - Add data Using Where`coffee['New_Price'] = np.where(coffee['Coffee Type'] == 'Espresso', 10,20 )`
    - More Ways to add `bios_new["first_name"] = bios_new['name'].str.split(' ').str[0]` and `bios_new['height_category'] = \
      bios['height_cm'].apply(lambda x: 'Kota' if x <165 else 'Samanya' if x < 185 else 'Diga' )`
    - Using Advanced Functions
  ```
        def categorize_athlete(row):
            if row['height_cm']< 175 and row['weight_kg']<70 :
                return 'Leight Weight'
            elif row['height_cm']< 185 and row['weight_kg']<=80 :
                return 'Middle Weight'
            else:
                return 'Heavy Weight'

        # Make sure to add the axis as 1 - In this case take in rows 
        bios_new['Category'] = bios_new.apply(categorize_athlete, axis=1)
  ``` 
      
    - Add constant value for all values `coffeeX['LK']= 5`
    - Deleting Rows using Index `coffee.drop(0)`
    - Deletiing Columns `coffee.drop(columns='Price',inplace=True)`
    - Rename Columns `coffeeY.rename(columns={'LK':'Price'},inplace=True)`
    - Copying `coffeeY = coffeeX.copy()`  Dont just use the =
    - Convert to Date time `bios_new["born_date"] = pd.to_datetime(bios_new['born_date'],errors='coerce')`
 
- Merge and Concat 
  - Key Wise `bios_new = pd.merge(bios,nocs, left_on='born_country', right_on='NOC', how='left',suffixes=["A","B"])`
      - Left Keep all on the left.
      - Right Keep all on the right.
      - Outher on Keep all
      - Inner on Keep only common 

  - Concat - Just make one from two `concat_df = pd.concat([usa,gbr])`
      - On concat - axis 1 stack rows 
      - On concat - axis 0 ctack columns
   
- Handling Nans
  - filling `coffee.fillna(100, inplace=True)`
  - Interpolating `coffee['Units Sold']  =  coffee['Units Sold'].interpolate()`
  - Dropping: `coffee.dropna(inplace=True)` or `coffee.dropna(subset = ['Units Sold'], inplace=True)`
  - Checking: `coffee[coffee['Units Sold'].isna()]` or `coffee[coffee['Units Sold'].notna()]`
 
- Grouping
  - `coffee.groupby(['Coffee Type']).agg({'Units Sold': 'sum', 'price': 'sum', 'revenue': 'sum'})`
  - `coffee.groupby(['Coffee Type','Day']).agg({'Units Sold': 'sum', 'price': 'sum', 'revenue': 'sum'})`
 
   Others
  - Pivoting `coffee.pivot(columns='Coffee Type', index='Day',values='revenue')` and ` pd.pivot_table(df, values='Temperature', index='City', columns='Date')`
         - Use pivot() if no duplicates and no aggregation needed.
         - Use pivot_table() if duplicates exist or you need aggregation.
  - Counting `bios.groupby([bios['birth_year'],bios['birth_month']])['name'].count().reset_index().sort_values('name',ascending=False).head(30))`
  - Ranking `bios['height_rank'] = bios['height_cm'].rank()`
  - Cumilative Summing `coffee['cumilitive_revenue'] = coffee['revenue'].cumsum()` and `coffee['revenue'].rolling(3).sum()`
  - Or Statement ` bios[(bios['born_region'] == 'New Hampshire') | (bios['born_city'] == 'San Francisco')]`
 
- Plotting
```
import matplotlib.pyplot as plt
# Plotting histogram of heights
plt.figure(figsize=(10, 6))
plt.hist(bios['height_cm'].dropna(), bins=30, log=True, edgecolor='black')
plt.title('Histogram of Heights')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency (log scale)')
plt.grid(True)
plt.show()
```

- Some more examples 
Adding Rows: `df.loc['k'] = [5.5, 'dog', 'no', 2]`
Droping Rows: `df = df.drop('k')`
Counting Each Value `df['animal'].value_counts()`
MaxMin Indexes and Labels: `print(df.idxmax(axis=1))   # Output: labels of max per row
print(df.values.argmax(axis=1))  # NumPy: position of max per row`
Largest N :`dF.nlargest(3)`
Shifting: `.shift()`
Convert to Numpy :`df.to_numpy()`
Aggregate and Transform `df.agg(lambda x: np.mean(x) * 5.6)` and `df.transform(lambda x: x * 101.2)`
String Methods: `s.str.lower()`
Time Series
```
rng = pd.date_range("1/1/2012", periods=100, freq="s")

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

ts.resample("5Min").sum()
```
