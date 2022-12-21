import random
# Задача №17

# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

#n = int(input('Введите размер списка: '))
#arr = []
# for i in range(n):
#    arr.append(random.randint(0, 10))

#res = set(arr)
# print(arr)
# print(res)
# print(len(res))

# Задача №19

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность(сдвиг - циклический) на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 2
#Output:  [4, 5, 1, 2, 3]

#n = int(input('Введите размер списка: '))
#k = int(input('Введите число сдвига списка: '))

#arr = []
# for i in range(n):
#    arr.append(random.randint(0, 10))
# print(arr)
# for i in range(k):
#    arr.insert(0, arr[-1])   # p = arr.pop[-1]
#    arr.pop(-1)              # arr.insert(0,p)
# print(arr)

# Задача №21

# Напишите программу для печати всех уникальных значений в словаре.

# Input:  {"I": "S001", "II": "S002", "III": "S001", "IV": "S005", "V": "S005", "VI": "S009", "VII": "S007"}
#Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# s = {"I": "S001",
#     "II": "S002",
#     "III": "S001",
#     "IV": "S005",
#     "V": "S005",
#     "VI": "S009",
#     "VII": "S007"}


# def unique(dictInput):
#    outSet = set(dictInput.values())
#    return outSet

# print(unique(s))


# Задача №23

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего(элемента с предыдущим номером)
#Input: [0, -1, 5, 2, 3]
#Output: 2

#exampleList = [0, -1, 5, 2, 3, 4, 8, 2, 7, 15, 7, 1]

#def presentBiggerPrevious(l):
#    count = 0
#    for i in range(len(l)-1):
#        if l[i+1] > l[i]:
#            count += 1
#    return count


#print(presentBiggerPrevious(exampleList))
