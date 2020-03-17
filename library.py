class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user}) 
            print("Lender-Book database has been updated. You can take the book! ")
        else:
            print(f"Book is already used by {self.lendDict[book]}")
    
    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been added to the book list ")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == "__main__":
    suman = Library(['python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++'],"The_Malakar_Empire")

    while(True):
        print(f"Welcome to the {suman.name} library. Enter Your choice to continue..")
        print("1.Display Books")
        print("2.Lend a Books")
        print("3.Add a Books")
        print("4.Return a Books")

    
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Enter a vailid option!")
            continue

        else:
            user_choice = int(user_choice)
        if user_choice == 1:
            suman.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:\n")
            user = input("Enter your name\n")
            suman.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:\n")
            suman.addBook(book)
        

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:\n")
            suman.addBook(book) 

        else:
            print("Not a valid option!")

        print("Press q to quit and c to continue\n")

        user_choice2 = ""

        while(user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            
            elif user_choice2 == "c":
                continue
