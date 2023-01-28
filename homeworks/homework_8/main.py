

def calc(a, b, op):
    if op == '+':
        return (a+b)
    elif op == '-':
        return (a-b)
    elif op == '*':
        return (a*b)
    elif op == '/':
        return (a/b)


n = '23 * 10 + 10 + 10 * 10 + 5 - 7 * 8 + 10 / 2'
m = n.split()
m2 = []
#a = int(m[0])
#b = int(m[2])
#c = m[1]

# 2


def sum(list_result):
    result = int(list_result[0])
    for i in range(1, len(list_result)-1, 2):
        result = calc(result, int(list_result[i+1]), list_result[i])
    return result


result = int(m[0])
#print(m)
for i in range(1, len(m) - 1, 2):
    if m[i] == '*' or m[i] == '/':
        result = calc(int(m[i - 1]), int(m[i + 1]), m[i])
        m2.append(result)
        # Если умножение или деление не подряд
        if i > 1:
            m2.pop(-2)
    else:
        m2.append(m[i])
        m2.append(int(m[i + 1]))


#print(m)
print(m2)
print(sum(m2))
