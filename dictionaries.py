
# **Dictionaries in Python (20 Examples)**  

### **Basic Dictionary Problems**  
### **1. Create a Dictionary and Print It**  

my_dict = {"name": "Alice", "age": 25}
print(my_dict)


### **2. Access a Value Using a Key**  

my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])


### **3. Add a New Key-Value Pair**  

my_dict = {"name": "Alice"}
my_dict["age"] = 25
print(my_dict)


### **4. Update a Value in a Dictionary**  

my_dict = {"name": "Alice", "age": 25}
my_dict["age"] = 30
print(my_dict)


### **5. Remove a Key from a Dictionary**  

my_dict = {"name": "Alice", "age": 25}
del my_dict["age"]
print(my_dict)




### **Intermediate Dictionary Problems**  
### **6. Get a Value Using `get()` Method**  

my_dict = {"name": "Alice"}
print(my_dict.get("age", "Not found"))


### **7. Get All Keys in a Dictionary**  

my_dict = {"name": "Alice", "age": 25}
print(my_dict.keys())


### **8. Get All Values in a Dictionary**  

my_dict = {"name": "Alice", "age": 25}
print(my_dict.values())


### **9. Get All Key-Value Pairs in a Dictionary**  

my_dict = {"name": "Alice", "age": 25}
print(my_dict.items())


### **10. Check If a Key Exists in a Dictionary**  

my_dict = {"name": "Alice"}
print("age" in my_dict)




### **Advanced Dictionary Problems**  
### **11. Merge Two Dictionaries**  

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)


### **12. Remove a Key Using `pop()`**  

my_dict = {"name": "Alice", "age": 25}
my_dict.pop("age")
print(my_dict)


### **13. Iterate Over a Dictionary**  

my_dict = {"name": "Alice", "age": 25}
for key, value in my_dict.items():
    print(key, ":", value)


### **14. Create a Dictionary from Two Lists**  

keys = ["name", "age"]
values = ["Alice", 25]
my_dict = dict(zip(keys, values))
print(my_dict)


### **15. Convert a Dictionary to a List of Tuples**  

my_dict = {"a": 1, "b": 2}
print(list(my_dict.items()))




### **Real-World Dictionary Problems**  
### **16. Count Word Frequency in a String**  

sentence = "apple banana apple cherry banana apple"
words = sentence.split()
word_count = {word: words.count(word) for word in words}
print(word_count)


### **17. Sort a Dictionary by Keys**  

my_dict = {"b": 2, "a": 1, "c": 3}
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)


