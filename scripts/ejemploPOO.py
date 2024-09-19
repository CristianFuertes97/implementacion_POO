class Book:
    def __init__(self, titulo,autor):
        self.titulo =titulo
        self.autor = autor
        self.disponible = True

    def borrow(self):
        if self.disponible:
            self.disponible = False
            print(f'El libro {self.titulo} ha sido prestado')
        else:
            print(f'El libro {self.titulo} no esta disponile')

    def return_book(self):
        self.disponible = True
        print(f'El libro {self.titulo} ha sido devuelto')

class User:
    def __init__(self, name, user_id):
        self.name = name 
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self,book):
        if book.disponible:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f'El libro {book.titulo} No esta disponible')
    
    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f'El libro {book.titulo} No esta disponible en la lista de prestados')

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def addBooks(self, book):
        self.books.append(book)
        print(f'El libro {book.titulo} has sido agregado ')

    def registerUser(self, user):
        self.users.append(user)
        print(f'El usuario {user.name} ha sido registrado')

    def showAVailableBook(self):
        print('Los libros disponibles: ')
        for book in self.books:
            if book.disponible:
                print(f'{book.titulo} por {book.autor}')

book1 = Book('El principito', 'Antoine de Saint')
book2 = Book('1984', 'George Orwelt')

#Crear usuario
user = User('Cristian', '001')

library1 = Library()
library1.addBooks(book1)
library1.addBooks(book2)
library1.registerUser(user)
library1.showAVailableBook()

user.borrow_book(book1)

library1.showAVailableBook()

user.return_book(book1)

library1.showAVailableBook()