# 1st Find the sum from 1 to n.

def sum(n):
    return n * (n+1) // 2 # // = Integer

# print(sum(10)) # result



# The sum of squares of consecutive numbers from 1 to n.

def sum(n):
    res = 0
    for i in range(1, n+1):
       res += i ** 2
    return res

print(sum(10)) # result