
class Library:
    books = ["Sneham Kamam Branth","Alchemist","Wings of fire","Gandhi My Father","Pularvettom"]
    no_of_books = len(books)
    lent = []

    def add_books(self,book):
        self.books.append(book)
        self.no_of_books += 1
        print(f"Thank you for Donating {book} for the library.")

    def get_book(self,book):
        if book in self.books and book not in self.lent:
            self.lent.append(book)
            print(f"Return the book in 14 days")
        else:
            print(f"The book titled {book} is not availale")
    
    def return_book(self,book):
        if book in self.lent:
            print("Thank you for returning the book")
            self.lent.remove(book)
        else:
            print("This book doesn't belong to this library.")

l = Library()
l.add_books("Jose The Dude")
l.get_book("Alchemist")

l.return_book("Alchemist")

    
    
    
