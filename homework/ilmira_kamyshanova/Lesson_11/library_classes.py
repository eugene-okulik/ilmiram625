class Book:
    page_material = 'бумага'
    is_have_text = True

    def __init__(self, title, author, number_of_pages, ISBN, is_reserved):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = ISBN
        self.is_reserved = is_reserved

    def print_books_info(self):
        if self.is_reserved:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages}, '
                  f'материал: {self.page_material}, зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages}, '
                  f'материал: {self.page_material}')


class ClassBook(Book):
    def __init__(self, title, author, number_of_pages, ISBN, is_reserved, subject, class_number, is_have_exercise):
        super().__init__(title, author, number_of_pages, ISBN, is_reserved)
        self.subject = subject
        self.class_number = class_number
        self.is_have_exercise = is_have_exercise

    def print_books_info(self):
        if self.is_reserved:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages}, '
                  f'предмет: {self.subject}, класс: {self.class_number}, зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages}, '
                  f'предмет: {self.subject}, класс: {self.class_number}')



idiot_book = Book('Идиот', 'Достоевский', 500, 123455677, True)
dead_souls_book = Book('Мертвые души', 'Достоевский', 600, 123455678, False)
demons_book = Book('Бесы', 'Достоевский', 400, 123455679, False)
player_book = Book('Игрок', 'Достоевский', 700, 123455680, False)
double_book = Book('Двойник', 'Достоевский', 300, 123455681, False)

math_class_book = ClassBook('Алгебра', 'Иванов', 200, 34567778, True,
                            'Математика', 7, True)
geometric_class_book = ClassBook('Геометрия', 'Иванов', 200, 34567779,
                                 False, 'Математика', 7, True)
history_class_book = ClassBook('История России', 'Петров', 150, 34567780,
                               False, 'История', 5, False)
biology_class_book = ClassBook('Анатомия человека', 'Каменский', 210, 34567781,
                               False,'Биология', 9, False)
chemistry_class_book = ClassBook('Органическая химия', 'Цой', 210, 34567782,
                               False,'Химия', 11, True)


print('Книги: ')

idiot_book.print_books_info()
dead_souls_book.print_books_info()
demons_book.print_books_info()
player_book.print_books_info()
double_book.print_books_info()

print('Учебники: ')

math_class_book.print_books_info()
geometric_class_book.print_books_info()
history_class_book.print_books_info()
biology_class_book.print_books_info()
chemistry_class_book.print_books_info()
