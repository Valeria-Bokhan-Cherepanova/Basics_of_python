#Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()

el_count = int(input("State the number of elements in the list "))
the_list = []
i = 0
el = 0
while i < el_count:
    the_list.append(input("Enter the following list value "))
    i += 1

for elem in range(int(len(the_list)/2)):
        the_list[el], the_list[el + 1] = the_list [el + 1], the_list[el]
        el += 2
print(the_list)