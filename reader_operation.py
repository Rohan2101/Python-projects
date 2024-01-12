class ReaderOperation:

    def add_bookmark(self, book_title, page_no, reader):
        """
        Add specified reader’s bookmarked
        """
        book_mark = (book_title, page_no)
        reader.bookmark_list.append(book_mark)

    def delete_bookmark(self, num, reader):
        """
        Delete the specified reader’s bookmark based on the index from bookmark_list list
        :param num: the mark number

        If num = 0 all marks will be deleted;
        if num < 0 the mark will be sorted from then ends;
        if the num position not exit then do nothing
        """
        if num == 0:
            reader.bookmark_list = []
        if num > 0:
            del reader.bookmark_list[num - 1]
        elif num < 0:
            del reader.bookmark_list[num]

    def show_all_bookmarks(self, reader):
        """Display all the Reader’s bookmarks"""
        if reader.bookmark_list:
            line_no = 1
            for mark in reader.bookmark_list:
                print(f"{line_no} : {mark}")
                line_no += 1
        else:
            print("Sorry, you don't have any bookmark!")
    def save_favorite_book(self, book_title, reader):
        """Add the specified reader’s favourite book (i.e., title) in favourite_book_list list"""
        reader.favourite_book_list.append(book_title)

    def delete_favorite_book(self, identity, reader):
        """
        Remove specified reader’s favourite book from favourite_book_list list
        :param identity: the book identity, accept a book id or a book title
        :param reader: the reader object

        If identity = 0 all marks will be deleted;
        if identity < 0 the mark will be sorted from the ends;
        if the identity position not exit then do nothing
        """
        id_type = type(identity)
        if id_type == int:
            if identity == 0:
                reader.favourite_book_list = []
            elif identity > 0:
                del reader.favourite_book_list[identity - 1]
            else:
                del reader.favourite_book_list[identity]
        elif id_type == str:
            try:
                reader.favourite_book_list.remove(identity)
            except ValueError:
                # ignore the error that book not exit
                pass

    def show_all_favorite_book(self, reader):
        """Display all the Reader’s favourite books"""
        if reader.favourite_book_list:
            line_no = 0
            for book in reader.favourite_book_list:
                print(f"{line_no}: {book}")
                line_no += 1
        else:
            print("Sorry, you don't have any favourite!")
