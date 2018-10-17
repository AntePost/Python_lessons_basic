# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


# Easy, task 1
class Triangle:
    def __init__(self, ax, ay, bx, by, cx, cy):
        """
        Initial function.
        """
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy

    def calc_length(self):
        """
        Calculates lengths of a triangle.
        """
        length = []
        length.append(math.sqrt((self.ax - self.bx)**2 + (self.ay - self.by)**2))
        length.append(math.sqrt((self.ax - self.cx)**2 + (self.ay - self.cy)**2))
        length.append(math.sqrt((self.bx - self.cx)**2 + (self.by - self.cy)**2))
        return length

    def calc_perimeter(self):
        """
        Calculates perimeter of a triangle.
        """
        p = self.calc_length()[0] + self.calc_length()[1] + self.calc_length()[2]
        return p

    def calc_area(self):
        """
        Calculates area of a triangle.
        """
        half_p = self.calc_perimeter()/2
        area = math.sqrt(half_p * (half_p - self.calc_length()[0]) * (half_p - self.calc_length()[1]) * (half_p - self.calc_length()[2]))
        return area

    def calc_height(self):
        """
        Calculates heights of a triangle.
        """
        height_ab = 2 * (self.calc_area() / self.calc_length()[0])
        height_ac = 2 * (self.calc_area() / self.calc_length()[1])
        height_bc = 2 * (self.calc_area() / self.calc_length()[2])
        return height_ab, height_ac, height_bc


triangle1 = Triangle(1, 14, 34, -23, 23, 0)
print("Lengths of a triangle are:")
print(triangle1.calc_length())
print("Perimeter of a triangle is:")
print(triangle1.calc_perimeter())
print("Area of a triangle is:")
print(triangle1.calc_area())
print("Heights of a triangle are:")
print(triangle1.calc_height())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# Easy, task 2
# Решил с использованием классов, но код получился очень запутанный, поэтому
# видимо решил неправильным способом.
class Isosceles_Trapezoid:
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        """
        Initial function.
        """
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy

    def calc_length(self):
        """
        Calculates lengths of an isosceles trapezoid (including diagonals).
        """
        def length_form(x1, x2, y1, y2):
            """
            Formula for length.
            """
            length_size = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            return length_size

        length = {}
        length['ab'] = length_form(self.ax, self.bx, self.ay, self.by)
        length['ac'] = length_form(self.ax, self.cx, self.ay, self.cy)
        length['ad'] = length_form(self.ax, self.dx, self.ay, self.dy)
        length['bc'] = length_form(self.bx, self.cx, self.by, self.cy)
        length['bd'] = length_form(self.bx, self.dx, self.by, self.dy)
        length['cd'] = length_form(self.cx, self.dx, self.cy, self.dy)
        # length['ab'] = (math.sqrt((self.ax - self.bx)**2 + (self.ay - self.by)**2))
        # length['ac'] = (math.sqrt((self.ax - self.cx)**2 + (self.ay - self.cy)**2))
        # length['ad'] = (math.sqrt((self.ax - self.dx)**2 + (self.ay - self.dy)**2))
        # length['bc'] = (math.sqrt((self.bx - self.cx)**2 + (self.by - self.cy)**2))
        # length['bd'] = (math.sqrt((self.bx - self.dx)**2 + (self.by - self.dy)**2))
        # length['cd'] = (math.sqrt((self.cx - self.dx)**2 + (self.cy - self.dy)**2))
        return length

    def whether_parallel(self):
        """
        Decides whether two sides are parallel and which ones.
        """
        def slope_form(x1, x2, y1, y2):
            """
            Formula for slope.
            """
            try:
                slope_size = (y1 - y2) / (x1 - x2)
            except ZeroDivisionError:
                slope_size = math.inf
            return slope_size

        slope = {}
        slope['ab'] = slope_form(self.ax, self.bx, self.ay, self.by)
        slope['ac'] = slope_form(self.ax, self.cx, self.ay, self.cy)
        slope['ad'] = slope_form(self.ax, self.dx, self.ay, self.dy)
        slope['bc'] = slope_form(self.bx, self.cx, self.by, self.cy)
        slope['bd'] = slope_form(self.bx, self.dx, self.by, self.dy)
        slope['cd'] = slope_form(self.cx, self.dx, self.cy, self.dy)

        if slope['ab'] == slope['cd']:
            return 1
        elif slope['ac'] == slope['bd']:
            return 2
        elif slope['ad'] == slope['bc']:
            return 3
        else:
            return 4

    def whether_iso_trap(self):
        """
        Checks whether object is an isosceles trapezoid.
        """
        if self.whether_parallel() == 1:
            if (self.calc_length()['ab'] != self.calc_length()['cd']) and \
            (self.calc_length()['ac'] == self.calc_length()['bd']):
                return "This is an isosceles trapezoid."
            else:
                return "This is not an isosceles trapezoid."
        elif self.whether_parallel() == 2:
            if (self.calc_length()['ac'] != self.calc_length()['bd']) and \
            (self.calc_length()['ad'] == self.calc_length()['bc']):
                return "This is an isosceles trapezoid."
            else:
                return "This is not an isosceles trapezoid."
        elif self.whether_parallel() == 3:
            if (self.calc_length()['ad'] != self.calc_length()['bc']) and \
            (self.calc_length()['ac'] == self.calc_length()['bd']):
                return "This is an isosceles trapezoid."
            else:
                return "This is not an isosceles trapezoid."
        elif self.whether_parallel() == 4:
            return "This is not an isosceles trapezoid."

    # Проверка на пересечения. Решено только для частного случая.
    # Ссылки, объясняющие код:
    # https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
    # https://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
    # https://www.geeksforgeeks.org/orientation-3-ordered-points/
    def whether_intersect(self):
        """
        Checks whether two lines intersect
        """
        def ccw(x1, x2, x3, y1, y2, y3):
            return (y3 - y1)*(x2 - x1) > (y2 - y1)*(x3 - x1)

        # AB and CD intersect
        if ccw(self.ax, self.cx, self.dx, self.ay, self.cy, self.dy) != \
        ccw(self.bx, self.cx, self.dx, self.by, self.cy, self.dy) and \
        ccw(self.ax, self.bx, self.cx, self.ay, self.by, self.cy) != \
        ccw(self.ax, self.bx, self.dx, self.ay, self.by, self.dy):
            return 1
        # AC and BD intersect
        elif False: # Аналогичная проверка
            return 2
        # AD and BC intersect
        elif False: # Аналогичная проверка
            return 3

    def calc_perimeter(self):
        """
        Calculates perimeter
        """
        if self.whether_intersect() == 1:
            p = self.calc_length()['ac'] + self.calc_length()['ad'] + \
            self.calc_length()['bc'] + self.calc_length()['bd']
        elif self.whether_intersect() == 2:
            p = self.calc_length()['ab'] + self.calc_length()['ad'] + \
            self.calc_length()['bc'] + self.calc_length()['cd']
        elif self.whether_intersect() == 3:
            p = self.calc_length()['ab'] + self.calc_length()['ac'] + \
            self.calc_length()['bd'] + self.calc_length()['cd']
        return p

    # Решен частный случай, далее должны быть аналогичные 4 проверки других случаев
    def calc_area(self):
        """
        Calculates area
        """
        half_p = self.calc_perimeter() / 2
        if self.whether_intersect() == 1 and self.whether_parallel() == 2:
            area = math.sqrt((half_p - self.calc_length()['ac']) * (half_p - self.calc_length()['bd']) *\
            (half_p - self.calc_length()['ad']) * (half_p - self.calc_length()['bc']))
        elif self.whether_intersect() == 1 and self.whether_parallel() == 3:
            area = math.sqrt((half_p - self.calc_length()['ad']) * (half_p - self.calc_length()['bc']) *\
            (half_p - self.calc_length()['ac']) * (half_p - self.calc_length()['bd']))
        return area

