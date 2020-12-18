def recursiveBinarySearch(array, lowerIndex, higherIndex, key):
    if higherIndex >= lowerIndex:
        # https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
        mid = lowerIndex + (higherIndex - lowerIndex) // 2
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            higherIndex = mid -1
            return recursiveBinarySearch(array, lowerIndex, higherIndex, key)
        else:
            lowerIndex = mid + 1
            return recursiveBinarySearch(array, lowerIndex, higherIndex, key)
    else:
        return -1
