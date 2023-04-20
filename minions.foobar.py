#Adrian Munene Bikuri
#Foobar Challenge 1 - Day 1 - 19/04/2023
def solution(i):
    primes = '';
    count = 0
    def is_prime(n):
        if (n < 2):
            return False
        for i in range(2,int(n**0.5)+1):
            if (n % i) == 0:
                return False
        return True
    while(len(primes) < i+5):
        if is_prime(count):
            primes += str(count)
        count += 1
    id = primes[i:i+5]
    return id
