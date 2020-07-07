""" Stwórz klasę Punkt, która będzie reprezentować punkt w układzie współrzędnych.
 Chcemy móc wyświetlić jego reprezentację na ekranie, przesunąć o dany wektor
 oraz obliczyć odległość od innego punktu. """

from math import sqrt

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def find_me(self):
        return f"Your current coordinates: x = {self.x}   y = {self.y} "

    def move(self, horizontal, vertical):
        self.x += horizontal
        self.y += vertical
        return self.x, self.y

    def distance(self, new):
        distance = sqrt(self.x - new.x)**2 + (self.y - new.y)**2
        return distance

# point = Point(2, 3)
# print(point.find_me())
# print(point.move(3,4))
# print(point.move(-5, -7))
# print(point.find_me())
# point = Point(2, 3)
# point2 = Point(2, 2)
# print(point2.distance(point))