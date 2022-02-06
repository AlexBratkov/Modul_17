import random
string = input('Введите произвольную последовательность разных целых чисел через пробел : ')
list_of_strings = string.split()
list_of_numbers = list(set((map(int, list_of_strings))))
nam = int(input('Ведите число в пределах последовательности не равное минимальному и максимальному: '))
while nam <= min(list_of_numbers) or nam >= max(list_of_numbers):
    if nam <= min(list_of_numbers):
        print('Веденное число не соответствует условию ввода данных, оно равно или менее минимального')
        nam = int(input('Ведите другое число в пределах последовательности не равное минимальному и максимальному: '))
    elif nam >= max(list_of_numbers):
        print('Веденное число не соответствует условию ввода данных, оно равно или более максимального')
        nam = int(input('Ведите другое число в пределах последовательности не равное минимальному и максимальному: '))
def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)
qsort_random(list_of_numbers, 0, len(list_of_numbers)-1)
element = nam
array = [i for i in list_of_numbers]
def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] < element <= array[middle + 1]:
        return middle
    elif element <= array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
print(f'Последовательность чисел {list_of_numbers}')
print(f'Позиция элемента, который меньше числа {nam}, а '
      f'следующий за ним больше или равен  числу {nam} - '
      f'{binary_search(array, element+1, 0, len(list_of_numbers))}')
