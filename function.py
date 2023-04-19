# Write a program to create a function that takes two arguments, 
# name and age, and print their value.
def person(name,age):
        print(name,age)

# Create a function  that can pass any number of arguments to this function.
def numbers(*args):
    sum = 0
    for i in args:
        print(i)

#find the largest item from a given list
y = [6,7,3,6,2,11,2]
print(max(y))