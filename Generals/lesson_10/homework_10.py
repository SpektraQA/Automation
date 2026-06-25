#Task 1


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language,  team_size):
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size
team_lead = TeamLead(
    "Serhii",
    5000,
    "QA",
    "Python",
    5
)
print(team_lead.name)
print(team_lead.salary)
print(team_lead.department)
print(team_lead.programming_language)
print(team_lead.team_size)

#Task 2

from abc import ABC, abstractmethod

import math

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetr(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimetr(self):
        return 2 * self.__width + 2 * self.__height

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius
    def area(self):
        return math.pi * self.__radius * self.__radius

    def perimetr(self):
        return 2 * math.pi * self.__radius

class Square(Figure):
    def __init__(self, side):
        self.__side = side
    def area(self):
        return self.__side * self.__side

    def perimetr(self):
        return 4 * self.__side

rectangle = Rectangle(5, 10)
circle = Circle(3)
square = Square(4)

figures = [rectangle, circle, square]

for figure in figures:
    print(f"Area: {figure.area()}")
    print(f"Perimeter: {figure.perimetr()}")