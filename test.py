def p1input():
    x = input("请任意输入")
    y = (x, x)
    return y


x = p1input()
print(x)
x = map(int, x)

print(x)
