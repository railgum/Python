import re

expr = '23* 10 * 2+ 10 + 10 * 10 * 2 + 5- 7 * 8 + 10 / 2'


def calc(a, b, op):
    if op == '+':
        return (a+b)
    elif op == '-':
        return (a-b)
    elif op == '*':
        return (a*b)
    elif op == '/':
        return (a/b)


expr_without_spaces = expr.replace(' ', '')
print(expr_without_spaces)
list_digits = re.split('\+|-|\/|\*', expr_without_spaces)
print(list_digits)
list_signs = list(
    filter(lambda x: x != '', re.split('\d+', expr_without_spaces)))
print(list_signs)

expr_list = re.split(
    '((\\d*\\.\\d+)|(\\d+)|([\+\-\\*\/\\(\\)]))', expr_without_spaces)

print(expr_list)

list_sum = []
result = int(list_digits[0])

for digit in range(1, len(list_digits)-1):
    if list_signs[digit-1] == '*' or list_signs[digit-1] == '/':
        result = calc(result, int(list_digits[digit]), list_signs[digit-1])
        # print(result)
        list_sum.append(result)
        if list_signs[digit] == '*' or list_signs[digit] == '/':
            result = calc(result, int(list_digits[digit]), list_signs[digit-1])
            list_sum.append(list_sum.pop(digit-1))
        else:
            list_sum.append(list_digits[digit+1])
    else:
        list_sum.append(list_digits[digit])
# print(list_sum)


def sum(list_result):
    result = int(list_result[0])
    for i in range(1, len(list_result)-1, 2):
        result = calc(result, int(list_result[i+1]), list_result[i])
    return result


#result = int(m[0])

# for i in range(1, len(m) - 1, 2):
#    if m[i] == '*' or m[i] == '/':
#        result = calc(int(m[i - 1]), int(m[i + 1]), m[i])
#        m2.append(result)
#        m.pop(i+1)
#        m.insert(i+1, result)
#    else:
#        m2.append(m[i])
    #m2.append(int(m[i + 1]))


# print(m)
# print(m2)
# print(sum(m2))
