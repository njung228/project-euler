"""For a six digit number, which the largest palindromic product of 2 3 digit numbers is likely to be, if it is palindromic, it is divisible by 11 because of the divisibility test for 11.
Additionally, I will assume the product begins and therefore ends with a 9, meaning the 2 factors must end in either 9 and 1, or 3 and 3. 
979 and 913 are the only 2 numbers above 900 that end in 9, 1, or 3 and are divisible by 11, and I only checked across that list.

"""

def is_palindrome(n):
    return str(n) == str(n)[::-1]

list = [979, 913]

def largest_palindromic_product():
    for i in list:
        for k in range (900, 1000):
            if is_palindrome(i * k):
                return i*k


largest_palindromic_product()
