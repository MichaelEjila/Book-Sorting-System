# list to hold all books and books sorted
book_list = [["Pride and Prejudice", "Jane austen", "0061964360"],
             ["The Instrumentality of Mankind", "Cordwainer Smith", "0345277163"],
             ["Children of the Lens", "E.E Doc Smith", "9780586038475"]]
sorted_book_list = []


# Function to sort newly added book
def add_book():
    # Moving all book entries into new list sorted
    sorted_book_list = (sorted(book_list))
    print("This list of books in alphabetical order are:", sorted_book_list, sep='\n')
    return sorted_book_list


# Main to request input of book name, author and ISBN number
print("The original list of books are: ", *book_list, sep='\n')
a = input("Press enter to sort alphabetically by title ")
add_book()
