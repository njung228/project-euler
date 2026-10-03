def prime_factorize(n):
    list = []
    if n == 1:
        return [1]
    else:
        for i in range(int((n ** 0.5) // 1)):
            if n % (i + 1) == 0:
                list.append([i + 1]) 
    return list 

def largest_prime_factor(n):
    return max(prime_factorize(n))  

largest_prime_factor(600651475143)    
            