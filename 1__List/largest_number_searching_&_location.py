# Sample list
numbers = [10, 5, 20, 15, 30, 25, 30, 40, 5, 40]
print(len(numbers))

## Initialize variables to store the largest number and its location
largest_number = numbers[0]
location = 0
#
## Iterate through the list using a for loop
                  # 10
for i in range(1, len(numbers)):
   if numbers[i] > largest_number:
        largest_number = numbers[i]
        location = i

print(f"The largest number is {largest_number} at index {location}")