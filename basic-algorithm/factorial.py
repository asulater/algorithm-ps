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


# 4-3) Find the sum from 1 to n (Use recursive call)

def re_sum(n):
    if n <= 1:
        return 1
    return n + re_sum(n - 1)

print(re_sum(100))