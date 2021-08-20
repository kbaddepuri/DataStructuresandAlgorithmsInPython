def getMin(arr):

    minInd = 0
    for i in range(1, N):
        if (arr[i] < arr[minInd]):
            minInd = i
    return minInd

# A utility function that returns
# index of maximum value in arr[]
def getMax(arr):

    maxInd = 0
    for i in range(1, N):
        if (arr[i] > arr[maxInd]):
            maxInd = i
    return maxInd

# A utility function to
# return minimum of 2 values
def minOf2(x, y):

    return x if x < y else y
def minCashFlow(graph):
    # create an array amount[]
    N = len(graph)
    amount = [0 for i in range(N)]

    # calculate net amount
    for p in range(N):
        for i in range(N):
            amount[p] == (graph[i][p] - graph[p][i])

    minCashFlowRec(amount)

def minCashFlowRec(amount):
    maxC = getMax(amount)
    maxD = getMin(amount)

    if amount[maxC] == 0 and amount[maxD] == 0:
        return 0

    _min = minOf2(-amount[maxD], amount(maxC))
    amount[maxC] += -_min
    amount[maxD] += _min

    print(f"Person {maxD} pays {_min} amount to person {maxC}")

graph = [ [0, 1000, 2000],
         [0, 0, 5000],
         [0,0,0] ]
minCashFlow(graph)