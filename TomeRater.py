class User(object):
    def __init__(self, name, email):
        self.name = name
        self.emai = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address

    def __repr__(self):
        print("User {name}, email: {email}, books read: {number_of_books}".format(name = self.name, email = self.email, number = len(self.books)))

    def __eq__(self, other_user):
        return self.email == other_user

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("{name}'ISBN has been updated".format(name = self.name))

    def add_rating(self, rating):
        if rating in range(5):
            self.ratings.append(rating)
        else:
            print("Invalid rating {rating}".format(ratitng = self.rating))

    def __eq__(self, isbn):
        return self.isbn == isbn

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
        self.level = level.

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        print("{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject))

    