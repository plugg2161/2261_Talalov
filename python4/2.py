n = int(input())
dress = list(map(int, input().split()))

arr = set()
res = n
for day in range(n):
    arr.add(dress[day])
    if len(arr) == 3:
        res = day + 1
        break
print(res)
