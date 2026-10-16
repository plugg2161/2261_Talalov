n = input()
if '.' not in n:
    print(n + " rub " + '0'+ " kop")
    exit()
a = n.replace('.', ' ').split()
b = a[1]
if len(b) == 1:
    b += '0'
    print(a[0] + " rub " + b + " kop")
    exit()
if b[0] == '0':
        print(a[0] + " rub " + b[1] + " kop")
        exit()
else:
    print(a[0] + " rub " + b + " kop")

