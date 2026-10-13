def factorize(n):
    list = []
    if n == 1:
        return [1]
    else:
        for i in range(int((n ** 0.5) // 1)):
            if n % (i + 1) == 0: 
                list += [i+1 , int(n / (i + 1))]
    return list

def is_prime(n):
    if len(factorize(n)) == 2:
        return True

def largest_prime(L):
    L.sort(reverse = True)
    for i in (L):
        if is_prime(i) == True:
            return i


def largest_prime_factor(n):
    list = factorize(n)
    print(largest_prime(list))