import math

inputed = raw_input("""Which calculator do you want to use?"
                  A = divisors
                  B = primes
                  C = gcd""")
def divisors(n):
        listed = range(1, n + 1)
        listed = filter(lambda x: n % x == 0, listed)
        return listed


def primes(a):
    list1 = range(1, a)
    list1 = filter(lambda x: len(divisors(x)) == 2, list1)
    print list1

def gcd(a, b):
    '''

    :param a: first number
    :param b: second number
    :return: the greatest common divisor of the two numbers
    '''
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print(a)

while True:
    if inputed == "C":
        input1 = input("input? ")
        input2 = input("input? ")
        gcd(input1, input2)
    if inputed == "A":
        input1 = input("input? ")
        print divisors(input1)
    else:
        input1 = input("input? ")
        primes(input1)









