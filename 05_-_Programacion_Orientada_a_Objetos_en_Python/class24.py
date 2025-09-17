class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro '{self.title}' ha sido prestado.")
        else:
            print(f"El libro '{self.title}' no está disponible.")
            
    def return_book(self):
        self.available = True
        print(f"El libro '{self.title}' ha sido devuelto.")

class User:
    def __init__(self, user_id, name, lastname):
        self.user_id = user_id
        self.name = name
        self.lastname = lastname
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro '{book.title}' no está disponible para ser prestado.")
            
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro '{book.title}' no fue prestado a este usuario.")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        
    def add_book(self, book):
        self.books.append(book)
        print(f"El libro '{book.title}' ha sido añadido a la biblioteca.")
    
    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario '{user.name} {user.lastname}' ha sido dado de alta en la biblioteca.")
        
    def show_available_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"- {book.title} por {book.author} - {book.isbn} - ({book.year})")
                
# Usuarios
user1 = User(1, "Ana", "Gómez")
user2 = User(2, "Luis", "Martínez")

# Objetos libros
book1 = Book("978-3-16-148410-0", "Cien Años de Soledad", "Gabriel García Márquez", 1967)
book2 = Book("978-0-14-118280-3", "1984", "George Orwell", 1949)
book3 = Book("978-0-452-28423-4", "Matar a un Ruiseñor", "Harper Lee", 1960)

# Biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.register_user(user1)
library.register_user(user2)

#Mostrar libros disponibles
library.show_available_books()

# Préstamos de libros
user1.borrow_book(book1)

#Mostrar libros disponibles
library.show_available_books()

user2.borrow_book(book1)  # Intento de préstamo de un libro no disponible
user2.borrow_book(book2)

# Devoluciones de libros
user1.return_book(book1)
user2.return_book(book1)  # Intento de devolución de un libro no prestado
user2.return_book(book2)

#Mostrar libros disponibles
library.show_available_books() 