# 1

def calc(a, b, op):
    if op == '+':
        return (a+b)
    elif op == '-':
        return (a-b)
    elif op == '*':
        return (a*b)
    elif op == '/':
        return (a/b)


n = '23 * 10 - 3 + 10 + 10 * 10'
m = n.split()

#a = int(m[0])
#b = int(m[2])
#c = m[1]

#result = calc(a, b, c)
result = int(m[0])
# 2
for i in range(1, len(m)-1, 2):
    result = calc(result, int(m[i+1]), m[i])

print(result)
