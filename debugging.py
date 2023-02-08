def cylinder():
    r = float(input())
    h = float(input())
    side = 2 * 3.14 * r * h
    circle = 3.14 * r ** 2
    full = side + 2 * circle
    return side, full


sCyl, fCyl = cylinder()
print("Площадь боковой поверхности %.2f" % sCyl)
print("Полная площадь %.2f" % fCyl)