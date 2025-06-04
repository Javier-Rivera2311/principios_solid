# Principios SOLID en Python

Este repositorio contiene ejemplos prácticos de los cinco principios SOLID aplicados en Python, con archivos separados para el código y los comentarios explicativos de cada principio.

---

## 📌 ¿Qué son los principios SOLID?

**SOLID** es un conjunto de cinco principios fundamentales del diseño de software orientado a objetos. Aplicarlos mejora la mantenibilidad, legibilidad y escalabilidad del código.

### Los principios son:

- **S** – Single Responsibility Principle (SRP)
- **O** – Open/Closed Principle (OCP)
- **L** – Liskov Substitution Principle (LSP)
- **I** – Interface Segregation Principle (ISP)
- **D** – Dependency Inversion Principle (DIP)

---

## 📂 Estructura del Repositorio

| Archivo | Descripción |
|--------|-------------|
| `1-Responsabilidad_unica.py` | Ejemplo del Principio de Responsabilidad Única (SRP). |
| `1-Responsabilidad_unica_comentarios.py` | Versión comentada del ejemplo SRP. |
| `2-Principio_abiertoCerrado.py` | Ejemplo del Principio Abierto/Cerrado (OCP). |
| `2-Principio_abiertoCerrado_comentarios.py` | Versión comentada del ejemplo OCP. |
| `3-Principio_de_sustitucion_liskov.py` | Ejemplo del Principio de Sustitución de Liskov (LSP). |
| `3-Principio_de_sustitucion_liskovComentado.py` | Versión comentada del ejemplo LSP. |
| `4-Principio_segregacion_interfaces.py` | Ejemplo del Principio de Segregación de Interfaces (ISP). |
| `4-Principio_segregacion_interfacesComentado.py` | Versión comentada del ejemplo ISP. |
| `5-Principio_inversion_dependencias.py` | Ejemplo del Principio de Inversión de Dependencias (DIP). |
| `5-Principio_inversion_dependenciasComentado.py` | Versión comentada del ejemplo DIP. |

---

## 🧩 Descripción de cada principio

### 1. SRP – Principio de Responsabilidad Única

**Definición**: Una clase debe tener una única responsabilidad o motivo para cambiar.  
**En el ejemplo**: Se muestra una clase que mezcla gestión de libros, usuarios y préstamos (incorrecto) y una versión donde cada responsabilidad se separa en distintas clases (correcto).

---

### 2. OCP – Principio Abierto/Cerrado

**Definición**: Las clases deben estar abiertas para extensión, pero cerradas para modificación.  
**En el ejemplo**: Se desarrolla una calculadora extensible a nuevas operaciones sin modificar su lógica interna.

---

### 3. LSP – Principio de Sustitución de Liskov

**Definición**: Las clases derivadas deben poder sustituir a sus clases base sin alterar la funcionalidad del sistema.  
**En el ejemplo**: Se implementa una jerarquía de vehículos con comportamiento coherente para todas las subclases.

---

### 4. ISP – Principio de Segregación de Interfaces

**Definición**: Los clientes no deben depender de interfaces que no usan.  
**En el ejemplo**: Se muestran interfaces separadas para impresoras básicas, a color y multifuncionales, evitando métodos innecesarios en clases que no los requieren.

---

### 5. DIP – Principio de Inversión de Dependencias

**Definición**: Las clases de alto nivel no deben depender de clases de bajo nivel, sino de abstracciones.  
**En el ejemplo**: Se aplica este principio a un sistema de notificaciones (Email, SMS, PUSH) y un interruptor de lámpara desacoplado de su implementación concreta.

---

## 🧪 Cómo probar los archivos

Puedes ejecutar cada archivo individualmente para ver el comportamiento correspondiente:

```bash
python 1-Responsabilidad_unica.py
python 2-Principio_abiertoCerrado.py
python 3-Principio_de_sustitucion_liskov.py
python 4-Principio_segregacion_interfaces.py
python 5-Principio_inversion_dependencias.py


