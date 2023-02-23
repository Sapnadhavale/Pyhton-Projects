class library:

    def __init__(self,Booklist):
        self.books=Booklist

    def AvilableBooks(self):
        print("The avilable books are:")
        for book in self.books:
            print(book)

    def BorrowBook(self,bookname):
        if bookname in self.books:
            print(f"The book is avilable.You have been issued for {bookname} book.") 
            self.books.remove(bookname)  
            return True    
        else:
            print("Sorry,Book is not avilable.Please wait until the book is returned.") 
            return False   

    def ReturnBook(self,bookname):
        self.books.append(bookname) 
        print("Thank you for returning this book.")   

class Student:
    
    def request_book(self):
        self.book = input("Enter a book you want to borrow")
        return self.book

    def ReturnBook(self):
        self.book = input("Enter a book you want to return")
        return self.book   

if __name__ == '__main__':
    lib=library(["OOP'S","Flask","Django","DSA"])
    stu=Student()

    while True:
        print('''
        ******Welcome to the Library*******
              Please enter an option
              1. To disply all the avilable books.
              2. Request a book
              3. Return a book
              4. Exit the library
        ''')

        a= int(input("Enter a choise.\n"))

        if a == 1:
            lib.AvilableBooks()

        elif a == 2:
            lib.BorrowBook(stu.request_book())

        elif a == 3:
            lib.ReturnBook(stu.ReturnBook())

        elif a == 4:
            print("Thank you for using the library")
            exit()  
        else:
            print("Enter a valid choise.")     

