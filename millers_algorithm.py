import random
import math


def is_prime(n):
    if n == 0: return False
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.sqrt(n)+1), 2):
        if n % i == 0: return False
    return True


def is_prime_miller(n):
    if n == 0: return False
    if n == 1: return False
    if n == 2: return True
    for i in range(20):
        b = random.randrange(2, n)
        ok = miller_test(n, b)
        if not ok:
            return False
    return True


def miller_test(n, b):
    new_n = n - 1
    s = 0
    t = 0

    while new_n % 2 == 0:
        new_n //= 2
        s += 1

    t = new_n

    if pow(b, t, n) == 1:
        return True

    for j in range(s):
        if pow(b, t, n) == n-1:
            return True
        t *= 2
    return False

t = 0
t2 = 0

for i in range(1_000_000):
    if (is_prime(i)):
        t += 1
    if (is_prime_miller(i)):
        t2 += 1

print(f"Primes: {t}")
print(f"Primes Miller: {t2}")

print(is_prime_miller(88751729846543208193105697151017841888649839985786772126296814288448804560578657878963832048309226653892515424593048648681178010432724394362416928631307382081040984765505650453940146489888213277575077))
