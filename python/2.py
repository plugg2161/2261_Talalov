n = str(input())
a = len(n)
b = a // 2
first = n[0:b]
second = n[b:a]

print(int(first) + int(second))
