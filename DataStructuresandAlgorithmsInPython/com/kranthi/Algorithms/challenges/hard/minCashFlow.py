
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