# 13) Binary Search

def binary_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
        
    return -1

d  = [1, 4, 9, 16, 25, 36, 49, 64, 81]

print(binary_search(d, 36))
print(binary_search(d, 50))



# 13-1) Binary Search (use recursive call)

def binary_search_sub(a, x, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search_sub(a, x, mid + 1, end)
    else:
        return binary_search_sub(a, x, start, mid - 1)
    return -1

def b_search(a, x):
    return binary_search_sub(a, x, 0, len(a) - 1)

print(b_search(d, 36))
print(b_search(d, 50))

