# calculate.py

import app
from app import util

import math

class InvalidPermissions(Exception):
    pass


class Calculator:
    def check_permissions(self, operation):
        if not app.util.validate_permissions(operation, "user1"):
            raise InvalidPermissions('User has no permissions')

    # Suma
    def add(self, x, y):
        self.check_types(x, y)
        self.check_permissions(f"{x} + {y}")
        return x + y

    # Resta
    def substract(self, x, y):
        self.check_types(x, y)
        self.check_permissions(f"{x} - {y}")
        return x - y

    # Multiplicacion
    def multiply(self, x, y):
        self.check_types(x, y)
        self.check_permissions(f"{x} * {y}")
        return x * y

    # Division
    def divide(self, x, y):
        self.check_types(x, y)
        self.check_permissions(f"{x} / {y}")
        if y == 0:
            raise TypeError("Division by zero is not possible")
        return x / y

    # Potencia
    def power(self, x, y):
        self.check_types(x, y)
        self.check_permissions(f"{x} ** {y}")
        return x ** y

    # Raiz cuadrada
    def sqrt(self, x):
        self.check_types(x)
        self.check_permissions(f"sqrt({x})")
        if x < 0:
            raise TypeError("Square root of negative number is not possible")
        return x ** 0.5

    # Logaritmo base 10 
    def log10(self, x):
        self.check_types(x)
        self.check_permissions(f"log10({x})")
        if x <= 0:
            raise TypeError("Logarithm of non-positive number is not possible")
        return math.log10(x)

    def check_types(self, x, y=None):
        if y is None:
            if not isinstance(x, (int, float)):
                raise TypeError("Parameter must be a number")
        else:
            if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
                raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
