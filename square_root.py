def square_root(n):
    for i in range(0, n+1):
        if (i*i) > n:
            return i, False
        if(i*i) == n:
            return i, True
    return False

print(square_root(35))

def is_prime(n): 
    if (n < 2):
        return False
    for i in range(2,int(n**0.5)+1):
        if (n % i) == 0:
            return False
    return True