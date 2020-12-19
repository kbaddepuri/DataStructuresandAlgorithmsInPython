def heapify(array: list, n: int, ith: int):
    largest = ith  # initialize largest as root
    l = 2 * ith + 1
    r = 2 * ith + 2

    # see if left child of root exist and is greater than root
    if (l < n) and (array[largest] < array[l]):
        largest = l
    # see if right child of root exists and is greater than root
    if r < n and array[largest] < array[r]:
        largest = r

    # change root, if needed
    if largest != ith:
        array[ith], array[largest] = array[largest], array[ith]  # swap

        # heapify
        heapify(array, n, largest)
    return array


def headSort(arry: list):
    n = len(arry)

    # Building max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arry, n, i)

    # one by one extract elements
    for i in range(n - 1, 0, -1):
        arry[i], arry[0] = arry[0], arry[i]
        heapify(arry, i, 0)


arr = [12, 11, 13, 5, 6, 7]
headSort(arr)

print(" Sorted array is : ")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
