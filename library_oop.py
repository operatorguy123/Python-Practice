class Book:
    def __init__(self, title: str, author: str, available: bool = True):
        self.title = title
        self.author = author
        self.available = available
        
    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} ({status})"

class Library:
    def __init__(self):
        self.books: list[Book] = [] 

    def add_book(self, title: str, author: str):
        for book in self.books:
            if book.title.lower() == title.lower() and book.author.lower() == author.lower():
                print(f"Error: '{title}' by {author} already exists in the library.")
                return

        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"'{title}' by {author} has been added to the library.")

    def borrow_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"You have successfully borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is currently not available.")
                    return
        print(f"Error: '{title}' not found in the library.")

    def return_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"You have successfully returned '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' was already available in the library.")
                    return
        print(f"Error: '{title}' not found in the library.")

    def display_all_books(self):
        if not self.books:
            print("The library is currently empty.")
            return

        print("\n--- Current Library Collection ---")
        for book in self.books:
            print(book)
        print("----------------------------------\n")

    def menu(self):
        while True:
            try:
                user_input = int(input("""
    Welcome to the Library!
    1. Add a book
    2. Borrow a book
    3. Return a book
    4. Check all titles
    5. Exit
    Please enter your choice: """))

                if user_input == 1:
                    title = input("Enter the title of the book: ")
                    author = input("Enter the author of the book: ")
                    self.add_book(title, author)
                elif user_input == 2:
                    title = input("Enter the title of the book to borrow: ")
                    self.borrow_book(title)
                elif user_input == 3:
                    title = input("Enter the title of the book to return: ")
                    self.return_book(title)
                elif user_input == 4:
                    self.display_all_books()
                elif user_input == 5:
                    print("Thank you for visiting the Library. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

my_library = Library()
my_library.menu()
