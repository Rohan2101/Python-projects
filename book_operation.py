import re
import os
import random
import math
from book import Book
book_title_list = []


class Book_Operations(Book):
    """
    This class performs all the book operations and provides the following functionality:
    displays the number of Chapters, number of Words and number of Lines, shows the title of all available books,
    shows the contents and chapters of a specified book, reads a specified book on the specified page,
    shows the available books by author and shows the number of books by year.

    """
    global book_folder_path
    global book_info_path
    book_folder_path = r"data/books_data"
    book_info_path = "data/result_data/books.txt"
    global book_title_list
    global book_info_dict
    book_info_dict = {}
    global book_info_list
    global authors_list
    authors_list = []
    book_info_list = []
    global release_date_list
    release_date_list = []

    def __init__(self, title = "Alice in Wonderland", author = "Lewis Carroll", release_date = "January, 1991", last_update_date = "October 12, 2020", language = "English", producer = "Arthur DiBianca and David Widger", book_path= "data/books_data/11-0.txt"):
        super().__init__(title, author, release_date, last_update_date, language, producer, book_path)

    def extract_book_info(self):
        book_folder_path = r"data/books_data"
        """
        This method extracts all book attributes which are title, author, release_date, 
        last_update_date, language, producer and book_path from each book contained within a the
        book_folder_path and writes these as a formatted string.
        :return: A boolean result will be returned to indicate the success of the method, True
        if completed and False if an error has occurred
        
        """
        l = []
        info = []
        for i in range(10, 4800):               #for loop for  generating filenames for the books
            s = str(i) + "-0.txt"               #file name generation
            d = "data/books_data/" + s
            l.append(d)

        for w in range(10, 68000):              #for loop for  generating filenames for the books
            q = "pg" + str(w) + ".txt"          #file name generation
            di = "data/books_data/" + q
            l.append(di)
        for a in l:
            if os.path.isfile(a):
                w = open(a, 'r', encoding="utf8")           #opening file
                book_title1list = w.readlines()

                info1 = []
                for i in book_title1list[0:100]:
                    if "Title" in i:
                        i11 = re.sub("Title: ", "", i)
                        i12 = re.sub("\n", "", i11)
                        i1 = re.sub(",", "", i12)
                        self.title = i1
                        info.append(i1)
                        if i1 not in book_title_list:
                            book_title_list.append(i1)

                        break
                for i in book_title1list:
                    if "Author" in i:
                        i4 = re.sub("Author: ", "", i)
                        i2 = re.sub("\n", "", i4)
                        self.author = i2
                        info.append(i2)
                        authors_list.append(i2)
                        break
                for j in book_title1list:
                    if "Release Date" in j:
                        ja = re.sub(" [^*][Ee]Book #[^*][^*][^*]", "", j)
                        ja3 = re.sub("Release Date: ", "", ja)
                        ja2 = re.sub("\n", "", ja3)
                        self.release_date = ja2
                        info.append(ja2)
                        release_date_list.append(ja2)
                        break
                for i in book_title1list:
                    if "[Most recently updated:" in i:
                        i7 = re.sub("[^*]Most recently updated: ", "", i)
                        i3 = re.sub("\n", "", i7)
                        self.last_update_date = i3
                        info.append(i3)
                        break
                for i in book_title1list:
                    if "Language:" in i:
                        i8 = re.sub("Language: ", "", i)
                        i4 = re.sub("\n", "", i8)
                        self.language = i4
                        info.append(i4)
                        break
                for i in book_title1list:
                    if "Produced by:" in i:
                        i9 = re.sub("Produced by: ", "", i)
                        i5 = re.sub("\n", "", i9)
                        self.producer = i5
                        info.append(i5)


                        break
                self.book_path = a
                """
                Initializing book object
                """
                b = Book(self.title, self.author, self.release_date, self.last_update_date, self.language, self.producer, self.book_path)
                f = open(book_info_path, 'a', encoding="utf8")
                f.write(b.__str__())                    #writing the formatted string object to external book txt file
                f.write(";;;\n")
                f.close()



                w.close()



        if (len(info) > 0):

            return True
        else:

            return False

    def load_book_info(self):
        """
        Loads all the book’s information from the book file in book_info_path
        into the book_info_dict dictionary and the book_title_list list

        :return: A boolean result will be returned to indicate the success of the method, which
         will be True if the method runs successfully, False if an error has occurred.

        """
        load1 = 0
        load1 = open(book_info_path, 'r', encoding="utf8")
        load3 = load1.readlines()
        for i in load3:
            b_title = re.sub(";;;[^*]+", "", i)
            if b_title not in book_title_list:
                book_title_list.append(b_title)


            load4 = re.sub("\n", "", i)
            if b_title not in book_info_dict.keys():
                book_info_dict[b_title] = (load4)
        load1.close()
        if load1 == 0:
            return False
        else :
            return True


        load1.close()

    def get_counts(self, title):
        """
        Returns the number of chapters, words, and lines for the specified
        book_title
        :param title: title of the book for which the number number of chapters, words, and lines
        need to be obtained
        :return: returns a tuple consisting of the number of chapters, words, and lines which are
        all of integer type
        """
        key_list = []
        x5 = 0
        for x in book_info_dict.keys():
            if x.lower() == title.lower():
                key_list.append(x)
        for x1 in key_list:
            m1 = book_info_dict[x1]
            m2 = re.sub(r'[^*]+books_data', "", m1)             #extracting book path
            m = re.sub(";;;", "", m2)                           #cleaning the data
            book_f = book_folder_path + m
            w = open(book_f, 'r', encoding="utf8")
            c1 = w.read()
            c = c1.lower()
            x = 0                                       #if no chapters are shown then recording 0
            no_lines = 0
            r = re.findall("chapter i", c)               #loops to find number of chapters
            if (len(r) > 0):
                x = x + 1
            r = re.findall("chapter ii", c)
            if (len(r) > 0):
                x = x + 1
            r = re.findall("chapter iii", c)
            if (len(r) > 0):
                x = x + 1
            r = re.findall("chapter iv", c)
            if (len(r) > 0):
                x = x + 1
            r = re.findall("chapter v", c)
            if (len(r) > 0):
                x = x + 1
            r = re.findall("chapter vi", c)
            if (len(r) > 0):
                x = x + 1
            r = re.findall("chapter vii", c)
            if (len(r) > 0):
                x = x + 1
            r = re.findall("chapter viii", c)
            if (len(r) > 0):
                x = x + 1
            r = re.findall("chapter ix", c)
            if (len(r) > 0):
                x = x + 1
            r = re.findall("chapter x", c)
            if (len(r) > 0):
                x = x + 1
            r = re.findall("chapter xi", c)
            if (len(r) > 0):
                x = x + 1
            r = re.findall("chapter xii", c)
            if (len(r) > 0):
                x = x + 1
            r = re.findall("chapter xiii", c)
            if (len(r) > 0):
                x = x + 1
            r = re.findall("chapter iv", c)
            if (len(r) > 0):
                x = x + 1

            pattern = r"[^?]+[*][*][*] START+[^*]+[*][*][*]"
            x1 = re.sub(pattern, "", c)                                 #locating start of book content
            pattern2 = r"[*][*][*] END OF THE +[^*]+[*][*][*][^?]+"            #locating end of book content
            x2 = re.sub(pattern2, "", x1)
            x3 = re.sub('[?.,:;:*"!]', "", x2)              #removing all punctuation
            x4 = re.sub('-', " ", x3)                       #converting Hyphenated words into two words
            no_words = len(x4.split())
            if re.search(pattern, c) is None:
                no_lines = c.count("\n")
            else:
                no_lines = x4.count("\n\n")
            get_count_results = (x, no_lines, no_words)
            return get_count_results


    def display_title(self, page_no):
        """
        Displays titles of the books listed in book_titles_list
        :param page_no: The page number of the title page the customer wishes to see,
                        its a positive integer starting from one
        :return: Displays the users choice of page of book titles from the
                book_title_list list, each title starts with
                the number that shows the title number in the list.
        """
        print("-----------List of book titles-------------")
        y = len(book_title_list)
        z = int(math.ceil(y/10))                    #calculating and generating pages
        if page_no == 1:
            for x in book_title_list[0:10]:
                print(f'{book_title_list.index(x)+1}. {x}')
            print("Current Page: 1")
            print(f'Total number of pages: {z}')
        elif page_no == 2:
            for x in book_title_list[10:20]:
                print(f'{book_title_list.index(x)+1}. {x}')
            print("Current Page: 2")
            print(f'Total number of pages: {z}')
        elif page_no == 3:
            for x in book_title_list[20:30]:
                print(f'{book_title_list.index(x)+1}. {x}')
            print("Current Page: 3")
            print(f'Total number of pages: {z}')
        elif page_no == 4:
            for x in book_title_list[30:40]:
                print(f'{book_title_list.index(x)+1}. {x}')
            print("Current Page: 4")
            print(f'Total number of pages: {z}')
        elif page_no == 5:
            for x in book_title_list[40:50]:
                print(f'{book_title_list.index(x)+1}. {x}')
            print("Current Page: 5")
            print(f'Total number of pages: {z}')
        elif page_no == 6:
            for x in book_title_list[50:60]:
                print(f'{book_title_list.index(x)+1}. {x}')
            print("Current Page: 6")
            print(f'Total number of pages: {z}')
        elif page_no == 7:
            for x in book_title_list[60:70]:
                print(f'{book_title_list.index(x)+1}. {x}')
            print("Current Page: 7")
            print(f'Total number of pages: {z}')
        elif page_no == 8:
            for x in book_title_list[70:80]:
                print(f'{book_title_list.index(x)+1}. {x}')
            print("Current Page: 8")
            print(f'Total number of pages: {z}')
        elif page_no == 9:
            for x in book_title_list[80:90]:
                print(f'{book_title_list.index(x)+1}. {x}')
            print("Current Page: 9")
            print(f'Total number of pages: {z}')
        elif page_no == 10:
            for x in book_title_list[90:95]:
                print(f'{book_title_list.index(x)+1}. {x}')
            print("Current Page: 10")
            print(f'Total number of pages: {z}')
            print("----------end--------------")
        else:
            print("Page number does not exist, please enter a valid page number between 1-10")   #invalid page no handling

    def show_book_contents(self, title):
        """
        Displays the contents of the book selected by the user for the specified book title
        :param title: the book title the user wishes to see the information of.
        :return: The book title with the list of contents of the book selected
        """
        key_list = []
        x5 = 0
        x6 = 0

        for x in book_info_dict.keys():
            if x.lower() == title.lower():
                key_list.append(x)
        for x1 in key_list:
            m1 = book_info_dict[x1]
            m2 = re.sub(r'[^*]+books_data', "", m1)
            m = re.sub(";;;", "", m2)
            book_f = book_folder_path + m
            w = open(book_f, 'r', encoding="utf8")
            y = w.readlines()
            print("CONTENTS")
            for x in y[0:300]:
                if (re.search("CHAPTER I[.]", x)) is not None:
                    if (x5 == 0):
                        print(x)
                        x5 = x5 + 1
                        x6 = x6 + 1


                if (re.search("CHAPTER II[.]", x)) is not None:
                    print(x)
                elif "contents" in x.lower():
                    u4 = y.index(x) + 1
                    u5 = u4 + 15
                    for i9 in y[u4:u5]:
                        print(i9)
                        x6 = x6 + 1

                if (re.search("CHAPTER III[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER IV[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER V[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER VI[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER VII[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER VIII[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER XI[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER X[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER XI[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER XII[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER XIII[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER XIV[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER XV[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER XVI[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER XVII[.]", x)) is not None:
                    print(x)
                if (re.search("CHAPTER XVIII[.]", x)) is not None:
                    print(x)
            if x6 == 0:
                print("No contents")                  #printing no contents if no chapters are present
            w.close()

    def show_book_text(self, title, page_no):
        """
        Displays the book text from user input book for the selected page number
        :param title: The title of the book selected
        :param page_no: the page number of the book
        :return: Displays one page of the book text where each page includes the title
         of the book, chapter number, book text and page number
        """
        key_list = []
        x5 = 0
        zzz = 0

        for x in book_info_dict.keys():
            if x.lower() in title.lower():
                key_list.append(x)
        for x1 in key_list:
            m1 = book_info_dict[x1]
            m2 = re.sub(r'[^*]+books_data', "", m1)
            m = re.sub(";;;", "", m2)
            book_f = book_folder_path + m
            z = 15 + (15 * (page_no - 1))
            r6 = 15*400*page_no
            u1 = open(book_f, 'r', encoding="utf8")
            u2 = u1.read(r6)
            u3 = u2.lower()
            u4 = re.findall("chapter i.", u3)
            chap_no = ""
            if len(u4) > 0:
                chap_no = u4[-1]

            u1.close()
            w = open(book_f, 'r', encoding="utf8")
            y = w.readlines()
            x1 = 0 + (15 * (page_no - 1))                       #calculating and generating pages
            print(f"---------------{title} -- {chap_no.upper()} --------------")
            for x6 in y[0:150]:
                if re.search("contents", x6.lower()) is not None:   #defining the start of the book
                    zzz = y.index(x6) + 18
            for x7 in y:

                if re.search("END OF THE PROJECT GUTENBERG EBOOK", x7) is not None:      #defining the end of the book
                    zz = y.index(x7) - 1

            ny = y[zzz:zz]
            for i in ny[x1:z]:
                print(i)
            if zzz == 0:
                for a1 in y:
                    if re.search("START OF THE PROJECT GUTENBERG EBOOK", a1) is not None:       #defining the start of the book
                        zz = y.index(a1) + 1
                    for a2 in y:
                        if re.search("END OF THE PROJECT GUTENBERG EBOOK", a2) is not None:     #defining the end of the book
                            z2 = y.index(a2) - 1
                    ny1 = y[zz:z2]


                    for i1 in ny1[x1:z]:
                        print(i1)
            print(f'-------------------{page_no}--------------')









    def get_book_by_author(self, author):
        """
        Displays all the book titles belonging to a specified author
        :param author: The name of the author as input by the author
        :return: the book title along with the full author name
        """
        author_title_list1 = []
        titles_by_author = []
        for x in book_info_dict.values():
            book_details = x.split(";;;")
            if author.lower() in book_details[1].lower():
                author_title_list1.append(x)

        for y in author_title_list1:
            value = {i for i in book_info_dict if book_info_dict[i] == y}
            book_details = y.split(";;;")
            titles_by_author.append(tuple((value, book_details[1])))

        print(f'-----------------Books by {author}------------------- ')
        for z in titles_by_author:
            print(f'The book title: {z[0]} _ {z[1]}')
        print("-------------------end--------------------")

    def get_book_by_release_year(self):
        """
        Displays the total number of books released before 1990, between 1990 and 2000 and after 2000

        :return: Printing out the total number of books for each of the specified release years.
        """
        n = 0
        g = 0                                       #if no book is within range then printing 0
        s = 0
        year_list = []
        for x in release_date_list:
            x2 = re.sub("[^?]+, ", "", x)
            x3 = re.sub("]", "", x2)                    #Cleaning the data to find the release year
            x1 = re.sub("[^1-3][^0-9]{3} ", "", x3)
            year_list.append(int(x1[0:4]))
        for i in year_list:
            if i < 1990:
                n = n + 1
            elif (i >= 1990) and (i <= 2000):
                g = g + 1
            elif i > 2000:
                s = s + 1

        print(f'Number of books released before 1990: {n}')
        print(f'Number of books released between 1990 and 2000: {g}')           #Showing output in clear format
        print(f'Number of books released after 2000: {s}')


