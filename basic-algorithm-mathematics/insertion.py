# 9) Insertion sort

# def find_ins_idx(r, v):
#     for i in range(0, len(r)):
#         print("value = {} , r[i] = {} " .format(v, r[i]))
#         if v < r[i]:
#             return i
#     return len(r)

# def ins_sort(a):
#     result = []
#     while a:
#         value = a.pop(0)
#         print("Value : {}" .format(value))
#         ins_idx = find_ins_idx(result, value)
#         result.insert(ins_idx, value)
#     return result

d = [2, 4, 5, 1, 3]
# print(ins_sort(d))


def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        print("i = {} / j = {} / key = {}" .format(i, j, key))
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            print("a[j+1] = {} / a[j] = {}" .format(a[j+1], a[j]))
            j -= 1
            print("j = {}" .format(j))
        a[j + 1] = key

ins_sort(d)
print(d)