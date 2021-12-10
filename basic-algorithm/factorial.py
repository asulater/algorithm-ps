# 4) factorial algorithm

def fact(n):
    sum = 1
    for i in range(1, n + 1):
        sum = sum * i
    return sum

print(fact(1))
print(fact(5))



# 4-1) recursive call

def hello(): # Calling functions infinitely
    print("Hello") 
    hello()

hello()



# 4-2) recursive factorial 