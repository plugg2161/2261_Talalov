n = int(input())
x = [int(input()) for _ in range(n)]
dasha = 0
masha = 0
for i in x:
    if i % 3 == 0:
        masha += 2
    else:
        dasha += 1
print(str(masha) + ':' + str(dasha))
