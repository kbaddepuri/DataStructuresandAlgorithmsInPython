"""
Watch this video for more understanding of Quick sort
overall: it works based on selecting  the pivot and arranging all values less than pivot at left side of the pivot
and all values which are greater than pivot at right side of the pivot value.
Once done, Pivot value will be in the middle of the array and same process needs to be applied for left and right
side of the array
https://www.youtube.com/watch?v=0SkOjNaO1XY
"""


def quickSort(array, l, r):
    if l >= r:
        return

    pivot = partition(array, l, r)

    quickSort(array, l, pivot - 1)
    quickSort(array, pivot + 1, r)


def partition(array, l, r):
    # In general, we can select pivot number randomly, but simplicity is to select last value of the array
    pivot = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # swap the i+1 value with pivot
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


arr = [6, -8, 0, 8, -2, 5, 7]
quickSort(arr, 0, len(arr) - 1)
print(arr)
