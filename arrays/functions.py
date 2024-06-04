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
    for e in arr:  #  O(n)
        if e == value:  # O(1)
            return e  # O(1)
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
