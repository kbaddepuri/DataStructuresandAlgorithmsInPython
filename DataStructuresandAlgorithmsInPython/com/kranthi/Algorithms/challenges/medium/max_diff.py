def diff(arr, n):
    max_diff = arr[1] - arr[0]
    min_elem = arr[0]

    for i in range(1, n):
        if arr[i] - min_elem > max_diff:
            max_diff = arr[i] - min_elem

        if min_elem > arr[i]:
            min_elem = arr[i]

    return max_diff


print(diff([1,2,3,4,-10,6,10], 7))