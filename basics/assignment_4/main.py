class LibraryItem():
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    def borrow_item(self):
        if self.is_borrowed:
            raise Exception(f"The item '{self.title}' is already borrowed.")
        self.is_borrowed = True
        print(f"{self.title} is now borrowed")

    def return_item(self):
        if not self.is_borrowed:
            raise Exception(f"The item '{self.title}' is not borrowed")
        self.is_borrowed = False
        print(f"{self.title} has been returned")


class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Journal(LibraryItem):
    def __init__(self, title, issue_number):
        super().__init__(title)
        self.issue_number = issue_number


def main():
    # book = Book("Can't hurt me", "David Goggins")
    # book.borrow_item()
    # book.borrow_item()
    book = Journal("Can't hurt me", "David Goggins")
    book.return_item()



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Exception occured: {e}")

