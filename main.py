from reader import Reader
from user_operation import UserOperation
from reader_operation import ReaderOperation
from book_operation import Book_Operations


reader_dict = {}


def command_validation(command_elements):
    """
    This function validates the commands being entered by the user
    :param command_elements: array of commands
    :return: boolean
    """
    if len(command_elements) > 0:
        if command_elements[0] in ['register', 'login', 'book info', 'book titles', 'book content',
                                   'read', 'search by author', 'show by year', 'bookmark', 'delete bookmark',
                                   'show all bookmarks', 'add to favourites', 'delete from favourites',
                                   'show all favourites', 'logout']:
            if command_elements[0] in ['show by year', 'show all bookmarks', 'show all favourites',
                                       'logout'] and len(command_elements) == 1:
                return True
            elif command_elements[0] in ['book info', 'book titles', 'book content', 'search by author',
                                         'delete bookmark', 'add to favourites', 'delete from favourites'] \
                    and len(command_elements) == 2:
                return True
            elif command_elements[0] in ['login', 'bookmark', 'read'] and len(command_elements) == 3:
                return True
            elif command_elements[0] in ['register'] and len(command_elements) == 4:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def user_commands(user_ops):
    """
    This function executes user related commands mainly register and login
    :param user_ops: UserOperation
    :return: Reader
    """
    print("-----------Login/Register Menu-------------")
    user_input = input("Enter 1 To Register or 2 To Login: ")
    if user_input == "1":
        user_command = input("Enter Your Registration Details: ")
        command_elements = user_command.split("|")
        if command_validation(command_elements):
            register_response = user_ops.user_registration(command_elements[1], command_elements[2],
                                                           command_elements[3])
            if register_response:
                print("User Registered Successfully")
                reader = Reader(command_elements[1], command_elements[2])
                reader_dict[reader.user_name] = reader
                return reader
            else:
                print("User Name In Use Already. Please Register Again")
                return None
    elif user_input == "2":
        user_command = input("Enter Your Login Details: ")
        command_elements = user_command.split("|")
        if command_validation(command_elements):
            login_response = user_ops.user_login(command_elements[1], command_elements[2])
            print(login_response[1])
            if login_response[0]:
                reader = reader_dict.get(command_elements[1], None)
                if reader is None:
                    reader = Reader(command_elements[1], command_elements[2])
                    reader_dict[reader.user_name] = reader
                return reader
            else:
                return None
    else:
        print("Invalid input")
        return None


def book_commands(command_elements, book_ops):
    """
    This function executes all book related commands being entered by the user
    :param command_elements: array of commands
    :param book_ops: Book_Operations
    :return: n/a
    """
    if command_elements[0] == 'book info':
        counts_info = book_ops.get_counts(command_elements[1])
        print(f"No. of Chapters: {counts_info[0]}, No. of Lines: {counts_info[1]}, No. of Words: {counts_info[2]}")
    elif command_elements[0] == 'book titles':
        book_ops.display_title(int(command_elements[1]))
    elif command_elements[0] == 'book content':
        book_ops.show_book_contents(command_elements[1])
    elif command_elements[0] == 'read':
        book_ops.show_book_text(command_elements[1], int(command_elements[2]))
    elif command_elements[0] == 'search by author':
        book_ops.get_book_by_author(command_elements[1])
    elif command_elements[0] == 'show by year':
        book_ops.get_book_by_release_year()


def reader_commands(command_elements, reader, reader_ops):
    """
    This function executes commands related to reader
    :param command_elements: array of commands
    :param reader: Reader
    :param reader_ops: ReaderOperation
    :return: n/a
    """
    if command_elements[0] == 'bookmark':
        reader_ops.add_bookmark(command_elements[1], command_elements[2], reader)
        print("Bookmark added successfully")
    elif command_elements[0] == 'delete bookmark':
        reader_ops.delete_bookmark(int(command_elements[1]), reader)
        print("bookmark deleted successfully")
    elif command_elements[0] == 'show all bookmarks':
        reader_ops.show_all_bookmarks(reader)
    elif command_elements[0] == 'add to favourites':
        reader_ops.save_favorite_book(command_elements[1], reader)
        print("Added to favourites successfully")
    elif command_elements[0] == 'delete from favourites':
        reader_ops.delete_favorite_book(command_elements[1], reader)
        print("Deleted from favourites successfully")
    elif command_elements[0] == 'show all favourites':
        reader_ops.show_all_favorite_book(reader)


def load_reader_info(file_path):
    """load reader info from a regular file"""
    with open(file_path, "a+") as f:
        f.seek(0)
        for l in f:
            reader_info = l.strip().split(";;;;")
            reader = Reader(*reader_info[1:4])
            reader.user_id = reader_info[0]
            reader.favourite_book_list = reader_info[4].split(";;")
            reader.bookmark_list = [tuple(bookmark.split(";")) for bookmark in reader_info[5].split(";;")]
            reader_dict[reader.user_name] = reader

def write_reader_info(file_path):
    """write all reader into a file"""
    print(reader_dict.values())
    with open(file_path, "w") as f:
        for reader in reader_dict.values():
            f.write(f"{reader.user_id};;;;{reader.user_name};;;;{reader.user_password};;;;{reader.user_role};;;;")
            f.write(f"{';;'.join(reader.favourite_book_list)};;;;")
            f.write(";;".join([f"{bookmark[0]};{bookmark[1]}" for bookmark in reader.bookmark_list]))
            f.write("\n")


def main():
    """
    This is the main function that displays the menu and executes the logic in the application
    :return: n/a
    """
    user_op = UserOperation()
    reader_op = ReaderOperation()
    book_op = Book_Operations()
    user_op.load_user_info()
    book_op.extract_book_info()
    book_op.load_book_info()
    load_reader_info('data/result_data/reader.txt')
    findle_reader = None
    print(reader_dict)
    while findle_reader is None:
        findle_reader = user_commands(user_op)
    if findle_reader is not None:
        findle_command = ""
        while findle_command != 'logout':
            findle_command = input("Enter A Valid Command Described In The User Manual: ")
            command_array = findle_command.split("|")
            if command_validation(command_array):
                if command_array[0] in ['bookmark', 'delete bookmark', 'show all bookmarks', 'add to favourites',
                                        'delete from favourites', 'show all favourites']:
                    reader_commands(command_array, findle_reader, reader_op)
                elif command_array[0] in ['book info', 'book titles', 'book content', 'read', 'search by author',
                                          'show by year']:
                    book_commands(command_array, book_op)
            else:
                print("Invalid Command")

    user_op.write_user_info()
    write_reader_info('data/result_data/reader.txt')


if __name__ == '__main__':
    main()
