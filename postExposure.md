
# Some examples 

##  How to check intersections between sets 
``` python
pd.DataFrame(
    set(result1["user_id"]).intersection(set(result2["user_id"])),
    columns=["user_id"]
)
```
## Drop, And Drop duplicated, merge and sort 
``` python

loans2 = loans1.sort_values(by=["created_at"], ascending=False) \ # Sorts refinance loans by creation date, newest first.
               .drop(["created_at", "status", "type"], axis=1) \  # Removes unneeded columns from the result to simplify the data.
               .drop_duplicates(["user_id"])                      # If a user has multiple refinance loans, keep only the most recent one (because of the sort above).
``` 

## Merging 
``` python
merged = pd.merge(loans2, submissions, left_on='id', right_on='loan_id')
# Now you're joining loans2 (recent unique refinance loans) with another DataFrame called submissions.
# You're matching: loans2["id"] (loan ID from loans2) with submissions["loan_id"] (matching loan ID in submissions)
```

## Keeping only needed columns 
``` python
final = merged.loc[:, ["user_id", "balance"]]
```

## Filtering using date times 
You’re filtering a DataFrame called fb_comments_count. You're keeping only rows where the created_at date is:
Within 30 days before 2020-02-10 (so starting from 2020-01-11)

In short, this gives you all Facebook comments made from Jan 11 to Feb 10, 2020.

🧠 Why use & and parentheses?
In pandas, when combining multiple conditions, you must use: & for AND | for OR, You also need to wrap each condition in parentheses because these are bitwise operations, not logical operators like and/or

``` python
fb_comments_count_date_filter = fb_comments_count[
    (fb_comments_count["created_at"] <= pd.to_datetime("2020-02-10")) &
    (fb_comments_count["created_at"] >= pd.to_datetime("2020-02-10") - pd.Timedelta(30, "D"))
]
```

## Grouping 
``` python 
fb_comments_count_date_filter_grouped = fb_comments_count_date_filter \
    .groupby("user_id")["number_of_comments"].sum().reset_index()
```
you group the data by user_id. reset_index() turns the user_id back into a normal column (instead of an index), making the DataFrame easier to use.


## 📦 1. Convert `post_date` to Day of the Month

```python
facebook_posts["dayOfMonth"] = pd.to_datetime(facebook_posts["post_date"]).dt.day
```

- `pd.to_datetime()` converts the `post_date` column to datetime format.
- `.dt.day` extracts the day of the month from the date.
- A new column `dayOfMonth` is created in the DataFrame to store these values.

---

## 📊 2. Group Posts by Day and Count

```python
facebook_posts.groupby("dayOfMonth").size().reset_index(name='count')
```

- `groupby("dayOfMonth")` groups the posts by the extracted day of the month.
- `.size()` counts the number of posts for each day.
- `.reset_index(name='count')` transforms the result into a DataFrame and names the count column as `"count"`.

This gives a summary DataFrame showing how many posts occurred on each day of the month.

---

✅ This type of analysis helps identify posting trends or spikes on certain days.


## 🔗 3. Merge User Data with Comment Counts

```python
merged = pd.merge(fb_active_users, fb_comments_count, on='user_id', how='inner')
```

- We combine the `fb_active_users` and `fb_comments_count` DataFrames using an **inner join** on the `user_id` column.
- Only users present in both datasets are retained.

---

## 🗓️ 4. Filter and Summarize Comments by Month

### December 2019

```python
decComments = merged[
    (merged['created_at'] >= '2019-12-01') & 
    (merged['created_at'] < '2020-01-01')
].groupby("country")['number_of_comments'].sum().reset_index("country")
```

### January 2020

```python
janComments = merged[
    (merged['created_at'] >= '2020-01-01') & 
    (merged['created_at'] < '2020-02-01')
].groupby("country")['number_of_comments'].sum().reset_index("country")
```

We filter comments by their `created_at` timestamp for each month and then group them by country to get the total number of comments.

---

## 🥇 5. Rank Countries by Total Comments

```python
decComments["Rank_Dec"] = decComments["number_of_comments"].rank(method='dense', ascending=False)
janComments["Rank_Jan"] = janComments["number_of_comments"].rank(method='dense', ascending=False)
```

- Countries are ranked using **dense ranking** (no gaps in ranks).
- `ascending=False` means higher comment counts get better (lower) ranks.

---

## 🔁 6. Compare Rankings Between Months

```python
merged2 = pd.merge(decComments, janComments, on='country', how='inner')
changed = merged2[merged2.Rank_Jan < merged2.Rank_Dec]
```

- We merge December and January comment summaries.
- We identify countries whose rank **improved** in January (i.e., lower rank number).

---

## ✅ 7. Get the Final Result

```python
result = changed.loc[:, "country"]
```

- Extracts the list of countries whose ranking improved from December to January.

---

📌 **Insight**: This analysis helps identify countries where Facebook comment activity increased in relative importance month-over-month.





