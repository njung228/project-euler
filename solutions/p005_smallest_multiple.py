"""For a number to be divisible by all of the numbers from 1 through 20, it needs to have all the prime factors of those numbers present, matching the highest power that is present in the factors of numbers 1 through 20. 
These are 2 to the 4th power (16), 3 squared (9), 5, 7, 11, 13, 17, and 19. We can just multiply these together to find the smallest positive number that is divisible.
For example, for a number to be divisible by 20, it must be divisible by 2 squared and 5, both of which are satisfied.
"""


def smallest_multiple():
    return (2**4) * (3**2) * 5 * 7 * 11 * 13 * 17 * 19