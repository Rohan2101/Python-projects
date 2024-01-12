class Book:
    def __init__(self, title = "Alice in Wonderland", author = "Lewis Carroll", release_date = "January, 1991", last_update_date = "October 12, 2020", language = "English", producer = "Arthur DiBianca and David Widger", book_path= "data/books_data/11-0.txt"):
        """
        This is the constructor method of the book class which constructs a book objects


        :param title: the title of book
        :param author: the author of the book
        :param release_date: the release date of the book
        :param last_update_date: the last update date of the book
        :param language: the language of the book
        :param producer: the producer of the book
        :param book_path: the path of where the book is located
        """
        self.title = title
        self.author = author
        self.release_date = release_date
        self.last_update_date = last_update_date
        self.language = language
        self.producer = producer
        self.book_path = book_path

    def __str__(self):
        """
        This method returns the string representation of book object in the specified format
        :return: (formatted) string
        """
        return f'{self.title};;;{self.author};;;{self.release_date};;;{self.last_update_date};;;{self.language};;;{self.producer};;;{self.book_path}'