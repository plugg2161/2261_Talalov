s1 = '1234567890'
s2 = 'qwertuiop'
s3 = 'asdfghjkl'
s4 = 'zxcvbnm'
n = int(input())
lines = [input() for _ in range(n)]
for i in lines:
    if s1 and s2 and s3 and s4 not in i:
        i = 'weak'
    else:
        i = 'strong'
    print(i)
