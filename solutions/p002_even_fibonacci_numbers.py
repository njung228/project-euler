"""To solve this problem, we need to find the sum of all even fibonacci numbers under four million.
To do this, I simply create a list of fibonacci numbers up to n, and I add only the elements of the list that are even.
"""

def fib_list_up_to_n(n):
    list = [1, 2]
    while list[-1] + list[-2] <= n:
        list.append(list[-1] + list[-2])
    return list

def even_fibonacci_numbers(n):
    list = fib_list_up_to_n(n)
    sum = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            sum += list[i]
    return sum




