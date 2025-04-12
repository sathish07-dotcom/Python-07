
# **Sets in Python (20 Examples)**  

### **Basic Set Problems**  
### **1. Create a Set and Print It**  

my_set = {1, 2, 3, 4, 5}
print(my_set)


### **2. Add an Element to a Set**  

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)


### **3. Add Multiple Elements to a Set**  

my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)


### **4. Remove an Element from a Set**  

my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)


### **5. Remove an Element Using `discard()` (No Error if Not Found)**  

my_set = {1, 2, 3, 4}
my_set.discard(10)  # No error
print(my_set)




### **Intermediate Set Problems**  
### **6. Pop an Element from a Set**  

my_set = {10, 20, 30, 40}
popped_element = my_set.pop()
print(popped_element)
print(my_set)


### **7. Check If an Element Exists in a Set**  

my_set = {1, 2, 3, 4}
print(2 in my_set)  # Output: True


### **8. Find the Length of a Set**  

my_set = {1, 2, 3, 4}
print(len(my_set))


### **9. Find the Union of Two Sets**  

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # or set1.union(set2)


### **10. Find the Intersection of Two Sets**  

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 & set2)  # or set1.intersection(set2)




### **Advanced Set Problems**  
### **11. Find the Difference of Two Sets**  

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 - set2)  # or set1.difference(set2)


### **12. Find the Symmetric Difference of Two Sets**  

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 ^ set2)  # or set1.symmetric_difference(set2)


### **13. Convert a List to a Set (Remove Duplicates)**  

my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)


### **14. Iterate Over a Set**  

my_set = {1, 2, 3}
for item in my_set:
    print(item)


### **15. Check if a Set is a Subset of Another**  

set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))




### **Real-World Set Problems**  
### **16. Check if a Set is a Superset of Another**  

set1 = {1, 2, 3, 4}
set2 = {2, 3}
print(set1.issuperset(set2))


### **17. Find Unique Characters in a String**  

string = "hello"
unique_chars = set(string)
print(unique_chars)


### **18. Remove All Elements from a Set**  

my_set = {1, 2, 3}
my_set.clear()
print(my_set)


### **19. Create a Frozen Set (Immutable Set)**  

frozen = frozenset([1, 2, 3, 4])
print(frozen)


### **20. Convert Set to List**  

my_set = {1, 2, 3}
my_list = list(my_set)
print(my_list)


