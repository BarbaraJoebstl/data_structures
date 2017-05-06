def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while low <= high:
        half = (low + high) / 2
        if input_array[half] == value:
            return half
        elif input_array[half] < value:
            low = half + 1
        else:
            high = half - 1

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
