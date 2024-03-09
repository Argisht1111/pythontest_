#Задание 1-2
# class Figure():
#     def podschet(self, a, b, c, d, h):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#         self.h = h
# class Rectangle(Figure):
#     def podschet(self, a, b):
#         super().__init__()
#         print(f'площадь прямоугольника равна {a*b}')
#     def __int__(self, a, b):
#         return f"{a*b}"
#     def __str__(self):
#         return 'Четырёхугольник, у которого все углы прямые равны 90°'
# class Righttriangle(Figure):
#     def podschet(self,a,b):
#         super().__init__()
#         print(f'Площадь прямоугольного треугольника равна {a*b/2}')
#     def __int__(self, a, b):
#         return f"{a*b/2}"
#     def __str__(self):
#         return 'Треугольник, в котором один угол прямой'
# class Trapecia(Figure):
#     def podschet(self,a,b,h):
#         super().__init__()
#         print(f'Площадь трапеции равна {(a+b)*h/2}')
#     def __int__(self, a, b,h):
#         return f"{(a+b)*h/2}"
#     def __str__(self):
#         return 'Выпуклый четырёхугольник, у которого две стороны параллельны, а две другие стороны не параллельны'
#
#
#
#
# c = Rectangle()
# g = Righttriangle()
# k = Trapecia()
# c.podschet(5,3)
# g.podschet(4,7)
# k.podschet(2,3,4)
# print(c.__int__(5,3))
# print(c.__str__())
# print(g.__int__(4,7))
# print(g.__str__())
# print(k.__int__(2,3,4))
# print(k.__str__())
#Задание 3!!!

#with open("file.true1", "r") as file:
file = open("file.txt", "w", encoding="utf-8")

class Shape():
    def show(self,a = '12',b = '435',c = '252'):
        self.a = a
        self.b = b
        self.c = c
        print('Ромбом называется параллелограмм, у которого все стороны равны')
    def save(self):
        file.write('Прямоугольник это - четырёхугольник, у которого противоположные стороны равны и все углы равны 90°\n')
        file.write('Квадратом называется прямоугольник, у которого все стороны равны\n')
        file.write('Окружность — это линия на плоскости, каждая точка которой расположена на одинаковом расстоянии от центра окружности\n')
        file.write('Элипс это множество всех точек плоскости, для которых сумма расстояний от двух данных точек, называемых фокусами, есть величина постоянная, большая расстояния между фокусами')
        file.write(str(a.rectangle()))
    def rectangle(self):
        for i in range(10):
            line = ''
            for j in range(8):
                line += '*'
            print(line)


    # def __getstate__(self) -> dict:
    #     fog = {}
    #     fog["a"] = self.a
    #     fog["b"] = self.b
    #     fog["c"] = self.c
    #     return fog
    # def __setstate__(self, fog: dict):
    #     self.a = fog["a"]
    #     self.b = fog["b"]
    #     self.c = fog["c"]


a = Shape()
a.save()
a.rectangle()
print('gela')



