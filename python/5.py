n, m, c, k = map(int, input().split())
papers1 = n*m
papers = papers1 - k
pack = (papers + 199) // 200
res = pack *c
print(res)
