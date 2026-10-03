""" In order to solve this problem, we have to find the sum of all multiples of 3 and 5 under 1000. 
To do this, we can find the sum of all multiples of 3, all multiples of 5, and subtract the doubles counts by subtracting the sum of the multiples of 15.
"""

def multiples_3():
    list = []
    for i in range( 0 // 3, 999 // 3 + 1):
        list.append(i * 3)
    return sum(list)


def multiples_5():
    list = []
    for i in range( 0 // 5, 999 // 5 + 1):
        list.append(i * 5)
    return sum(list)


def multiples_15():
    list = []
    for i in range( 0 // 15, 999 // 15 + 1):
        list.append(i * 15)
    return sum(list)


def multiples_3_and_5():
    return multiples_3() + multiples_5() - multiples_15()

