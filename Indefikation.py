import math
class Figure:
    sides_count = 0
    def __init__(self, color, sides, filled=True):
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        examination = None
        for w in range(0,256):
            if w == r and type(r) == int:
                r = True
            elif w == g and type(g) == int:
                g = True
            elif w == b and type(b) == int:
                b = True
            else:
                examination = False
        if r == g == b == True:
            examination = True
        return examination



    def set_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self.__color = [r, g, b]
        else:
            self.__color = list(self.color)
        return self.__color



    def __is_valid_sides(self):
        pass

    def get_sides(self):
        return self.sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.sides = list(new_sides)
        else:
            self.sides = self.sides
        return self.sides

    def __len__(self):
        return self.sides[0]


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides):
        self.color = color
        self.sides = sides
        self.__radius = self.sides / 3.14 * 2

    def get_square(self):
        S = self.__radius * 3.14 * 2
        return S



class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        self.sides = sides
        self.color = color

    def get_square(self):
        p = sum(self.sides)/2
        S = math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))
        return S



class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        self.color = color
        self.sides = sides

    def get_sides(self):
        si1 = []
        for i in range(self.sides_count):
            si1.append(self.sides)
        self.sides = si1
        return self.sides

    def get_volume(self):
        V = self.sides[0] ** 3
        return V








circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# # Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


