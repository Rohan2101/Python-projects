from user import User


class Reader(User):

    def __init__(self, user_name, user_password, user_role="reader", favourite_book_list=None, bookmark_list=None):
        """
        This is the constructor method of Reader class
        """
        super(Reader, self).__init__(user_name, user_password, user_role)
        self.favourite_book_list = favourite_book_list or []
        self.bookmark_list = bookmark_list or []

    def __str__(self):
        """
        This method returns the string representation of User object in the specified forma
        :return:string
        """
        return f"{self.user_id};;;;{self.user_name};;;;{self.user_password};;;;" \
               f"{self.user_role};;;;{self.favourite_book_list};;;;{self.bookmark_list}"

