"""
EJERCICIO:
Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
de forma correcta e incorrecta.

DIFICULTAD EXTRA (opcional):
Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
manejar diferentes aspectos como el registro de libros, la gestión de usuarios
y el procesamiento de préstamos de libros.
Requisitos:
1. Registrar libros: El sistema debe permitir agregar nuevos libros con
información básica como título, autor y número de copias disponibles.
2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
información básica como nombre, número de identificación y correo electrónico.
3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
tomar prestados y devolver libros.
Instrucciones:
1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
los tres aspectos mencionados anteriormente (registro de libros, registro de
usuarios y procesamiento de préstamos).
2. Refactoriza el código: Separa las responsabilidades en diferentes clases
siguiendo el Principio de Responsabilidad Única.
"""

# incorrecto

class Library:  # ❌ Esta clase asume múltiples responsabilidades: gestionar libros, usuarios y préstamos.

    def __init__(self) -> None:
        self.books = []  # ❌ Almacena libros como diccionarios en lugar de objetos, lo que limita la encapsulación.
        self.users = []  # ❌ También almacena usuarios como diccionarios, mezclando responsabilidades.
        self.loans = []  # ❌ Lógica de préstamos incluida en la misma clase Library (violación del SRP).

    def add_book(self, title, author, copies):
        # ❌ Crea y almacena un libro en formato dict, sin usar una clase específica como Book.
        self.books.append({"title": title, "author": author, "copies": copies})

    def add_user(self, name, id, email):
        # ❌ Similar al método anterior, gestiona directamente usuarios como diccionarios.
        self.users.append({"name": name, "id": id, "email": email})

    def loan_book(self, user_id, book_title):
        # ❌ Lógica de negocio del préstamo implementada directamente en Library.
        for book in self.books:
            if book["title"] == book_title and book["copies"] > 0:
                book["copies"] -= 1  # ❌ Modificación directa del stock dentro de la misma clase que lo almacena.
                self.loans.append(
                    {"user_id": user_id, "book_title": book_title})  # ❌ Representación del préstamo como diccionario plano.
                return True
        return False  # ✅ Retorno correcto si no se puede realizar el préstamo.

    def return_book(self, user_id, book_title):
        # ❌ También contiene la lógica de devolución, mezclando funciones de negocio e infraestructura.
        for loan in self.loans:
            if loan["user_id"] == user_id and loan ["book_title"] == book_title:
                self.loans.remove(loan)
                for book in self.books:
                    if book["title"] == book_title:
                        book["copies"] += 1  # ❌ Nuevamente, se modifica el stock directamente.
                    return True  # ⚠️ Este return está mal indentado: solo se ejecutará en la primera coincidencia parcial.
            return False  # ⚠️ Retorno prematuro: puede salir del loop antes de revisar todos los préstamos.

# correcto

class books:  # ✅ Clase con única responsabilidad: representar un libro.
    
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies  # ✅ Encapsula atributos propios del libro, permitiendo escalabilidad futura.

class Users:  # ✅ Clase dedicada a representar un usuario de la biblioteca.

    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email  # ✅ Atributos bien definidos para un modelo de usuario.

class Loan:  # ✅ Clase especializada en la gestión de préstamos.

    def __init__(self):
        self.loans = []  # ✅ Almacena los préstamos de forma interna, separando esta lógica de Library.

    def loan_book(self, user, book):
        if book.copies > 0:
            book.copies -= 1  # ✅ Se reduce la copia directamente en el objeto Book.
            self.loans.append(
                {"user_id": user.id, "book_title": book.title})  # ✅ Registro estructurado del préstamo.
            return True
        return False  # ✅ Bien manejado: préstamo solo se realiza si hay copias disponibles.
    
    def return_book(self, user, book):
        for loan in self.loans:
            if loan["user_id"] == user.id and loan["book_title"] == book.title:
                self.loans.remove(loan)
                book.copies += 1  # ✅ Devuelve la copia al inventario.
                return True
            return False  # ⚠️ Este return debería estar fuera del for para revisar todos los préstamos.

class Library:  # ✅ Clase principal con responsabilidad de coordinación entre objetos.

    def __init__(self) -> None: 
        self.books = []  # ✅ Lista de objetos tipo Book.
        self.users = []  # ✅ Lista de objetos tipo User.
        self.loans_service = Loan()  # ✅ Delegación correcta: no gestiona directamente los préstamos.

    def add_book(self, book): 
        self.books.append(book)  # ✅ Agrega un libro ya instanciado, respetando SRP.

    def add_user(self, user): 
        self.users.append(user)  # ✅ Agrega un usuario ya instanciado, respetando SRP.

    def loan_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)  # ✅ Búsqueda encapsulada y clara.
        book = next((b for b in self.books if b.title == book_title), None)  # ✅ Correcta identificación del libro.
        if user and book: 
            return self.loans_service.loan_book(user, book)  # ✅ Delegación de la operación a Loan.
        return False 

    def return_book(self, user_id, book_title): 
        user = next((u for u in self.users if u.id == user_id), None) 
        book = next((b for b in self.books if b.title == book_title), None)  # ⚠️ Posible error: debería ser `b.title == book_title`.
        if user and book: 
            return self.loans_service.return_book(user, book) 
        return False 
