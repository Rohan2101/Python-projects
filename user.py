import random


class User:

    def __init__(self, user_name="", user_password="", user_role=""):
        """
        This is the constructor method of User class
        """
        self.user_id = random.randint(1000000000, 9999999999)
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role

    def __str__(self):
        """
        This method returns the string representation of User object in the specified forma
        :return:string
        """
        return f"user_id;{self.user_id};;user_name;{self.user_name}" \
               f";;user_password;{self.user_password};;user_role;{self.user_role}"


