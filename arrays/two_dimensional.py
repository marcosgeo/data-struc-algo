
# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np

# complexity: O(m*n)
two_d_array = np.array([
    [11, 15, 10, 6], [10, 14, 11, 6], [12, 17, 12, 8], [15, 18, 14, 9]
])
print(f"\ntwo dimensional array\n{two_d_array}\n")


# inserting a column
new_two_d = np.insert(two_d_array, 0, [[1, 2, 3, 4]], axis=1)
print(f"\nadded new column:\n{new_two_d}\n")

# inserting a row
new_two_d = np.insert(two_d_array, 0, [[1, 2, 3, 4]], axis=0)
print(f"\nadded new row:\n{new_two_d}\n")


# accessing elements
def access_elem(arr, row, col):
    if row >= len(arr) and col >= len(arr[0]):  # O(1)
        raise IndexError("Incorrect index")     # O(1)
    return arr[row][col]  # O(1)
    # time complexity: O(1)
    # space complexity: O(1)


print(f"value found: {access_elem(two_d_array, 2, 3)}")


print(f"\ntraversing\n")

# traversing
def traverse(arr):
    for i in range(len(arr)):  # O(m*n)
        for j in range(len(arr[0])):  # O(n)
            print(arr[i][j])  # O(1)
    # time complexity: O(m*n), for m != n
    #                : O(n²), for m = n


traverse(two_d_array)


# searching (linear)
def search(arr, value):
    for i in range(len(arr)):  # O(m*n)
        for j in range(len(arr[0])):  # O(n)
            if arr[i][j] == value:  # O(1)
                return f"The value was found at: {i}, {j}"  # O(1)
    return "The value was not found"  # O(1)
    # time complexity: O(m*n)
    # space complexity: O(1)


print(f"\nsearching\narray: {two_d_array}")
print(search(two_d_array, 18))
print(search(two_d_array, 100))


# deleting a column
# numpy array delete fucntion works by creating a new array without the deleted column
print(f"original array:\n{two_d_array}")
new_array = np.delete(two_d_array, 1, axis=1)
print(f"new array with column #2 removed:\n{new_array}")

# deleting a row
new_array = np.delete(two_d_array, 1, axis=0)
print(f"new array with row #2 removed:\n{new_array}")

# the operations above are time and space complexity O(m*n)


