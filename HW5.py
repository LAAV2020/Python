"""Homework 5 for CSE-41273"""
# Adam Vickter
import math


# Part 1, Circle class.
class Circle:
    """Class to create Circle objects"""

    def __init__(self, radius=1):
        """Circle initializer"""
        self.history = []
        self.radius = radius

    def __str__(self):
        """returns the unofficial string representation of object"""
        return 'Circle with radius of '+str(self.radius)

    def __repr__(self):
        """returns the official string representation of object"""
        return 'Circle(radius='+str(self.radius)+')'

    @property
    def area(self):
        """Calculate and return the area of the Circle"""
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """Calculate and return the diameter of the Circle"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        """Set the diameter"""
        self.radius = diameter / 2

    @property
    def radius(self):
        """Calculate and return the radius of the Circle"""
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Set the radius of circle"""
        # raise an error if radius <0
        if radius < 0:
            raise ValueError('Radius cannot be negative!')
        else:
            self._radius = radius
            self.history.append(self._radius)


# Part 2. BankAccount class.
class BankAccount:
    """ Simple BankAccount class """

    def __init__(self, balance=0):
        """Initialize account with balance"""
        self.balance = balance

    def __str__(self):
        """returns the unofficial string representation of object"""
        return 'Account with balance of $'+str(float(self.balance))

    def __repr__(self):
        """returns the official string representation of object"""
        return 'BankAccount(balance=$'+str(float(self.balance))+')'

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return "True"

    def deposit(self, amount):
        """Deposit amount to this account"""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw amount from this account"""
        self.balance -= amount

    def deposit(self, amount):
        """Deposit amount to this account"""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw amount from this account"""
        self.balance -= amount
