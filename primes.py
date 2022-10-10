"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Inappropriate amount")
    list = []
    i = 0
    num = 2
    num2 = num//2
    while i in range(number_of_primes):
        for num2 in range(2, num):
            if (num % num2) == 0:
                num += 1
                break
        else:
            list.insert(i, num)
            i += 1
            num += 1
    print(list)
    return list


print(27//2)
primes(10)
