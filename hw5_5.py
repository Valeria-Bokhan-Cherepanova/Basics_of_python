def summary():
    try:
        with open('test_5.txt', 'w+') as file_obj:
            line = input('Enter the numbers with a space \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('File error')
    except ValueError:
        print('Wrong number dialed. I/O error')
summary()