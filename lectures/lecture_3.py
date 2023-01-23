# Задача
# В файле хранятся числа, нужно выбрать четные и составить список пар(число; квадрат числа)
# пример:
# 1 3 6 15 4
# [(6,36),(4,16)]

#path = '/x/Geek/Developer/2_block/Python/Python/file.txt'
#f = open(path,'r')
# data = f.read() + ' ' # Добавляем к прочитанному пробел
# f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')  # найти позицию пробела
    # взять всё от первого символа до пробела
    numbers.append(int(data[:space_pos]))
    # обновить выборку, чтобы убрать использованное
    data = data[space_pos + 1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e**2))
print(out)
