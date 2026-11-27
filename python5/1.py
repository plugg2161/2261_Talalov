n = int(input())
arr = list(map(int, input().split()))
arr.sort(key=lambda x: (abs(x), x))
print(*arr)
