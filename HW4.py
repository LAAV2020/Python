"""Homework 4 for CSE-41273"""
# Adam Vickter
import datetime
import math


#Part 1
class Person:
    """Person with first and last name."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def full_name(self):
        return (self.first_name) + " " + (self.last_name)
    @property
    def name(self):
        return self.last_name + ", " + self.first_name


# Part 2
class Point:
    """2-D Point objects."""
    def __init__(self, x=0, y=0):
        """Initialize the Point instance"""
        self.x = x
        self.y = y
    @property
    def magnitude(self):
        """Return the magnitude of vector from (0,0) to self."""
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def __repr__(point): 
        return f"Point(x={point.x}, y={point.y})"
    def __str__(point):
        return f"Point at ({point.x}, {point.y})"
    

# Part 3
class Vehicle:
    """A simple class representing a vehicle"""
    def __init__(self, make, model, year, price, color):
        if not isinstance(year, int):
            raise TypeError("Input year must be a number!")
        if not isinstance(price, (int,float)):
            raise TypeError("Input price must be a number!")
        
        self.make = make
        self.model = model
        self.year =  int(year)
        self.price = price 
        self.color = color
        
    @property
    def current_year(self):
        """Return the current year"""
        return datetime.datetime.now().year
    def __repr__(self):
        return f"Vehicle('{self.make}', '{self.model}', '{self.year}', {self.price}, {self.color}')"
    def __str__(car):
        return("This is a "+str(car.year)+" "+car.color+" "+ car.model+" costing "+str(car.price))
    def current_value(self): 
        age = self.current_year - self.year + 1 
        if age > 5: 
            return 0.1 * self.price
        return self.price - 0.15 * age
    










    