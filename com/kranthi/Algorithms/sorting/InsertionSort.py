
def insertionSort(arr: list, size: int) -> list:
    i, key, j = 0,0,0
    for i in range(size):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = key

    return arr

arr = [2, 6, 3, 12, 56, 8]
print(insertionSort(arr, len(arr)))