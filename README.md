# 📘 Python Sets and Dictionaries

## 🧩 Sets in Python

### 🔹 What is a Set?
A **Set** is an unordered collection of **unique**, **immutable** elements. It does **not allow duplicates** and is useful for storing non-repeating items.

### 🔹 Creating a Set
```python
# Using curly braces
my_set = {1, 2, 3, 4}

# Using set() constructor
my_set2 = set([1, 2, 3, 4])
```

### 🔹 Important Properties
- Unordered (no indexing)
- Mutable (can add or remove items)
- Elements must be immutable

### 🔹 Set Operations
```python
a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)        # {1, 2, 3, 4, 5}
a.intersection(b) # {3}
a.difference(b)   # {1, 2}
a.symmetric_difference(b) # {1, 2, 4, 5}
```

### 🔹 Set Methods
```python
my_set.add(5)       # Add element
my_set.remove(2)    # Remove element (raises error if not found)
my_set.discard(2)   # Removes if exists (no error)
my_set.pop()        # Removes a random element
my_set.clear()      # Clears the set
```

---

## 📚 Dictionaries in Python

### 🔹 What is a Dictionary?
A **Dictionary** is an **unordered**, **mutable** collection of **key-value pairs**. Keys must be unique and immutable (e.g., strings, numbers).

### 🔹 Creating a Dictionary
```python
# Basic dictionary
my_dict = {'name': 'Sathish', 'age': 22}

# Using dict()
my_dict2 = dict(name='Sathish', age=22)
```

### 🔹 Accessing & Modifying Data
```python
my_dict['name']           # Access value by key
my_dict['age'] = 23       # Update value
my_dict['city'] = 'Hyderabad'  # Add new key-value pair
```

### 🔹 Dictionary Methods
```python
my_dict.keys()      # Returns all keys
my_dict.values()    # Returns all values
my_dict.items()     # Returns key-value pairs
my_dict.get('age')  # Safer access to value
my_dict.pop('age')  # Removes key and returns value
my_dict.update({'email': 'sathish@email.com'})  # Add/update multiple items
```

### 🔹 Looping Through Dictionary
```python
for key in my_dict:
    print(key, my_dict[key])

# Or use .items()
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

---

## 🔍 When to Use?

| Use Case | Data Structure |
|----------|----------------|
| Unique items without duplicates | `Set` |
| Key-value mapping | `Dictionary` |

---

## 🧠 Quick Tip:
- Sets are useful for operations like union/intersection.
- Dictionaries are great for fast lookups and organizing data with labels.
