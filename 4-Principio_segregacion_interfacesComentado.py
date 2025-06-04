"""
EJERCICIO:
Explora el "Principio SOLID de Segregación de Interfaces
(Interface Segregation Principle, ISP)", y crea un ejemplo
simple donde se muestre su funcionamiento de forma correcta e incorrecta.

DIFICULTAD EXTRA (opcional):
Crea un gestor de impresoras.
Requisitos:
1. Algunas impresoras sólo imprimen en blanco y negro.
2. Otras sólo a color.
3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
Instrucciones:
1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
2. Aplica el ISP a la implementación.
3. Desarrolla un código que compruebe que se cumple el principio.
"""

from abc import ABC, abstractmethod

# --- Ejemplo SIN aplicar el Principio de Segregación de Interfaces (ISP) ---

# Interfaz que obliga a implementar tanto trabajar como comer
class WorkerInterface(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

# Humano implementa ambas funciones correctamente
class Human(WorkerInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")

# Robot implementa work, pero eat no tiene sentido para él
class Robot(WorkerInterface):
    
    def work(self):
        print("Trabajando")

    def eat(self):
        pass  # No tiene sentido para un robot, pero está obligado a implementarlo

# Pruebas
human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()
robot.eat() # Esto es un error conceptual, ya que un robot no debería comer

# --- Ejemplo aplicando el ISP correctamente ---

# Interfaz solo para trabajar
class WorkInterface(ABC):

    @abstractmethod
    def work(self):
        pass

# Interfaz solo para comer
class EatInterface(ABC):

    @abstractmethod
    def eat(self):
        pass

# Humano implementa ambas interfaces porque puede trabajar y comer
class Human(WorkInterface, EatInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")

# Robot solo implementa la interfaz de trabajo
class Robot(WorkInterface):
    
    def work(self):
        print("Trabajando")

# Pruebas
human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()

# --- Resolución del ejercicio: gestor de impresoras aplicando ISP ---

# Interfaz para impresoras en blanco y negro
class PrinterInterface(ABC):
    
    @abstractmethod
    def print(self, document: str):
        pass

# Interfaz para impresoras a color
class ColorPrinterInterface(ABC):

    @abstractmethod
    def print_color(self, document: str):
        pass

# Interfaz para escáner
class ScannerInterface(ABC):

    @abstractmethod
    def scan(self, document: str) -> str:
        pass

# Interfaz para fax
class FaxInterface(ABC):

    @abstractmethod
    def send_fax(self, document: str):
        pass

# Impresora solo blanco y negro
class Printer(PrinterInterface):
    def print(self, document: str):
        print(f"imprimiendo en blanco y negro el documento {document}.")

# Impresora solo color
class ColorPrinter(ColorPrinterInterface):
    def print_color(self, document: str):
        print(f"imprimiendo a color el documento {document}.")

# Impresora multifunción: implementa todas las interfaces necesarias
class MultifunctionPrinter(ColorPrinterInterface, PrinterInterface, ScannerInterface, FaxInterface):
    
    def print(self, document: str):
        print(f"imprimiendo en blanco y negro el documento {document}.")
    
    def print_color(self, document: str):
        print(f"imprimiendo a color el documento {document}.")

    def scan(self, document: str) -> str:
        print(f"escaneando el documento el documento {document}.")
        return f"documento {document} escaneado."
    
    def send_fax(self, document: str):
        print(f"escaneando el documento {document}.")

def test_printers():
    # Crea una impresora solo blanco y negro
    printer = Printer()
    # Crea una impresora solo color
    color_printer = ColorPrinter()
    # Crea una impresora multifunción
    Multifunction_printer = MultifunctionPrinter()

    # Prueba impresión en blanco y negro
    printer.print("doc.pdf")
    # Prueba impresión a color
    color_printer.print_color("doc.pdf")
    # Prueba todas las funciones de la impresora multifunción
    Multifunction_printer.print("doc.pdf")
    Multifunction_printer.print_color("doc.pdf")
    Multifunction_printer.scan("doc.pdf")
    Multifunction_printer.send_fax("doc.pdf")

# Llama a la función de prueba para demostrar el cumplimiento del ISP
test_printers()