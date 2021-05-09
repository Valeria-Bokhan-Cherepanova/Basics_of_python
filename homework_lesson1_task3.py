n = int(input("Enter the number - "))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
total = (temp, t1, t2)
sum = n + int(t1) +  int(t2)
print(total, sum)

n = input('Enter the number -')
print(f'{n} + {n + n} + {n +n +n}) = {int(n) + int(n + n) + int(n + n + n)}')


