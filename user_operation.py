from user import User


class UserOperation:
    """
    This class defines all user related operations which will be performed by the user
    and for the user
    """
    user_info_path = "data/result_data/users.txt"
    user_info_list = list()

    def load_user_info(self):
        """
        This method will load all registered user information stored in the users.txt file
        and compiles it in user_info_list which is a list of user objects.
        1.Read file users.txt and loop through each line
        2.Split each attribute using delimiter and append it to the user_info_list
        :return: boolean
        """
        file = None
        try:
            file = open(self.user_info_path, 'r')
            users_info = file.readlines()
            for user in users_info:
                if len(user) > 0 and user != "" and user != "\n":
                    lines = user.split(";;")
                    user = User(lines[1].split(";")[1], lines[2].split(";")[1], lines[3].split(";")[1])
                    user.user_id = lines[0].split(";")[1]
                    self.user_info_list.append(user)
            return True
        except FileNotFoundError:
            return False
        finally:
            if file is not None:
                file.close()

    def user_registration(self, user_name, user_password, user_role):
        """
        This method registers a user, creates a user object and saves it in user_info_list
        if the user_name already exists it returns False
        :param user_name: string
        :param user_password: string
        :param user_role: string
        :return: boolean
        """
        duplicate_username = [user_info for user_info in self.user_info_list if (user_info.user_name == user_name)]
        if not duplicate_username:
            user = User(user_name, user_password, user_role)
            duplicate_id = [user_info for user_info in self.user_info_list if (user_info.user_id == user.user_id)]
            if bool(duplicate_id):
                return False
            else:
                self.user_info_list.append(user)
                return True
        else:
            return False

    def user_login(self, user_name, user_password):
        """
        This method verifies the login credentials of the user i.e. user_name and user_password
        If any of the two are incorrect it will return False
        :param user_name: string
        :param user_password: string
        :return: boolean
        """
        user = None
        for user_info in self.user_info_list:
            if user_info.user_name == user_name:
                user = user_info
        if user is None or user.user_password != user_password:
            return False, "Incorrect username/password"
        else:
            return True, "Login Successfully"

    def write_user_info(self):
        """
        This method writes the user information from the user_info_list into the users.txt file
        It uses the predefined string method from User class
        :return: boolean
        """
        file = None
        try:
            file = open(self.user_info_path, 'w')
            for user in self.user_info_list:
                file.write(f"{user.__str__()}\n")
            return True, "Successfully Written"
        except FileNotFoundError:
            return False, "An error has occurred"
        finally:
            if file is not None:
                file.close()
