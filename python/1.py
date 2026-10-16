n = int(input())
a = ((n-1)// 15)*15
b = n -a
if b == 15:
    print(a+b, '0')
else:
    print(a, b)
