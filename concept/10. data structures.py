
#List

my_list = ["apple", "banana","cherry","date"]

first_element = my_list[0]
print("first element: ", first_element)

my_list[1] = "blueberry"
print("Modified list: ",my_list)

my_list.append("elderberry")
print("List after appending an element: ",my_list)

my_list.insert(2,"fig")
print("List after inserting an element: ", my_list)

my_list.remove("cherry")
print("List after removing an element:", my_list)

popped_element = my_list.pop()
print("Popped element: ", popped_element)
print("List after popping an element: ",my_list)

popped_index_element=my_list.pop(1)
print("Popped element at index 1: ", popped_index_element)
print("List after popping an element at index 1: ",my_list)

index_of_apple=my_list.index("apple")
print("Index of 'apple': ", index_of_apple)

count_of_fig=my_list.count("fig")
print("Count of 'fig': ", count_of_fig)

my_list.sort()
print("Sorted list: ",my_list)

my_list.reverse()
print("Reversed list: ", my_list)

my_list.clear()
print("List after clearing: ",my_list)






#Tuple

my_tuple = ("apple", "banana", "cherry", "date", "elderberry")

first_element=my_tuple[0]
print("First element: ", first_element)

last_element=my_tuple[-1]
print("last element: ", last_element)

sub_tuple=my_tuple[1:4]
print("Sliced tuple: ", sub_tuple)

count_of_cherry = my_tuple.count("cherry")
print("Count of 'cherry': ",count_of_cherry)

index_of_date = my_tuple.index("date")
print("Index of 'date': ", index_of_date)

new_tuple = my_tuple+("Fig","grape")
print("Concantenated tuple:",new_tuple)

repeated_tuple = new_tuple*2
print("Repeated tuple:",repeated_tuple)

isa = "apple" in my_tuple
print("Is 'apple' in the tuple?:",isa)

f1,f2,f3,f4,f5=my_tuple
print("Unpacked elements:",f1,f2,f3,f4,f5)

tl = len(my_tuple)
print("Length of the tuple:",tl)





#Sets

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print("Set 1: ", set1)
print("Set 2: ", set2)

union_set=set1.union(set2)
print("Union of set 1 and set 2: ",union_set)

intersection_set = set1.intersection(set2)
print("Intersection of set 1 and set 2: ", intersection_set)

difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)
print("Difference of set 1 from set 2: ", difference_set1)
print("Difference of set 2 from set 1: ", difference_set2)

sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric difference f set 1 and set 2: ", sym_diff_set)

set1.add(9)
print("Set 1 after adding 9: ", set1)

set1.remove(9)
print("Set 1 after removing 9: ", set1)

set1.discard(10)
print("Set 1 after discarding 10:", set1)

print("Is set 1 a subset of set 2? ", set1.issubset(set2))
print("Is set 2 a superset of set 1? ", set2.issuperset(set1))

set1.clear()
print("Set 1 after clearing: ", set1)

copy_set2=set2.copy()
print("Copied Set 2: ",copy_set2)




#Dictionaries

my_dict = {
    "name": "Alice",
    "age":30,
    "city":"New York" }

print("Initial dictionary: ",my_dict)

name=my_dict["name"]
age=my_dict["age"]
print("Name: ", name)
print("Age: ",age)

my_dict["email"]="alice@example.com"
my_dict["age"]=31
print("Updated dictionary:",my_dict)

del my_dict["email"]
removed_age=my_dict.pop("age")
print("Removed age: ", removed_age)
print("Dictionary after removal: ",my_dict)

print("Iterating over a dictionary:")
for key in my_dict:
    print(key,":",my_dict[key])

print("Iterating over items:")
for key,value in my_dict.items():
    print(key,":",value)

if name in my_dict:
    print("Name is present in the dictionary")

if "email" not in my_dict:
    print("Email is not present in the dictionary")

length=len(my_dict)
print("Number of items in the dictionary:",length)

copy_dict=my_dict.copy()
print("Original Dictioanary:",my_dict)
print("Copied Dictionary:",copy_dict)

