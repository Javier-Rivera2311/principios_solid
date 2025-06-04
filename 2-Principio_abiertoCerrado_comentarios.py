"""
EJERCICIO:
Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
y crea un ejemplo simple donde se muestre su funcionamiento
de forma correcta e incorrecta.

DIFICULTAD EXTRA (opcional):
Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
Requisitos:
- Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
Instrucciones:
1. Implementa las operaciones de suma, resta, multiplicación y división.
2. Comprueba que el sistema funciona.
3. Agrega una quinta operación para calcular potencias.
4. Comprueba que se cumple el OCP.
"""

from abc import ABC, abstractmethod

# Clase abstracta que define la interfaz para todas las operaciones.
class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

# Implementación concreta para la suma.
class Summation(Operation):
    def execute(self, a, b):
        return a + b

# Implementación concreta para la resta.
class Subtraction(Operation):
    def execute(self, a, b):
        return a - b

# Implementación concreta para la multiplicación.
class Multiplication(Operation):
    def execute(self, a, b):
        return a * b

# Implementación concreta para la división.
class Division(Operation):
    def execute(self, a, b):
        if b != 0:
            return a / b
        return None  # Evita la división por cero.

# Implementación concreta para la potencia.
class Power(Operation):
    def execute(self, a, b):
        return a ** b

# Clase Calculadora que gestiona las operaciones.
class Calculator:
    def __init__(self) -> None:
        self.operations = {}  # Diccionario para almacenar operaciones.

    # Método para agregar una nueva operación a la calculadora.
    def add_operation(self, name, operation):
        self.operations[name] = operation

    # Método para ejecutar una operación por su nombre.
    def calculate(self, name, a, b):
        if name in self.operations:
            return self.operations[name].execute(a, b)
        raise ValueError(f"Operation '{name}' not found.")

# Instancia de la calculadora.
calculator = Calculator()
# Se agregan las operaciones disponibles.
calculator.add_operation("sum", Summation())
calculator.add_operation("subtract", Subtraction())
calculator.add_operation("multiply", Multiplication())
calculator.add_operation("divide", Division())
calculator.add_operation("power", Power())

# Ejemplo de uso de la calculadora con distintas operaciones.
print(calculator.calculate("sum", 5, 3))        # 8
print(calculator.calculate("subtract", 5, 3))   # 2
print(calculator.calculate("multiply", 5, 3))   # 15
print(calculator.calculate("divide", 5, 3))     # 1.6666666666666667
print(calculator.calculate("power", 5, 3))      # 125