
# 🐼 Pandas Essentials: A Beginner's Guide with Code Examples and Explanations

Welcome! This guide is structured as a **lesson** to help you master `pandas`—Python’s most powerful data manipulation tool. Each section walks through an essential concept using real code and **clear explanations**.

---

## 📦 1. Importing Pandas

```python
import pandas as pd
```

Before doing any data analysis, we import the `pandas` library, which gives us powerful tools to work with tabular data (think spreadsheets or SQL tables).

---

## 🧹 2. Cleaning and Preparing Data

### a. Drop Unnecessary Columns

```python
df = df.drop(["unnecessary_column"], axis=1)
```

Use this to remove columns that aren’t needed for your analysis, making the dataset cleaner and more manageable.

---

### b. Remove Duplicate Rows

```python
df = df.drop_duplicates(subset=["user_id"])
```

When users have multiple rows and we only want one per user, `drop_duplicates()` helps reduce redundancy.

---

### c. Sort Data

```python
df = df.sort_values(by="created_at", ascending=False)
```

Sorting helps us prioritize the most recent or important records (e.g., latest transactions or posts).

---

### ✅ Combined Example

```python
loans2 = loans1.sort_values(by=["created_at"], ascending=False) \
               .drop(["created_at", "status", "type"], axis=1) \
               .drop_duplicates(["user_id"])
```

This code keeps only the **latest loan** for each user, removes unnecessary columns, and organizes the data chronologically.

---

## 🔗 3. Merging DataFrames

```python
merged = pd.merge(loans2, submissions, left_on="id", right_on="loan_id", how="inner")
```

Merging is like joining tables in SQL:
- We connect two datasets using a common key (here, `id` and `loan_id`).
- The `inner` method keeps only rows that match in both tables.
This is useful when you want to combine user info with related records (e.g., loan applications and user details).

---

## 📄 4. Selecting Specific Columns

```python
final = merged.loc[:, ["user_id", "balance"]]
```

Always narrow down to the relevant columns before exporting or visualizing. This keeps data concise and readable.

---

## 🔍 5. Filtering Data

### a. Using Multiple Conditions

```python
filtered = df[(df["status"] == "open") & (df["country"] == "USA")]
```

This filters the dataset to include **only active users** in the USA.

> ⚠️ Important: Use `&` for AND and `|` for OR, and wrap each condition in parentheses!

---

### b. Filtering by Date Ranges

```python
filtered_date = df[
    (df["created_at"] <= pd.to_datetime("2020-02-10")) &
    (df["created_at"] >= pd.to_datetime("2020-02-10") - pd.Timedelta(30, "D"))
]
```

This gets records **within 30 days before** February 10, 2020.
Perfect for analyzing recent activity or trends.

---

## 🧮 6. Grouping and Aggregation

### a. Sum of Values per Group

```python
grouped = df.groupby("user_id")["number_of_comments"].sum().reset_index()
```

Groups data by `user_id`, then calculates total comments.
`reset_index()` turns `user_id` from index back to a column.

---

### b. Count Records per Group

```python
post_counts = df.groupby("dayOfMonth").size().reset_index(name='count')
```

This counts how many posts occurred on each day of the month.

---

## 📅 7. Working with Dates

### Convert String to Date and Extract Day

```python
df["dayOfMonth"] = pd.to_datetime(df["post_date"]).dt.day
```

- Converts string-formatted dates into pandas datetime objects.
- Extracts the **day** of the month (1–31), which is useful for temporal patterns.

---

## 📊 8. Ranking

```python
df["rank"] = df["value"].rank(method="dense", ascending=False)
```

Ranks entries based on a column's value. For example:
- Countries with more comments rank higher.
- `dense` ensures no rank gaps (e.g., 1, 2, 2, 3).

---

## 🔁 9. Comparing Time Periods

Let’s see how country-level Facebook comment activity changed between December and January.

### a. Group Comments by Month

```python
dec = df[(df['created_at'] >= '2019-12-01') & (df['created_at'] < '2020-01-01')] \
         .groupby("country")["number_of_comments"].sum().reset_index()

jan = df[(df['created_at'] >= '2020-01-01') & (df['created_at'] < '2020-02-01')] \
         .groupby("country")["number_of_comments"].sum().reset_index()
```

### b. Rank and Compare

```python
dec["rank_dec"] = dec["number_of_comments"].rank(method='dense', ascending=False)
jan["rank_jan"] = jan["number_of_comments"].rank(method='dense', ascending=False)

merged_rank = pd.merge(dec, jan, on="country", how="inner")
improved = merged_rank[merged_rank["rank_jan"] < merged_rank["rank_dec"]]
result = improved[["country"]]
```

- Ranks for each month are calculated.
- We merge both to see which countries improved their ranking (i.e., became more active in January).

---

## 🔗 10. Finding Intersections Between Sets

```python
pd.DataFrame(
    set(df1["user_id"]).intersection(set(df2["user_id"])),
    columns=["user_id"]
)
```

This technique identifies common users across two datasets, which is handy when analyzing behavior overlap or cross-platform activity.

---

## 🎯 Summary

With just a few lines of code, you can:
- Clean and filter raw data
- Join multiple datasets
- Perform group-based analysis
- Rank and compare metrics over time

These are the **building blocks** of data analysis with pandas. Mastering these operations empowers you to extract insights from virtually any dataset!

---

🧠 **Next Steps**: Try these techniques on your own dataset or experiment with public datasets (like from Kaggle or UCI). Practice makes perfect!

## Whats faster
```
Vectorized ops > itertuples() > iterrows() > iloc in loop > loc in 
Vector Opts
df['new_col'] = df['col1'] + df['col2']  # Vectorized and fast

for row in df.itertuples():
    print(row.Index, row.column_name)
 ```



