numbers = list(map(int, input().split()))

for num in numbers:
    if num < 0:
        print(f"отрицательное число: {num}")
        break
else:
    print("Все числа в последовательности неотрицательные")
