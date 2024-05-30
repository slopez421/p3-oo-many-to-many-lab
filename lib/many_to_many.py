import ipdb
class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self): 
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalities):
        new_contract = Contract(self, book, date, royalities)
        Contract.all.append(new_contract)
        return new_contract

    def total_royalties(self):
        royalties = [contract.royalties for contract in Contract.all if contract.author == self]
        return sum(royalties)
        #return a sum of the royalties


class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Author should be an instance of the Author class.")
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise ValueError("Book should be an instance of the Book class.")
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise ValueError("Date should be a string.")
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise ValueError("Royalties should be an integer.")

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]