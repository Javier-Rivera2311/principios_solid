"""
EJERCICIO:
Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
y crea un ejemplo simple donde se muestre su funcionamiento
de forma correcta e incorrecta.

DIFICULTAD EXTRA (opcional):
Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
cumplir el LSP.
Instrucciones:
1. Crea la clase Vehículo.
2. Añade tres subclases de Vehículo.
3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
4. Desarrolla un código que compruebe que se cumple el LSP.
"""

# Clase base que representa un vehículo genérico
class vehicle:
    def __init__(self, speed=0) -> None:
        self.speed = speed  # Velocidad inicial del vehículo
        
    # Método para acelerar el vehículo
    def accelerate(self, increment):
        self.speed += increment
        print(f"Velocidad: {self.speed} Km/h")

    # Método para frenar el vehículo
    def brake(self, decrement):
        self.speed -= decrement
        if self.speed <= 0:
            self.speed = 0
        print(f"Velocidad: {self.speed} Km/h")

# Subclase que representa un auto
class Car(vehicle):
    def accelerate(self, increment):
        print("El auto esta acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("El auto esta frenando")
        super().brake(decrement)

# Subclase que representa una bicicleta
class Bicyvle(vehicle):
    def accelerate(self, increment):
        print("La bicicleta esta acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("La bicicleta esta frenando")
        super().brake(decrement)
    
# Subclase que representa una motocicleta
class Motorcycle(vehicle):
    def accelerate(self, increment):
        print("La motocicleta esta acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("La motocicleta esta frenando")
        super().brake(decrement)

# Función que prueba el comportamiento de cualquier vehículo
def test_vehicle(vehicle):
    vehicle.accelerate(4)  # Acelera el vehículo en 4 Km/h
    vehicle.brake(2)       # Frena el vehículo en 2 Km/h

# Instancias de cada tipo de vehículo
car = Car()
bicycle = Bicyvle()
motorcycle = Motorcycle()

# Se prueba que todas las subclases pueden ser usadas como la clase base (LSP)
test_vehicle(car)
test_vehicle(bicycle)
test_vehicle(motorcycle)