isosceles_trapezoid1 = Isosceles_Trapezoid(-6, 0, 2, 2, 6, 0, -2, 2)
print("Length of sides are:")
if isosceles_trapezoid1.whether_intersect() == 1:
    print(isosceles_trapezoid1.calc_length()['ac'])
    print(isosceles_trapezoid1.calc_length()['ad'])
    print(isosceles_trapezoid1.calc_length()['bc'])
    print(isosceles_trapezoid1.calc_length()['bd'])
elif isosceles_trapezoid1.whether_intersect() == 2:
    print(isosceles_trapezoid1.calc_length()['ab'])
    print(isosceles_trapezoid1.calc_length()['ad'])
    print(isosceles_trapezoid1.calc_length()['bc'])
    print(isosceles_trapezoid1.calc_length()['cd'])
elif isosceles_trapezoid1.whether_intersect() == 3:
    print(isosceles_trapezoid1.calc_length()['ab'])
    print(isosceles_trapezoid1.calc_length()['ac'])
    print(isosceles_trapezoid1.calc_length()['bd'])
    print(isosceles_trapezoid1.calc_length()['cd'])
# print(isosceles_trapezoid1.whether_parallel())
print(isosceles_trapezoid1.whether_iso_trap())
# print(isosceles_trapezoid1.whether_intersect())
print("Perimeter of this object is:")
print(isosceles_trapezoid1.calc_perimeter())
print("Area of this isosceles trapezoid is:")
print(isosceles_trapezoid1.calc_area())
