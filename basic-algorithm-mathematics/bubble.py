# 12) Bubble Sort

d = [2, 4, 5, 1, 3]

def bsort(a):
    n = len(a)
    while True:
        changed = False
        for i in range(0, n - 1):
            if a[i] > a[i + 1]:
                print(a)
                a[i], a[i + 1] = a[i + 1], a[i]
                changed = True
        if changed == False:
            return

bsort(d)

print(d)

