def heapify(arr: list, n: int, i: int):
    largest = i  # initialize largest as root
    l = 2 * i + 1
    r = 2 * i + 2

    # see if left child of root exist and is greater than root
    if (l < n) and (arr[i] < arr[l]):
        largest = l
    # see if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # heapify
        heapify(arr, n, largest)
    return arr


def headSort(arr: list):
    n = len(arr)

    # Building max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # one by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
headSort(arr)

print(" Sorted array is : ")
for i in range(len(arr)):
    print("%d" %arr[i], end=" ")