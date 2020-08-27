def area(x1, y1, x2, y2, x3, y3):
    triangle_area = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2.0
    return triangle_area

def is_inside(x1, y1, x2, y2, x3, y3, x, y):
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x1, y1, x2, y2, x, y)
    A2 = area(x1, y1, x3, y3, x, y)
    A3 = area(x2, y2, x3, y3, x, y)
    if A==(A1+A2+A3):
        print('Point is inside the triangle')
    else:
        print('Point is not inside the triangle')

is_inside(0, 0, 20, 0, 10, 30, 10, 15)