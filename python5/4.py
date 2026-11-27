n, m = map(int, input().split())

matrix = []
for _ in range(n):
    row = input().split()
    matrix.append(row)
for j in range(m):
    transposed_row = [matrix[i][j] for i in range(n)]
    print(*transposed_row)
