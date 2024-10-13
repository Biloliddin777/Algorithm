'''
Linear Search
Binearch Search
Stack
Queue
LList
HashMap
'''


# def linear_search(arr, target):
#     for item in arr:
#         if item == target:
#             return arr.index(item)
#
#     return None
#
#
# arr = [42, 24, 12, 56, 10, 28, 67]
#
# result = linear_search(arr,28)
# print(result)

# ============        Binary Search =============


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        med = (low + high) // 2
        if arr[med] == target:
            return med

        elif arr[med] > target:
            high = med - 1

        elif arr[med] < target:
            low = med + 1


arr = [10, 20, 30, 40, 50, 60, 70]

print(binary_search(arr, 60))


