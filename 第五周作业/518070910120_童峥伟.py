# -*- coding: utf-8 -*-
def slope(p1, p2):
    return (p1[1]-p2[1])/(p1[0]-p2[0])


def intercept(p1, p2):
    k = slope(p1, p2)
    b = p1[1]-k*p1[0]
    return b


def p1input():
    p1x = input("Please input the x coordinator of the first point on R^2 flat:")
    p1y = input("Please input the y coordinator of the first point on R^2 flat:")

    p1 = (p1x, p1y)

    return p1


def p2input():
    p2x = input(
        "Please input the x coordinator of the second point on R^2 flat:")
    p2y = input(
        "Please input the y coordinator of the second point on R^2 flat:")

    p2 = (p2x, p2y)

    return p2


def main():
    p1 = p1input
    p2 = p2input
    print("The slope of the line crossing these two points is:")
    print("The intercept of the line crossing these two points is:", intercept(p1, p2))


main()
