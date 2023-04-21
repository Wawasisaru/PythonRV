# calculate the average of a list in a number
numbers = [22,34,12,25,77,18]
def numbers():
    sum = 0
    for i in numbers:
        sum = sum + i
    size = len(numbers)
    average = sum / size

    print(average)

# print all odd and even numbers
def even_numbers():
    for i in range(1,10):
        if i%2 == 0:
            print(f"{i} is even number")
        else:
            print(f"{i} is an odd number")

            