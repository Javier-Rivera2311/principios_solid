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

class vehicle:
    def __init__(self, speed=0) -> None:
        self.speed = speed
        
    def accelerate(self, increment):
        self.speed += increment
        print(f"Velocidad: {self.speed} Km/h")

    def brake(self, decrement):
        self.speed -= decrement
        if self.speed <= 0:
            self.speed = 0
        print(f"Velocidad: {self.speed} Km/h")

class Car(vehicle):
    def accelerate(self, increment):
        print("El auto esta acelerando")
        super().accelerate(increment)

    def brake(self,decrement):
        print("El auto esta frenando")
        super().brake(decrement)

class Bicyvle(vehicle):
    def accelerate(self, increment):
        print("La bicicleta esta acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("La bicicleta esta frenando")
        super().brake(decrement)
    
class Motorcycle(vehicle):
    def accelerate(self, increment):
        print("La motocicleta esta acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("La motocicleta esta frenando")
        super().brake(decrement)

def test_vehicle(vehicle):
    vehicle.accelerate(4)
    vehicle.brake(2)

car = Car()
bicycle = Bicyvle()
motorcycle = Motorcycle()

test_vehicle(car)
test_vehicle(bicycle)
test_vehicle(motorcycle)