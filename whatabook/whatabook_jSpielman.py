import mysql.connector
from mysql.connector import errorcode

#test ID
user_id = 1

#validate that user input is 1,2, or 3. Loop until a valid ID is selected.
def validate_user():
    valid = False
    
    while(valid == False):
        try:
            user_id = int(input("Please enter your customer ID(Users_ID 1-3 are valid): "))
            if user_id > 3:            
                print("\nIncorrect ID.")
            if user_id <= 0:            
                print("\nIncorrect ID.")
            if user_id <= 3 and user_id >=1:
                valid = True
                return user_id
        except ValueError:
            print("\nInvalid entry.")
#query to fetch all users
def select_all_users(cursor):
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    print("\n User List:")
    for user in users:
        print(" User ID: {}\n First Name: {}\n Last Name: {}\n".format(user[0],user[1],user[2]))

#query to fetch all books
def select_all_books(cursor):
    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()
    print("\n Book List:")
    for book in books:
        print(" Book ID: {}\n Book Name: {}\n Author:{}\n Details: {}\n".format(book[0],book[1],book[2],book[3]))

#query to fetch all stores
def select_all_stores(cursor):
    cursor.execute("SELECT * FROM store")
    stores = cursor.fetchall()
    print("\n Store List:")
    for store in stores:
        print(" Store ID: {}\n Locale: {}\n".format(store[0],store[1]))

#query to select a specific users wishlist and display the books name and author.
def select_user_wishlist(cursor,user_id):
    cursor.execute("SELECT u.user_id,u.first_name,u.last_name, b.book_id, b.book_name,b.author " +
                    "FROM wishlist w " +
                    "JOIN user u ON w.user_id = u.user_id "+
                    "JOIN book b ON w.book_id = b.book_id " +
                    "WHERE u.user_id = {}".format(user_id))
    wishlist = cursor.fetchall()
     
    for book in wishlist:
        print("Book Name: {}    Author: {}\n".format(book[4],book[5]))
#main menu method
def show_menu():
    end = False

    while(end == False):
        try:
            menu_selection = int(input("Enter 1 to view all books, 2 to view all locations,3 to view your account, or 4 to quit: "))
            if menu_selection == 1:
                select_all_books(cursor)
            if menu_selection == 2:
                select_all_stores(cursor)
            if menu_selection == 3:
                show_account_menu()
                #print("Feature unavailable")
            if menu_selection == 4:
                input("Program ended. Press any key to continue....")
                end = True
            if menu_selection > 4 or menu_selection < 1:
                print("Selection out of Range!")
        except ValueError:
            print("\nInvalid Entry.")

#account menu view
def show_account_menu():
    validate_user()
    
    end = False

    while(end == False):
        try:
            account_menu_selection = int(input("\nEnter 1 to view your wishlist, 2 to add a book to your wishlist, or 3 to return to the main menu: "))
            if account_menu_selection == 1:
                select_user_wishlist(cursor,user_id)
            if account_menu_selection == 2:
                print("Add feature unavailable.")
            if account_menu_selection == 3:
                print("\nReturned to Main Menu")
                end = True
            if account_menu_selection > 3 or account_menu_selection < 1:
                print("Selection out of range!")
        except ValueError:
            print("Invalid Entry!")
    

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#start try/catch for database connection
try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) 
    #initialize cursor
    cursor = db.cursor()
    
    # output the connection status 
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    print("\nWelcome to Whatabook.")

   # input("\n\n  Press any key to continue...")

#testing queries and output.
    #select_all_users(cursor)
    #select_all_books(cursor)
    #select_all_stores(cursor)
    #select_user_wishlist(cursor,"2")
    #validate_user()
    #select_user_wishlist(cursor,user_id)
    show_menu()

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()


