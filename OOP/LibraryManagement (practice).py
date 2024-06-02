class LibraryItem:

    def __init__(self):
        self.all_items = {}

    def add_item(self):
        title = input('Enter title\n> ')
        author = input('Enter author\n> ')
        year = input('Enter year\n> ')
        item_id = input('Enter item_id\n> ')

        self.title = title
        self.author = author
        self.year = year
        self.item_id = item_id

        self.all_items.update({self.title:{'Author':self.author,'Year':self.year,'Item ID':self.item_id,'Checkout':False}})

    def display_items(self):
        for key,value in self.all_items.items():
            print(key,value)

    def checkout_item(self):
        title = input('Enter title to checkout\n> ')
        if title in self.all_items:
            self.all_items[title]['Checkout'] = True
        else:
            print('Title does not exist.')

    def return_item(self):
        title = input('Enter title to return\n> ')
        if title in self.all_items:
            self.all_items[title]['Checkout'] = False
        else:
            print('Title does not exist.')

# new_LibraryItem = LibraryItem()
# new_LibraryItem.add_item()
# new_LibraryItem.display_items()
# new_LibraryItem.checkout_item()
# new_LibraryItem.display_items()
# new_LibraryItem.return_item()
# new_LibraryItem.display_items()

class Book(LibraryItem):
    def add_item(self):
        super().add_item()

        genre = input('Enter genre\n> ')
        pages = input('Enter pages\n> ')

        self.all_items[self.title].update({'Genre':genre,'Pages':pages})

new_book = Book()
new_book.add_item()
new_book.display_items()
new_book.checkout_item()
new_book.display_items()
new_book.return_item()
new_book.display_items()

class Magazine(LibraryItem):
    def add_item(self):
        super.add_item()

        issue_number = input('Enter issue_number\n')