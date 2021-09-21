book_title = []
sorted_book_title = []

def isntitle():
    book_status = True
    isn = int(input("What is the books International Standard Number "))
    isn_title = ((isn // 10) % 1000)
    print()
    # Scan isn number with database and bring out corresponding title with variable name "title"
    # if book is found book_Status = True
    if book_status == True:
        title = "A title"
        print(f"Book found! title is {title}")
        book_title.append(title)
        sorted_book_title.extend(sorted(book_title))
        print(f"the list of books are {sorted_book_title}")

    # if book not found, book_status = False
    else:
        print("Book not found. Check ISN number")


access = 1
while(access == 1):
    rideon = input("Click Enter to add a book ")
    isntitle()
    access = int(input("Enter the number 1 to add another book or any other number to cancel: "))
    if access != 1:
        break