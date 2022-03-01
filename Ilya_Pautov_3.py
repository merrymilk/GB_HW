def div(*args):

    try:
        arg1 = int(input("Введите делимое "))
        arg2 = int(input("Введите делитель "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Неправильный делитель! Невозможно делить на ноль"

    return res


    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Wrong number! Devider can't be null")



print(f'result  {div()}')


def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Pautov', name = 'Ilya', year = '1996', city = 'Kandalaksha', email = 'abcd31005@gmail.ru', telephone = '+79113310486'))


def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("Первый агрумент ")), int(input("Второй аргумент ")), int(input("Третий аргумент ")))}')



def int_func (*args):
    word = input("Введите слова ")
    print(word.title())
    return
int_func()

Lesson 3