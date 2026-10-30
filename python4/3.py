t = int(input())
arr = []
for _ in range(t):
    line = [int(x) for x in input().split()]
    
    p1, q1 = line[0], line[1]
    p2, q2 = line[2], line[3]
    p3, q3 = line[4], line[5]
    p4, q4 = line[6], line[7]
    left = (p1 * q2 + p2 * q1) * (q3 * q4)
    right = (p3 * q4 + p4 * q3) * (q1 * q2)
    
    if left > right:
        arr.append("1")
    elif left < right:
        arr.append("-1")
    else:
        arr.append("0")

print(*arr)
