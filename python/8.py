a = input()
arr = []
for i in range(0, len(a)):
    if a[i].isdigit():
        arr.append(int(a[i]))
print(sum(arr))
