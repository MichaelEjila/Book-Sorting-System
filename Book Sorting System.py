# list to hold all books and books sorted
book_list = []
sorted_book_list = []


# Function to sort newly added book
def add_book():
    book_list.append([book_name, book_author, book_isbn])
    # Moving all book entries into new list sorted
    sorted_book_list = (sorted(book_list))
    print("This list of books in alphabetical order are\n", sorted_book_list)
    return sorted_book_list


# Main to request input of book name, author and ISBN number
a = "a"
# Loop to keep adding books till user is done
while a.upper() == "A":
    book_name = input("Enter book name: ")
    book_author = input("Enter book Author: ")
    book_isbn = int(input("Enter book International Standard Number: "))
    add_book()
    a = input("Enter A to add another book or any other letter to end ")
    # condition to leave loop
    if a.upper() != "A":
        break
