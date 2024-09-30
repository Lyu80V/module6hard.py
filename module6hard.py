import math

class Figure:

    sides_count = 0

    def __init__(self, color: tuple[int, int, int], *sides, filled=False):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_sides(self, *sides):
        self.__is_valid_sides = True
        if len(sides) == len(self.__sides):
            for side in sides:
                if not isinstance(side, int) or side <= 0:
                    self.__is_valid_sides = False
                    break
        else:
            self.__is_valid_sides = False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == len(self.__sides):
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], side, filled=False):
        super().__init__(color, side, filled=False)
        self.__radius = side / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2



class Triangle(Figure):

    sides_count = 3

    def get_square(self):
        p = len(self) / 2
        sides = self.get_sides()
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple[int, int, int], side, filled=False):
        cube_sides = [side] * 12
        super().__init__(color, *cube_sides, filled=False)

    def get_volume(self):
        sides = self.get_sides()[0]
        return sides ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
