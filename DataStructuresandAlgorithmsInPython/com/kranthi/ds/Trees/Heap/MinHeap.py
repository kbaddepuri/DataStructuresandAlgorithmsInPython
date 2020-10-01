"""
Sort a nearly sorted (or K sorted) array

Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that
sorts in O(n log k) time. For example, let us consider k is 2, an element at index 7 in the sorted array,
can be at indexes 5, 6, 7, 8, 9 in the given array. """

from heapq import heapify, heappush, heappop


def sortingUsingMinHeap(array: list, size: int, k_elem: int) -> list:
    # list of first k+1 items
    heap = array[:k_elem + 1]

    # heapify to convert list to min heap
    heapify(heap)

    # pop data and heapify remaining element after inserting into heap

    target_index = 0
    for rem_elem_idx in range(k_elem + 1, size):
        array[target_index] = heappop(heap)
        heappush(heap, array[rem_elem_idx])
        target_index += 1

    while heap:
        array[target_index] = heappop(heap)
        target_index += 1

    return array


arr = [2, 6, 3, 12, 56, 8]
n = len(arr)
k = 3
print(sortingUsingMinHeap(arr, n, k))
