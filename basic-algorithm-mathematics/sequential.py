# 7) sequential search

v = [17, 92, 18, 33, 58, 7, 33] # List

def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return a[i], i
    return -1

print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))

# 7-1) 

def search_list2(a, x):
    n = len(a)
    temp = []
    for i in range(0, n):
        if x == a[i]:
            temp.append(i)
    return temp

print(search_list2(v, 18))
print(search_list2(v, 900))


# 7-2) 

stu_no = [39, 14, 67, 105]
stu_name  = ["Justin", "John", "Mike", "Summer"]

def stu_search(a, b, c):
    for i in range(0, len(b)):
        if a == b[i]:
            return c[i]
    return "?"

print(stu_search(39, stu_no, stu_name))
print(stu_search(900, stu_no, stu_name))
print(stu_search(105, stu_no, stu_name))