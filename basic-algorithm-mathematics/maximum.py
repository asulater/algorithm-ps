# 2) Find the maximum value of the list.

v = [17, 92, 18, 33, 58, 7, 33, 42] # List


# def find_max(a):
#     n = len(a)
#     max_v = a[0]
#     for i in range(1, n):
#         if a[i] > max_v:
#             max_v = a[i]
#     return max_v
             

# print(find_max(v))


# 2-1) Find the location of the maximum value

# def find_max_idx(a):
#     n = len(a)
#     max_idx = 0
#     for i in range(1, n):
#         if a[i] > a[max_idx]:
#             max_idx = i
#     return max_idx

# print(find_max_idx(v))


# 2-2) Algorithm to find the minimum value

def find_min(a):
    n = len(a)
    min_v = a[0]
    for i in range(1, n):
        if min_v > a[i]:
            min_v = a[i]
    return min_v

print(find_min(v))
