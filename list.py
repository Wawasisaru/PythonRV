# # append()
# # used to add one element into a list
list = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
list.append("nancy")
print(list)

# .extend()
# it adds a new list to the current list
fruits = ["mango","banana","apple","orange","kiwi","berry"]
fruits2=("pinnaple","watermelon")
fruits.extend(fruits2)
print(fruits)

# .sort()
# sorts the items in a list
fruits = ["mango","banana","apple","orange","kiwi","berry"]
fruits.sort()
print(fruits)

# .pop()
# removes the item at a given position in a list
fruits = ["mango","banana","apple","orange","kiwi","berry"]
fruits.pop()
print(fruits)

# .count()
# it returns the number of times the item appers
fruits = ["mango","banana","apple","orange","kiwi","berry"]
fruits.count("apple")
print(fruits)

# .insert()
# insert an item at a given position
fruits = ["mango","banana","apple","orange","kiwi","berry"]
fruits.insert(0,"pinnnapple")
print(fruits)

# index
# returns the index position of a given element
fruits = ["mango","banana","apple","orange","kiwi","berry"]
print(fruits.index("apple"))

# list in comprehension
fruits = ["mango","banana","apple","orange","kiwi","berry"]
fruits2 = []
for x in fruits:
    if "a" in x:
        fruits2.append(x)
        print(fruits2)