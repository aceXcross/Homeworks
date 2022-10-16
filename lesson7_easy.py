# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:
    def __init__ (self, a , b , c):
        self.a = a
        self.b = b
        self.c = c
        self.accuracy = 5

    def perimeter(self):
        ab = math.sqrt((self.b[0] - self.a[0])**2 + (self.b[1] - self.a[1])**2)
        ac = math.sqrt((self.c[0] - self.a[0])**2 + (self.c[1] - self.a[1])**2)
        bc = math.sqrt((self.c[0] - self.b[0])**2 + (self.c[1] - self.b[1])**2)
        return round(ab + ac + bc, self.accuracy)

    def square(self):
        # расчет площади по формуле определителя второго порядка
        det = ((self.a[0] - self.c[0]) * (self.b[1] - self.c[1])) - ((self.b[0] - self.c[0]) * (self.a[1]) - self.c[1])
        return round(abs(det)/2, self.accuracy)

    def height(self, point):
        # определение противолежащей стороны
        if point == self.a:
            side = math.sqrt((self.c[0] - self.b[0])**2 + (self.c[1] - self.b[1])**2)
        elif point == self.b:
            side = math.sqrt((self.c[0] - self.a[0])**2 + (self.c[1] - self.a[1])**2)
        elif point == self.c:
            side = math.sqrt((self.b[0] - self.a[0])**2 + (self.b[1] - self.a[1])**2)
        else:
            return f'Точка {point} не является вершиной треугольника'

        s = round(2 * self.square() / side, self.accuracy)
        return f'Высота в треугольнике A{self.a}, B{self.b}, C{self.c} из точки {point} = {s}'


tri1 = Triangle((1, 2), (3, -1), (2, 5))
print(f'Периметр треугольника A{tri1.a}, B{tri1.b}, C{tri1.c} = {tri1.perimeter()}')
print(f'Площадь треугольника A{tri1.a}, B{tri1.b}, C{tri1.c} = {tri1.square()}')
print(tri1.height((2, 5)))
print()


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Figtrapezium:

	def __init__ (self, x1, y1, x2, y2, x3, y3, x4, y4):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.x3 = x3
		self.y3 = y3
		self.x4 = x4
		self.y4 = y4
		a1 = math.sqrt ((x2-x1)**2 + (y2-y1)**2)
		a2 = math.sqrt ((x3-x2)**2 + (y3-y2)**2)
		a3 = math.sqrt ((x4-x3)**2 + (y4-y3)**2)
		a4 = math.sqrt ((x1-x4)**2 + (y1-y4)**2)
		if a1 == a2:
			self.c = a1
			self.a = a3
			self.b = a4
		elif a1 == a3:
			self.c = a1
			self.a = a2
			self.b = a4
		elif a1 == a4:
			self.c = a1
			self.a = a2
			self.b = a3
		elif a2 == a3:			
			self.c = a2
			self.a = a1
			self.b = a4
		elif a2 == a4:
			self.c = a2
			self.a = a1
			self.b = a3
		elif a3 == a4:
			self.c = a3
			self.a = a1
			self.b = a2
		else:
			print ('Не ок')

	def check_tz(self):
		pass

	def len_tz (self):
		return [self.a, self.b, self.c]

	def sq_tz(self):
		S = ((self.a + self.b)/2) * math.sqrt(self.c**2 - ((self.a - self.b)**2)/4)
		return S

	def p_tz(self):
		p = self.a + self.b + 2*self.c
		return p

res_2 = Figtrapezium(0, 0, 2, 2, 4, 2, 4, 0)

print (res_2.len_tz())
print (res_2.sq_tz())
print (res_2.p_tz())