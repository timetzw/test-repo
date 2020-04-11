# -*- coding: utf-8 -*-
def slope(p1, p2):
    return (p1[1] - p2[1]) / (p1[0] - p2[0])


def intercept(p1, p2):
    k = slope(p1, p2)
    b = p1[1] - k * p1[0]
    return b


def p1input():
    p1x = input("Please input the x coordinator of the first point on R^2 flat:")
    p1y = input("Please input the y coordinator of the first point on R^2 flat:")

    p1 = [int(p1x), int(p1y)]

    return p1


def p2input():
    p2x = input("Please input the x coordinator of the second point on R^2 flat:")
    p2y = input("Please input the y coordinator of the second point on R^2 flat:")

    p2 = [int(p2x), int(p2y)]

    return p2


def judge(p1, p2):
    if p1[0] == p2[0]:
        print(
            "This is a straight line parallelling Y-axis. If you want to get a finite slope and intercept, please try other points."
        )
        p1 = p1input()
        p2 = p2input()
        judge(p1, p2)
    return [p1, p2]


def main():
    p1 = p1input()
    p2 = p2input()
    c = judge(p1, p2)
    p1 = (c[0][0], c[0][1])
    p2 = (c[1][0], c[1][1])
    a = slope(p1, p2)
    b = intercept(p1, p2)
    print("The slope of the line crossing these two points is:", a)
    print("The intercept of the line crossing these two points is:", b)


main()
