numbers_list = input("Введите последовательность целых чисел через пробел: ")
numbers_list_mod = [int(x) for x in numbers_list.split()]

try:
    user = int(input("Введите целое число: "))
    if user % 1 == 0:
        numbers_list_mod.append(user)
        print("Список до сортировки: ", numbers_list)
        numbers_list_mod.sort()
        print("Список после сортировки по возрастанию: ", numbers_list_mod)
    else:
        print("введите корректное число")
except ValueError:
    print("Некорректные данные")
    print("Программа завершена!")

def binary_search(numbers_list_mod, user, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if numbers_list_mod[middle] == user:
            return middle
        elif user < numbers_list_mod[middle]:
            return binary_search(numbers_list_mod, user, left, middle - 1)
        else:
            return binary_search(numbers_list_mod, user, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'


print("Индекс введенного числа в списке: ", binary_search(numbers_list_mod, user, 0, len(numbers_list_mod) - 1))

