
def binarySearchUsingWhile(arr, key):
    l = 0
    r = len(arr) - 1

    while l < r:
        mid = (l + r) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            r = mid + 1
        else:
            l = mid - 1

def binarysearch(arr, l, r, key):
    if r >= l:
        mid = (l + r) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binarysearch(arr, l, mid - 1, key)
        else:
            return binarysearch(arr, mid + 1, r, key)

    else:
         return -1
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binarysearch(arr, 0, len(arr)-1, x)

if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")