import math
x, y = map(float, input().split())
k = math.floor(y) - math.ceil(x)
print(k)
