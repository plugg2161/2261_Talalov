s1 = '1234567890'
s2 = 'qwertyuiop'
s3 = 'asdfghjkl'
s4 = 'zxcvbnm'
n = int(input())
lines = [input() for _ in range(n)]
for i in lines:
    bools1 = False
    bools2 = False
    bools3 = False
    bools4 = False
    for char in i:
        if char in s1:
            bools1 = True
        elif char in s2:
            bools2 = True
        elif char in s3:
            bools3 = True
        elif char in s4:
            bools4 = True
    if bools1 and bools2 and bools3 and bools4:
        print('strong')
    else:
        print('weak')
