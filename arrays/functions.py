import array
import numpy as np

my_array = array.array('i')

# array.array(data_type: str, items_list: list)
my_array2 = array.array('i', [1, 2, 3, 4])  # time complexity: O(n)
print(my_array2)

np_array = np.array([], dtype=int)  # time complexity: O(1); space complexity: O(1)

np_array2 = np.array([1, 2, 3, 4])  # time complexity: O(n); space complexity: O(n)


## inserting
my_array2.insert(0, 6)  # time complexity: O(n); space complexity: O(1)


## operations

# traverse
def traverse_array(arr):
    for i in arr:  # O(n)
        print(i)   # O(1)
    #  full array: O(n)


# accessing
def access_elem(arr, index):
    if index >= len(arr):  # time complexity: O(1)
        print("There is not any element with this index")  # O(1)
    else:
        print(arr[index])  # time complexity: O(1)

    # full method complexity: time O(1), space: O(1)


# linear search
def search_elem(arr, value):
    for i, _ in enumerate(arr):  #  O(n)
        if arr[i] == value:  # O(1)
            return i  # O(1)
    return -1  # O(1)

    # full method: time O(n)
    # space complexity is O(1) since no additional space is required


# delete element
def remove_elem(arr, value):
    for i in range(len(arr)):  # O(n)
        if arr[i] == value:  # O(1)
            arr.remove(i)  # O(1)
    # time complexity: O(n)
    # space complexity: O(1)


# memory info (position and length
def buffer_info(arr: array.array):
    print(arr.buffer_info)  # (1408482404w34, 11)


# converting and creating from bytes
def converting(arr: array.array):
    _bytes = arr.tobytes()
    print(_bytes)
    _integers = array.array("i")
    _integers.frombytes(_bytes)
    print(_integers)


int_array = array.array("i", [1, 2, 3, 4, 5])
print(converting(int_array))


def missing_number(arr, n):
    # calculate the sum of first n natural numbers using arithmetic progression formula
    total = n * (n + 1) // 2

    # calculates the sum of array
    sum_arr = sum(arr)

    # find the missing number by subtracting sum_arr from total
    missing = total - sum_arr
    return missing

    # the time complexity is O(n) because it iterates through the array once


def integer_pairs(arr: list, target: int) -> list:
    """Find all pairs of integers that sum equals to target"""
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                result.append([i, j])
    return result


def max_product(arr: list) -> int:
    """Returns the max product of the numbers of an array"""
    max1, max2 = 0, 0
    for num in arr:  # O(n), loop through array
        if num > max1:  # O(1), constant time comparison
            max2 = max1  # O(1), constant time assignment
            max1 = num  # O(1), constant time assignment
        elif num > max2:  # O(1)
            max2 = num  # O(1)
    return max1 * max2
    # final complexity: O(n)


def diagonal_sum(arr: list) -> int:
    result = 0
    for i in range(len(arr[0])):
        result += arr[i][i]
    return result


def first_second(arr):
    first = 0
    second = 0
    for value in arr:
        if value > first:
            second = first
            first = value
        elif value > second:
            second = value
    return first, second
    # time complexity: O(n)


def remove_duplicates(arr):
    new_arr = []
    for value in arr:
        if value not in new_arr:
            new_arr.append(value)
    return sorted(new_arr)


def pair_sum(arr: list, target: int) -> list:
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if int(arr[i]) + int(arr[j]) == target:
                result.append(f"{str(arr[i])}+{str(arr[j])}")
    return result


def contains_duplicate(nums: list) -> bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def permutation(list1, list2) -> bool:
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False


def rotate(matrix: list) -> list:
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):  # iterate over the rows
        for j in range(i, n):  # iterates over the columns
            # swap the elements at positions(i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix
