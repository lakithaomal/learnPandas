# Pandas Quick Reference Guide

## Table of Contents
1. [Setup](#setup)
2. [Data Structures](#data-structures)
3. [Lambda Functions](#lambda-functions)
4. [Creating DataFrames](#creating-dataframes)
5. [Accessing Data](#accessing-data)
6. [Modifying Data](#modifying-data)
7. [Data Summarization](#data-summarization)
8. [Filtering Data](#filtering-data)
9. [Merging and Concatenation](#merging-and-concatenation)
10. [Handling Missing Data](#handling-missing-data)
11. [Grouping and Aggregation](#grouping-and-aggregation)
12. [Pivot Tables](#pivot-tables)
13. [Plotting](#plotting)
14. [Advanced Operations](#advanced-operations)
15. [Time Series](#time-series)

---

## Setup
```bash
python3 -m venv vEnvPandas  # Create virtual environment
source vEnvPandas/bin/activate  # Activate environment
pip3 install -r requirements.txt  # Install dependencies
```

Requirements file: [GitHub Requirements](https://github.com/KeithGalli/complete-pandas-tutorial/blob/master/requirements.txt)

---

## Data Structures

### DataFrames
- Main structure in pandas, similar to SQL tables or Excel spreadsheets.
- Supports row and column labels.

---

## Lambda Functions

### Syntax
```python
lambda arguments: expression
```

### Examples
```python
# Square a number
square = lambda x: x * x
print(square(4))  # Output: 16

# Even/Odd check
check = lambda x: 'Even' if x % 2 == 0 else 'Odd'

# Grading
grade = lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C' if x >= 70 else 'F'
```

### In Pandas
```python
df['result'] = df['score'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')
```

---

## Creating DataFrames
```python
import pandas as pd
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
```

---

## Accessing Data

### Rows and Columns
```python
df.iloc[:3]  # First 3 rows
df[['animal', 'age']]  # Specific columns
df.loc[:, ['animal', 'age']]  # Equivalent
df.loc['a']  # Row 'a'
```

### Conditions
```python
df[df['visits'] > 3]
df[df['age'].isnull()]
df[(df['animal']=='cat') & (df['age']<3)]
df[df['age'].between(2, 4)]
```

---

## Modifying Data

### Change Values
```python
df.loc['f', 'age'] = 1.5
df['priority2'] = df['priority'] == 'yes'
```

### Add or Delete
```python
df.loc['k'] = [5.5, 'dog', 'no', 2]  # Add row
df = df.drop('k')  # Drop row
df.drop(['priority'], axis=1, inplace=True)  # Drop column
```

### Rename and Sort
```python
df.rename({'priority2': 'priority'}, axis=1)
df.sort_values(['age','visits'], ascending=[False, True])
```

---

## Data Summarization
```python
df.info()
df.describe()
df.head()
df['visits'].sum()
df.groupby('animal')['age'].mean()
df['animal'].value_counts()
```

---

## Filtering Data

### Using Conditions
```python
bios[bios['height_cm'] > 215]
bios[(bios['height_cm'] > 210) & (bios['born_country'] == 'USA')]
bios[bios['name'].str.contains("Keith|Patric", case=False)]
```

### Using `isin()` and `query()`
```python
bios[bios['born_country'].isin(["USA", "FRA", "GBR"])]
bios.query("born_country =='USA' and born_city == 'Seattle'")
```

---

## Merging and Concatenation
```python
# Merge
pd.merge(bios, nocs, left_on='born_country', right_on='NOC', how='left')

# Concatenate
pd.concat([usa, gbr])
```

---

## Handling Missing Data
```python
df.fillna(100, inplace=True)
df['Units Sold'].interpolate()
df.dropna(inplace=True)
df[df['Units Sold'].isna()]
```

---

## Grouping and Aggregation
```python
df.groupby('animal').agg({'age': 'mean', 'visits': 'sum'})
```

---

## Pivot Tables
```python
df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')
```

---

## Plotting
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(bios['height_cm'].dropna(), bins=30, log=True, edgecolor='black')
plt.title('Histogram of Heights')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency (log scale)')
plt.grid(True)
plt.show()
```

---

## Advanced Operations

### Ranking, Cumulative Sum, and Rolling
```python
df['rank'] = df['height_cm'].rank()
df['cumulative'] = df['revenue'].cumsum()
df['rolling_sum'] = df['revenue'].rolling(3).sum()
```

### Convert to NumPy and Aggregate
```python
df.to_numpy()
df.agg(lambda x: np.mean(x) * 5.6)
df.transform(lambda x: x * 101.2)
```

---

## Time Series
```python
rng = pd.date_range("1/1/2012", periods=100, freq="s")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts.resample("5Min").sum()
```
