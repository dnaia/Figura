from math import sqrt
from operator import itemgetter


class Point():
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Figure(Point):
    some_side = 0

    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1)
        print("Создание фигуры.")

    def show(self):
        print("I am figure!")

    def perimeter(self):
        print("Вычисление периметра.")

    def square(self):
        print("Вычисление площади.")


class Triangle(Figure):

    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__(x1, y1, x2, y2)

        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.p3 = Point(x3, y3)

        self.side_a = (self.p1.dist(self.p2))
        self.side_b = (self.p1.dist(self.p3))
        self.side_c = (self.p2.dist(self.p3))
        super().show()
        super().perimeter()
        super().square()

    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c

    def get_square(self):
        return sqrt((Triangle.get_perimetr(self) / 2) * ((Triangle.get_perimetr(self) / 2) - self.side_a) * (
                (Triangle.get_perimetr(self) / 2) - self.side_b) * ((Triangle.get_perimetr(self) / 2) - self.side_c))


class Circle(Figure):
    pi = 3.14

    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.radius = (self.p1.dist(self.p2))
        super().show()
        super().perimeter()
        super().square()

    def get_perimetr(self):
        return self.radius * 2 * Circle.pi

    def get_square(self):
        return Circle.pi * self.radius ** 2


class Quadrilateral(Figure):  # четырехугольник
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2)
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.p3 = Point(x3, y3)
        self.p4 = Point(x4, y4)
        self.side_a = (self.p1.dist(self.p2))
        self.side_b = (self.p1.dist(self.p4))
        self.side_c = (self.p2.dist(self.p3))
        self.side_d = (self.p3.dist(self.p4))
        super().show()
        super().perimeter()
        super().square()

    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c

    def get_square(self):
        return sqrt(self.side_a * self.side_b * self.side_c * self.side_d)


spisok = []
sqspisok = []
n = 0
numfig = int(input('Сколько фигур вы хотите ввести? Введите число '))
for i in range(numfig):
    n += 1
    spisok.append(n)
    fig = int(
        input('\nКакую фигуру вы хотите рассчитать?\nТреугольник - 1\nКруг - 2\nЧетырехугольник - 3\nВведите цифру!\n'))
    if fig == 1:
        tx_1 = (int(input('Введите x1 = ')))
        ty_1 = (int(input('Введите y1 =  ')))
        tx_2 = (int(input('Введите x2 = ')))
        ty_2 = (int(input('Введите y2 =  ')))
        tx_3 = (int(input('Введите x3 = ')))
        ty_3 = (int(input('Введите y3 =  ')))
        t1 = Triangle(tx_1, ty_1, tx_2, ty_2, tx_3, ty_3)
        print('Периметр треугольника', t1.get_perimetr())
        print('Площадь треугольника', t1.get_square())
        name = 'Треугольник'
        spisok.append(name)
        spisok.append(t1.get_square())
        sqspisok.append(t1.get_square())
    elif fig == 2:
        cx_1 = (int(input('Введите x1 = ')))
        cy_1 = (int(input('Введите y1 =  ')))
        cx_2 = (int(input('Введите x2 = ')))
        cy_2 = (int(input('Введите y2 =  ')))
        c1 = Circle(cx_1, cy_1, cx_2, cy_2)
        print('Периметр круга', c1.get_perimetr())
        print('Площадь круга', c1.get_square())
        name = 'Круг'
        spisok.append(name)
        spisok.append(c1.get_square())
        sqspisok.append(c1.get_square())
    elif fig == 3:
        qx_1 = (int(input('Введите x1 = ')))
        qy_1 = (int(input('Введите y1 =  ')))
        qx_2 = (int(input('Введите x2 = ')))
        qy_2 = (int(input('Введите y2 =  ')))
        qx_3 = (int(input('Введите x3 = ')))
        qy_3 = (int(input('Введите y3 =  ')))
        qx_4 = (int(input('Введите x4 = ')))
        qy_4 = (int(input('Введите y4 =  ')))
        q1 = Quadrilateral(qx_1, qy_1, qx_2, qy_2, qx_3, qy_3, qx_4, qy_4)
        print('Периметр четырехугольника', q1.get_perimetr())
        print('Площадь четырехугольника', q1.get_square())
        name = 'Четырехугольник'
        spisok.append(name)
        spisok.append(q1.get_square())
        sqspisok.append(q1.get_square())
    else:
        print('Вы выбрали неверную фигуру! Попробуйте снова!')

spisokk = []
# spisok.sort(key=lambda x:(x[2]))
# print('qq',spisok.sort())

# spisok.sort(key=lambda i: i[2])
spisokk.append(spisok)
spisokk.sort()
sqspisok.sort()
# print(spisok)
# print(sqspisok)
answer = []
ansswer = []
j = 0
ploshad = []
figgura = []
#print(sqspisok[i])
for i in spisok:
    if j >= len(sqspisok):
        break
    if sqspisok[j] in spisok:
        h = sqspisok[j]
        ind_1 = spisok.index(h)  # Индекс площади
        helpnum = ind_1 - 1
        ind_2 = spisok[helpnum]  # Фигура
        answer.append(ind_2) #Фигура
        answer.append(h) #Площадь
        j += 1
ansswer.append(answer)
for a in ansswer:
    print(a[0],a[::2],sep = "\n")
    for b in ansswer[1:len(ansswer):2]:
        print(b)
columns = 2
#print(answer[0])
#print(*ansswer,sep = "\n")
print(*ansswer,sep="\n")

# print(*spisokk,sep = '\n')
# spisok.sort(key = itemgetter(2))
# print('ЙЙ',spisok)
'''
i = 2
dlina = len(spisok)
for i in range(dlina-1):
    if spisok[i] > spisok[i+3]:
        stock = spisok[i]
        spisok[i] = spisok[i+3]
        spisok[i+3] = stock
    i +=3
print(spisok)


#for (i < dlina) in spisok:


# num = spisok[::2]
# while True:
#    n =
'''
