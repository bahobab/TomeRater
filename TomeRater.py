class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address

    def __repr__(self):
        print("User {name}, email: {email}, books read: {number_of_books}".format(name = self.name, email = self.email, number = len(self.books)))

    def __eq__(self, other_user):
        return self.email == other_user

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_avarage_rating(self):
        average = 0
        n = 0
        for value in self.books.values():
            if value != None:
                n += 1
                average += value
        return average / n

# ============= Fiction class =================

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def	__hash__(self):
    		return	hash((self.title,	self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("{title}'ISBN has been updated".format(title = self.title))

    def add_rating(self, rating):
        if rating in range(5):
            self.ratings.append(rating)
        else:
            print("Invalid rating {rating}".format(ratitng = self.ratings))

    def __eq__(self, isbn):
        return self.isbn == isbn

    def get_avarage_rating(self):
        average = 0
        for rating in self.ratings:
            average += rating
        return average / len(self.ratings)

# ============= Fiction class =================

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        print("{title} by {author}.".format(title = self.title, author = self.author))

# ============= No_Fiction class =================

class Non_Fiction(Book):
    def __init__(self, title, isbn, subject, level):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        print("{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject))

    # ============= No_Fiction class =================

    class TomeRater(object):
        def __init__(self):
            self.users = {}
            self.books = {}

        def create_book(self, title, isbn):
            new_book = Book(title, isbn)
            return new_book

        def create_novel(self, title, author, isbn):
            new_fiction = Fiction(title, author, isbn)
            return new_fiction

        def create_non_fiction(self, title, subject, level, isbn):
            new_non_fiction = Non_Fiction(title,isbn,subject,level)
            return new_non_fiction

        def add_book_to_user(self, book, email, rating = None):
            try:
                name = self.users[email]
                user = User(name, email)
                user.read_book(book,rating)
            except KeyError:
                print("No user with email {email}".format(email=email))
                return

            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
            
        def add_user(self, name, email, books = None):
            self.users[email] = name
            if books != None:
                for book in books:
                    self.add_book_to_user(book, email)