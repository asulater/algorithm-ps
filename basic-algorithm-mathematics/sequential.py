# 7) sequential search

v = [17, 92, 18, 33, 58, 7, 33, 42] # List

def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return a[i], i
    return -1

print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))
