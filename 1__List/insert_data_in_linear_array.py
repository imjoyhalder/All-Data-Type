# Create an array with some initial data
my_array = [10, 20, 30, 40, 50]

# Insert data at a specific index
index_to_insert = 2  # Insert at index 2
value_to_insert = 25

# Check if the index is within the bounds of the array
if 0 <= index_to_insert <= len(my_array):
    # Shift elements to the right to make space for the new data
    my_array.append(None)  # Add a placeholder element at the end
    for i in range(len(my_array) - 1, index_to_insert, -1):
        my_array[i] = my_array[i - 1]
    my_array[index_to_insert] = value_to_insert
    print("Data inserted successfully:", my_array)
else:
    print("Invalid index. Cannot insert data at this index.")
