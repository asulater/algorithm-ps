# 5) Greatest Common Divisor

def gcd(a, b):
    i = min(a, b) # Find the minimum value out of the two numbers
    while True:
        if a % i == 0  and b % i == 0 :
            return i
        i = i - 1

print(gcd(1, 5))
print(gcd(3, 6))
print(gcd(60, 24))



# 5-1) Euclid algorithm

def eu_gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)