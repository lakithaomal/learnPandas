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


