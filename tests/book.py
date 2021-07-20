class Book:
    def __init__(self, book_type, title, date):
        self.title = title
        self.type = book_type
        self.date = date

    def title(self):
        return self.title

    def type(self):
        return self.type

    def date(self):
        return self.date


# b = Book('Sc', 'tt', 'date')
# print(b.type)
