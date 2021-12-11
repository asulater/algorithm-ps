# 6) Tower of Hanoi algorithm

'''
The number of disks to move : n 
Current pillar : from_pos
Arrival point pillar to move the disk : to_pos
A pillar to be used in the process of moving : aux_pos
'''

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:  # If there's one disk, just move it.
        print(from_pos, " -> ", to_pos)
        return
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    print(from_pos, " -> ", to_pos)
    hanoi(n - 1, aux_pos, to_pos, from_pos)

print("n = 1")
hanoi(1, 1, 3, 2)
print("*" * 20)
print("n = 2")
hanoi(2, 1, 3, 2)