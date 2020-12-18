from binary_search import recursiveBinarySearch


arr = [1, 2, 3, 4, 5, 6]
result = recursiveBinarySearch(arr, 0, len(arr)-1, 6)
if result == -1:
    print('Element not present')
else:
    print('Element in position', result)