"""
Write a program to calculate GCD (greatest decimal count) for the given array

"""

def generalizedGCD(num, arr):
    indx = 0
    while indx < num:
        n_arr = [0 if i % arr[indx] == 0 else i % arr[indx] for i in arr]
        if len(set(n_arr)) == 1 and n_arr[0] == 0:
            return arr[indx]
        else:
            indx += 1
    return 1

generalizedGCD(5, [2,4,6,8,10])