n = int(input("enter N\n"))
numbers = [i for i in range(n + 1)]
numbers[1] = 0

i = 2
while i <= n:
    if numbers[i] != 0:
        j = i * 2
        while j <= n:
            numbers[j] = 0
            j += i
    i += 1

numbers = [i for i in numbers if i != 0]
print(numbers)