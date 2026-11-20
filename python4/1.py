n = int(input())

count = 0
x = 1
while count < n:
  x += 1
  prime = True
  for i in range(2, int(x**0.5) + 1):
    if x % i == 0:
      prime = False
      break
  if prime: 
    count += 1

print(x)
