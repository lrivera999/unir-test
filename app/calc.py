import app
import math
import os
import sys


class InvalidPermissions(Exception):
    pass


class Calculator:
    # Suma
    def check_permissions(self, x, y):
        if not app.util.validate_permissions(f"{x} + {y}", "user1"):
            raise InvalidPermissions('User has no permissions')
    def add(self, x, y):
        self.check_types(x, y)
        return x + y
# Resta
    def check_permissions(self, x, y):
        if not app.util.validate_permissions(f"{x} - {y}", "user1"):
            raise InvalidPermissions('User has no permissions')
    def substract(self, x, y):
        self.check_types(x, y)
        return x - y
# Multiplicacion
    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y
#Division
    def check_permissions(self, x, y):
        if not app.util.validate_permissions(f"{x} / {y}", "user1"):
            raise InvalidPermissions('User has no permissions')
    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y
# Potencia
    def check_permissions(self, x, y):
        if not app.util.validate_permissions(f"{x} ** {y}", "user1"):
            raise InvalidPermissions('User has no permissions')
    def power(self, x, y):
        self.check_types(x, y)
        return x ** y
    

    #Raiz cuadrada
    def check_permissions(self, x):
        if not app.util.validate_permissions(f"sqrt({x})", "user1"):
            raise InvalidPermissions('User has no permissions')
    def sqrt(self, x):
        self.check_types(x)
        if x < 0:
            raise TypeError("Square root of negative number is not possible")

        return x ** 0.5
    

    # Logaritmo base 10 
    def check_permissions(self, x):
        if not app.util.validate_permissions(f"log10({x})", "user1"):
            raise InvalidPermissions('User has no permissions')
    def log10(self, x):
        self.check_types(x)
        if x <= 0:
            raise TypeError("Logarithm of non-positive number is not possible")

        return math.log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
