# 8) Selection Sort

d = [2, 4, 5, 1, 3]

# def find_min_idx(a):
#     n = len(a)
#     min_idx = 0
#     for i in range(1, n):
#         if a[i] < a[min_idx]:
#             min_idx = i
#     return min_idx

# def sel_sort(a):
#     result = []
#     while a:
#         min_idx = find_min_idx(a)
#         value = a.pop(min_idx)
#         result.append(value)
#     return result

# print(sel_sort(d))


def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
                a[i], a[min_idx] = a[min_idx], a[i]

sel_sort(d)
print(d)