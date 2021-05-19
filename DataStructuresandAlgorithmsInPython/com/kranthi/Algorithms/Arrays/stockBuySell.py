
def stockBuySell(price):
    n = len(price)

    if n == 1:
        return
    i = 0

    while i < n-1:
        #find local minima note that limit is n-2 as we are  comparing wth next element
        while ((i < n-1) and (price[i+1] <= price[i])):
            i += 1

        if (i == n -1):
            break

        buy = i
        i += 1

        # find local maxima
        while ((i < n) and (price[i] >= price[i-1])):
            i += 1

        sell = i - 1

        print("Buy on day: {}\t sell on day: {}".format(buy, sell))

price = [100, 180, 260, 310, 40, 535, 695]
stockBuySell(price)