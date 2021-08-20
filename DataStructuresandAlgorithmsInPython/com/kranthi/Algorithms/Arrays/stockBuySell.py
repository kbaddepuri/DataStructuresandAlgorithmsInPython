def stockAndBySell(prices):
    n = len(prices)
    if n == 1:
        return
    i = 0
    profit = 0
    while i < (n-1):
        # find local min
        while i < (n-1) and prices[i + 1] <= prices[i]:
            i += 1
            if i == n-1:
                break
        buy = i
        i += 1

        # find local max
        while i < n and prices[i] >= prices[i-1]:
            i += 1

        sell = i-1

        print(f"Buy on day: {buy} and sell on day: {sell}")
        profit += prices[sell] - prices[buy]
    print(f"profit: {profit}")


price = [100, 180, 260, 310, 40, 535, 695]
stockAndBySell(price)