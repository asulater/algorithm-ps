# 1) Find the sum from 1 to n.

def sum(n):
    return n * (n+1) // 2 # // = Integer

# print(sum(10)) # result



# 1-1) The sum of squares of consecutive numbers from 1 to n.

# def sum_sq(n):
#     res = 0
#     for i in range(1, n+1):
#        res += i ** 2
#     return res

def sum_sq(n):
    return n * (n+1) * (2 * n +1) // 6

print(sum_sq(100)) # result

