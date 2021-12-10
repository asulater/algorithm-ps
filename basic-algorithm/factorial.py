# 4) factorial algorithm

def fact(n):
    sum = 1
    for i in range(1, n + 1):
        sum = sum * i
    return sum

print(fact(1))
print(fact(5))



# 4-1) recursive call

# def hello(): # Calling functions infinitely
#     print("Hello") 
#     hello()

# hello()



# 4-2) recursive factorial 
# 1! = 1  //  2! = 2 x 1 = 2 x 1!  //  3! = 3 x (2 x 1) = 3 x 2!

def re_fact(n):
    if n <= 1:  # Termination conditions
        return 1
    return n * re_fact(n - 1)

print(re_fact(2))
print(re_fact(5))


# 4-3) Find the sum from 1 to n (use recursive call)

def re_sum(n):
    if n == 0:
        return 0
    return n + re_sum(n - 1)

print(re_sum(100))


# 4-4) Find the maximum value of the list (use recursive call)

v = [17, 92, 18, 33, 58, 7, 33, 42] # List


def re_max(a, n):
    if n == 1:
        return a[0]
    max_n_1 = re_max(a, n - 1)
    if max_n_1 > a[n - 1]:
        return max_n_1
    else:
        return a[n - 1]

print(re_max(v, len(v)))