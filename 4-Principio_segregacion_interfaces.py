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

#sin ISP

class WorkerInterface(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Human(WorkerInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")

class Robot(WorkerInterface):
    
    def work(self):
        print("Trabajando")

    def eat(self):
        pass

human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()
robot.eat() # error

#con ISP

class WorkInterface(ABC):

    @abstractmethod
    def work(self):
        pass

class EatInterface(ABC):

    @abstractmethod
    def eat(self):
        pass

class Human(WorkInterface, EatInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")

class Robot(WorkInterface):
    
    def work(self):
        print("Trabajando")


human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()


#resolver ejercicio

class PrinterInterface(ABC):
    
    @abstractmethod
    def print(self, document: str):
        pass

class ColorPrinterInterface(ABC):

    @abstractmethod
    def print_color(self, document: str):
        pass

class ScannerInterface(ABC):

    @abstractmethod
    def scan(self, document: str) -> str:
        pass

class FaxInterface(ABC):

    @abstractmethod
    def send_fax(self, document: str):
        pass

class Printer(PrinterInterface):
    def print(self, document: str):
        print(f"imprimiendo en blanco y negro el documento {document}.")

class ColorPrinter(ColorPrinterInterface):
    def print_color(self, document: str):
        print(f"imprimiendo a color el documento {document}.")


class MultifunctionPrinter(ColorPrinterInterface, PrinterInterface, ScannerInterface,FaxInterface):
    
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

    printer = Printer()
    color_printer = ColorPrinter()
    Multifunction_printer = MultifunctionPrinter()

    printer.print("doc.pdf")
    color_printer.print_color("doc.pdf")
    Multifunction_printer.print("doc.pdf")
    Multifunction_printer.print_color("doc.pdf")
    Multifunction_printer.scan("doc.pdf")
    Multifunction_printer.send_fax("doc.pdf")

test_printers()