# 1
# a

# 2
class QuizGift:
    def compute_result(self, capacity, weights, values, n):
        grid = [[0 for x in range(capacity + 1)]
                for x in range(n + 1)]
        for item in range(n + 1):
            for cap in range(capacity + 1):
                if item == 0 or cap == 0:
                    grid[item][cap] = 0
                elif weights[item - 1] <= cap:
                    grid[item][cap] = max(values[item - 1] +
                                          grid[item - 1][cap - weights[item - 1]],
                                          grid[item - 1][cap])
                else:
                    grid[item][cap] = grid[item - 1][cap]
        global k
        k = grid[n][capacity]
        return grid[n][capacity]

    def print_result(self):
        QuizG.compute_result(time_max, time_tasks, points, n_points)
        print('Sara can get a maximum of', k, 'points')
        if k < 250:
            print('Sara will receive a watch')
        if k > 250 and k <= 750:
            print('Sara gets a smartphone')
        if k > 750:
            print('Sara gets a laptop')


points = [120, 200, 150, 350, 100, 90]
time_tasks = [15, 20, 40, 50, 20, 10]
time_max = 100
n_points = len(points)
QuizG = QuizGift()
QuizG.print_result()

# 3
from abc import ABC, abstractclassmethod
import math


class Shape(ABC):
    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def compute_area(self):
        pass


class Square(Shape):
    def __init__(self, parameter):
        self.parameter = parameter

    def compute_area(self):
        area = self.parameter * self.parameter
        print(area)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        area = self.radius * self.radius * 3.14
        print(area)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        # self.s = 0

    def compute_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        print(area)


my_square = Square(2)
my_circle = Circle(2)
my_triangle = Triangle(5, 4, 3)
print('Area of square:', end=' ')
my_square.compute_area()
print('Area of circle:', end=' ')
my_circle.compute_area()
print('Area of triangle:', end=' ')
my_triangle.compute_area()


# 4
class House:
    counter = 0

    def __init__(self, owner, condition, price):
        self.owner = owner
        self.condition = condition
        self.price = price
        self.cost = 0
        self.sold = False
        House.counter = House.counter + 1
        self.id = House.counter

    def sell(self, new_owner):
        self.owner = new_owner
        self.sold = True
        profit = self.price - self.cost
        print(profit)

    def change_price(self, new_price):
        if self.sold == True:
            print('House has been sold!')
        else:
            self.price = new_price

    def renovate(self, expense, new_condition):
        self.cost = self.cost + expense
        self.condition = new_condition
        print('House renovated')

    def print_info(self):
        print(self.owner, self.condition, self.price, '$')


house1 = House('Jhon', 'Good', 100000)
house2 = House('Sara', 'Bad', 250000)

house1.print_info()
house2.print_info()
house1.sell('Leo')
house1.change_price(30000)
house2.change_price(20000)
house2.renovate(5000, 'Great')
house1.print_info()
house2.print_info()