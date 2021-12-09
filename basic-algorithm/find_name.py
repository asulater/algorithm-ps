def find_same_name(a):
    n = len(a)
    res = set()
    for i in range(0, n-1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                res.add(a[i])
    return res


name = ["Tom", "Jerry", "Mike", "Tom"]

print(find_same_name(name))