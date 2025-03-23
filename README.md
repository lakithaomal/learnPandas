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

# Advanced Functions 
- 






`
