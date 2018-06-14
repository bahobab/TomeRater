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
        return("User {name}, email: {email}, books read: {number_of_books}".format(name = self.name, email = self.email, number_of_books = len(self.books)))

    def __eq__(self, other_user):
        return self.email == other_user

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        total_rating = 0
        n = 0
        for value in self.books.values():
            if value != None:
                n += 1
                total_rating += value
        return total_rating / n

# ============= Fiction class =================

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return '{title} - ISBN: {isbn}'.format(title = self.title, isbn = self.isbn)

    def	__hash__(self):
    		return	hash((self.title,	self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("{title}'s ISBN has been updated".format(title = self.title))

    def add_rating(self, rating):
        if rating == None:
            rating = 0
        if rating in range(5):
            self.ratings.append(rating)
        else:
            print("Invalid rating {rating}".format(ratitng = self.ratings))

    def __eq__(self, isbn):
        return self.isbn == isbn

    def get_average_rating(self):
        #print('get average rating called')
        total_rating = 0
        if len(self.ratings) == 0:
            return 0
        for rating in self.ratings:
            total_rating += rating
        return total_rating / len(self.ratings)

# ============= Fiction class =================

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_average_rating(self):
        return super().get_average_rating()

    def get_author(self):
        return self.author

    def __repr__(self):
        return("{title} by {author}.".format(title = self.title, author = self.author))

# ============= No_Fiction class =================

class Non_Fiction(Book):
    def __init__(self, title, isbn, subject, level):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_average_rating(self):
        return super().get_average_rating()

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return("{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject))

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
        if email not in self.users:
            print("No user with email {email}".format(email=email))
            return

        user = self.users[email]    
        user.read_book(book,rating)
        book.add_rating(rating)
        
        if book in self.books:
            self.books[book] += 1
        else:
            self.books[book] = 1
        
    def add_user(self, name, email, books = None):
        new_user = User(name, email)
        self.users[email] = new_user
        if books != None:
            for book in books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        print('Book catalog:')
        for book in self.books:
            print('{book}'.format(book=book))

    def print_users(self):
        print('Users:')
        for user in self.users:
            print('{user}'.format(user = user))

    def most_read_book(self):
        most_read_book = ''
        num_readers = 0
        for (book, readers) in self.books.items():
            if readers > num_readers:
                num_readers = readers
                most_read_book = book
        return 'The most read book is: {book}'.format(book = most_read_book)

    def highest_rated_book(self):
        highest_rating = 0
        highest_rated_book = ''
        for book in self.books.keys():
            #print(type(book))
            # print(book)
            # print(book.ratings)
            if book.get_average_rating() > highest_rating:
                highest_rating = book.get_average_rating()
                highest_rated_book = book.title
        return 'The highiest rated book is: {book}'.format(book = highest_rated_book)

    def most_positive_user(self):
        most_positive_user = ''
        highest_rating = 0
        for user in self.users.values():
            # print(user.name)
            # print(user.get_average_rating())
            if user.get_average_rating() > highest_rating:
                highest_rating = user.get_average_rating()
                most_positive_user = user.name
        return 'The most positive reader is: {reader}'.format(reader = most_positive_user)
