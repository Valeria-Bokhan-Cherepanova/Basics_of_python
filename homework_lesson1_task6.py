a = int(input('Enter the results of the first day run: '))
b = int(input('Enter the desired result: '))
i = 1
while a < b:
    a = a + 0.1 * a
    i += 1
print(f'You will achieve your desired result on %.d day' % i)




