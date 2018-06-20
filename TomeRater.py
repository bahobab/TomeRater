class User(object):
    """
    User class
    """
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
        """
        compute and return the average rating of books read by a user
        """
        total_rating = 0
        n = 0
        for value in self.books.values():
            if value != None:
                n += 1
                total_rating += value
        return total_rating / n

    def get_user_worth(self):
        """
        compute and return the total price of books read by a user
        """
        total_worth = 0
        for book in self.books:
            total_worth += book.price
        return round(total_worth, 2)

# ============= Fiction class =================

class Book(object):
    isbn_list = []
    def isbn_exists(isbn):
        """
        class helper method checks if an ISBN is already used by a created book
        input: isbn, string
        """
        if isbn in Book.isbn_list:
            print("A book with ISBN '{isbn}' already exists. No Book created!".format(isbn=isbn))
            return True
        return False
        
    def __init__(self, title, isbn, price = 0):
        self.title = title
        self.isbn = isbn
        self.price = float(price)
        self.ratings = []
        Book.isbn_list.append(self.isbn)

    def __len__(self):
        return len(self.ratings)
        
    def __call__(self):
        print("This book's ratings:")
        for rating in self.ratings:
            print(rating)

    def __repr__(self):
        return '{title} - ISBN: {isbn}'.format(title = self.title, isbn = self.isbn)

    def	__hash__(self):            
        return	hash((self.title,	self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn
    
    def get_price(self):
        return self.price

    def set_isbn(self, isbn):
        """
        update the ISBN value of a book
        input: isbn, string
        """
        if Book.isbn_exists(isbn):
            return
        old_isbn = self.isbn
        for i in range(len(Book.isbn_list)):
            if old_isbn == Book.isbn_list[i]:
                self.isbn = isbn
                Book.isbn_list[i] = isbn
        print("{title}'s ISBN has been updated".format(title = self.title))

    def set_price(self, new_price):
        """
        update the price of a book
        input: new_price, float or int
        """
        if not isinstance(new_price, float) or not isinstance(new_price, int):
            print('Invalid price value type... Should something like 12 or 23.0')
        self.price = float(new_price)
        print("{title}'s price has been updated from ${old} to ${new}".format(title = self.title, old = self.price, new = new_price))

    def add_rating(self, rating):
        """
        add rating to a book's rating list
        input: rating, int
        """
        if not isinstance(rating, int):
            rating = 0
        if rating in range(5):
            self.ratings.append(rating)
        else:
            print("Invalid rating {rating}".format(rating = rating))

    def __eq__(self, other):
        return (self.isbn == other.isbn) and (self.title == other.title)

    def __del__(self):
        try:
            Book.isbn_list.remove(self.isbn)
            print('Book deleted!')
        except:
            raise ValueError('Object not found')

    def get_average_rating(self):
        """
        compute and return a book's average rating
        """
        total_rating = 0
        if len(self.ratings) == 0:
            return 0
        for rating in self.ratings:
            total_rating += rating
        return round(total_rating / len(self.ratings), 2)

# ============= Fiction class =================

class Fiction(Book):
    def __init__(self, title, author, isbn, price):
        super().__init__(title, isbn, price)
        self.author = author

    def get_average_rating(self):
        return super().get_average_rating()

    def get_author(self):
        return self.author

    def __len__(self):
        return super().__len__()
        
    def __call__(self):
        return super().__call__()

    def __del__(self):
        super().__del__()

    def __repr__(self):
        return("{title} by {author}.".format(title = self.title, author = self.author))

    def	__hash__(self):            
        return	hash((self.title, self.isbn))

    def __eq__(self, other):
        return super().__eq__(other)

# ============= Non_Fiction class =================

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def get_average_rating(self):
        return super().get_average_rating()

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __del__(self):
        super().__del__()

    def __repr__(self):
        return("{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject))

    def __hash__(self):
        return hash((self.isbn, self.title))

    def __len__(self):
        return super().__len__()
        
    def __call__(self):
        return super().__call__()
    
    def __eq__(self, other):
        return super().__eq__(other)

    # ============= end Non_Fiction class =================

class TomeRater(object):
    """
    TomeRater class
    """
    def __init__(self):
        self.users = {}
        self.books = {}           

    def sorted_dictionary(self, a_dictionary):
        """
        helper function: sort a dictionary by values, desc
        input: unsorted dictionary
        return: sorted dictionary by values, dec
        """
        working_dict = {}
        sorted_dict = []
        for (key, value) in a_dictionary.items():
            working_dict.update({key: value})
        sorted_dict = sorted(working_dict.items(), key = lambda x: x[1], reverse=True)
        return sorted_dict

    def delete_book(self, book):
        """
        delete the book instance
        """
        if book is None:
            print("Book type is invalid.\nPlease verify this book is created without error!" )
            return
        del book
    
    def create_book(self, title, isbn, price):
        """
        create a Book instance
        input:  title, string
                isbn: string
                price: float/int
        return: Book book instance
        """
        if Book.isbn_exists(isbn):
            return
        new_book = Book(title, isbn, price)
        return new_book

    def create_novel(self, title, author, isbn, price):
        """
        create a Novel book instance
        input:  title, string
                author: string
                isbn: string
                price: float/int
        return: Novel book instance
        """
        if Book.isbn_exists(isbn):
            return
        new_fiction = Fiction(title, author, isbn, price)
        return new_fiction

    def create_non_fiction(self, title, subject, level, isbn, price):
        """
        create a Non-Fiction book instance
        input:  title, string
                subject: string
                level: string
                isbn: string
                price: float/int
        return: Non-Fiction book instance
        """
        if Book.isbn_exists(isbn):
            return
        new_non_fiction = Non_Fiction(title, subject, level, isbn, price)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating = None):
        # type(x) == my.object.kind #3.x
        # if any(isinstance(x, my.object.kind) for x in alist)
        """
        add a book read by user to catalog, add rating to book's rating
        input:
                book: Book object
                email: string
                rating
        return: None
        """
        if book is None:
            print("Book type is invalid. Please make sure this book is created without error!" )
            return
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
        
    def email_is_valid(self, email):
        # quick and easy solution
        """
        helper function: check for email valid
        input:  email, string
        return: boolean
        """
        domains = ['com', 'edu', 'io', 'net', 'tv', 'org']
        domain = email.split('.')[-1]
        if '@' in email and domain in domains:
            return True
        else:
            return False

    def add_user(self, name, email, books = None):
        # extra #1: unique email address
        """
        create a new user, add user to users dictionary,
        add book list to dictionary of books read by user
        input:  name: user name, string
                email: user email, string
                books: books read by user, list
        """
        if email in self.users:
            print('User with email {email} already exists.\nPlease use another email'.format(email = email))
            return
        # extra #2: email validation
        if not self.email_is_valid(email):
            print('Email {email} appears to be invalid.\nPlease use another email'.format(email = email))
            return

        new_user = User(name, email)
        self.users[email] = new_user
        if books != None:
            for book in books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        """
        print all read books
        """
        print('Book catalog:')
        for book in self.books:
            print('{book}'.format(book=book))

    def print_users(self):
        """
        print current users
        """
        print('Users:')
        for user in self.users:
            print('{user}'.format(user = user))

    def get_worth_of_user(self, email):
        # extra #:
        """
        print user with most worth in book value
        """
        user = self.users[email]
        worth = user.get_user_worth()
        print('User {name} is worth ${total} in books read'.format(name = user.name, total = worth))

    def top_n_worth_of_users(self, n = 1):
        # extra #:
        """
        print top n most users worh of total book value
        input: n, integer
        output: string
        """

        if not isinstance(n, int):
            raise ValueError('please use int for n')

        dict_to_sort = {}
        sorted_dict = {}
        for user in self.users.values():
            dict_to_sort.update({user.name: user.get_user_worth()})
        sorted_dict = self.sorted_dictionary(dict_to_sort)
        if n > len(self.books):
            n = len(self.books)
        print('The Top {n} user(s) most worth in books read is/are:'.format(n=n)) 
        print('---------------------------------------------------')    
        for i in range(n):
            print('{name} is worth {worth}'.format(name = sorted_dict[i][0], worth = sorted_dict[i][1]))

    def top_n_read_books(self, n = 1):
        # extra #:
        """
        print top n most read books
        input: n, integer
        output: string
        """

        if not isinstance(n, int):
            raise ValueError('please use int for n')
        
        dict_to_sort = {}
        sorted_dict = {}
        for (book, readers) in self.books.items():
            dict_to_sort.update({book.title: readers})
        sorted_dict = self.sorted_dictionary(dict_to_sort)        
        if n > len(self.books):
            n = len(self.books)
        print('The Top {n} most read books are:'.format(n=n)) 
        print('--------------------------')    
        for i in range(n):
            print('{title}: Readers: {readers}'.format(title = sorted_dict[i][0], readers = sorted_dict[i][1]))
    
    def most_read_book(self):
        # extra #:         
        # sort by values
        """
        print highest read book
        """
        most_read_book = ''
        num_readers = 0
        for (book, readers) in self.books.items():
            if readers > num_readers:
                num_readers = readers
                most_read_book = book
        return 'The most read book is: {book}'.format(book = most_read_book)

    def highest_rated_book(self):
        # extra #:
        """
        print highest rated book
        """     
        highest_rating = 0
        highest_rated_book = ''
        for book in self.books.keys():
            if book.get_average_rating() > highest_rating:
                highest_rating = book.get_average_rating()
                highest_rated_book = book.title
        return 'The highiest rated book is: {book}'.format(book = highest_rated_book)

    def top_n_rated_books(self, n = 1):
        # extra #:
        """
        print n highest rated books
        input: n, integer
        output: string
        """
        
        if not isinstance(n, int):
            raise ValueError('please use int for n')
        
        dict_to_sort = {}
        sorted_dict = {}
        for book in self.books:
            dict_to_sort.update({book.title: book.get_average_rating()})
        sorted_dict = self.sorted_dictionary(dict_to_sort)
        if n >= len(self.books):
            n = len(self.books)
        print('The Top {n} most rated book(s) is/are:'.format(n=n)) 
        print('--------------------------------')
        for i in range(n):
            print('{book}  - Rating: {rating}'.format(book = sorted_dict[i][0], rating = sorted_dict[i][1]))

    def most_positive_user(self):
        # extra #:
        """
        print user with highiest book ratings
        output: string
        """       
        most_positive_user = ''
        highest_rating = 0
        for user in self.users.values():
            if user.get_average_rating() > highest_rating:
                highest_rating = user.get_average_rating()
                most_positive_user = user.name
        return 'The most positive reader is: {reader}'.format(reader = most_positive_user)

    def top_n_positive_readers(self, n = 1):
        # extra #:
        """
        print users with n highiest book ratings
        input: n, integer
        output: string
        """

        if not isinstance(n, int):
            raise ValueError('please use int for n')

        dict_to_sort = {}
        sorted_dict = {}
        for user in self.users.values():
            dict_to_sort.update({user.name: user.get_average_rating()})
        sorted_dict = self.sorted_dictionary(dict_to_sort)
        print('The Top {n} most positive reader(s) is/are:'.format(n=n)) 
        print('-------------------------------------')
        for i in range(n):
            print('{reader}  - Highiest Rating: {rating}'.format(reader = sorted_dict[i][0], rating = sorted_dict[i][1]))