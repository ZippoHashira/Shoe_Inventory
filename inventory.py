# =======Imports==========
# Import tabulate module.
from tabulate import tabulate


# ========The beginning of the class==========
class Shoe:
    """ Create class 'Shoe'."""

    def __init__(self, country, code, product, cost, quantity):
        """Constructor method with instance variables country, code, product, cost and quantity."""
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """This method returns the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """This method returns the quantity of the shoes."""
        return self.quantity

    def __str__(self):
        """This method returns a string representation of the Shoe class."""
        return [self.country, self.code, self.product, self.cost,
                self.quantity]


# =============Shoe list===========
# Defining empty list "shoe_list" to store a list of objects of shoes.
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    """
    This function will open the file inventory.txt and read data from this file,
    then create a shoes object with this data.
    One line in this file represents data to create one object of shoes.
    """
    try:
        # Open 'inventory.txt' for reading and read file using .readlines()
        with open("inventory.txt", "r") as file:
            shoes_contents = file.readlines()

            # If the length of 'shoes_contents' is more than 0, meaning the file is not empty,
            # create a shoe object with this data and append this object to shoe_list.
            if len(shoes_contents) > 0:
                for line in shoes_contents:
                    if shoes_contents.index(line) > 0:
                        country, code, product, cost, quantity = line.strip(). \
                            split(",")
                        line = Shoe(country, code, product, cost, quantity)
                        shoe_list.append(line)

            # Else, if the file is empty, display an error message.
            else:
                print("ERROR! Your file is empty!")
                exit()

    # Print an error message if the file is not found.
    except FileNotFoundError:
        print("ERROR! File not found!")
        exit()


def capture_shoes():
    """
    This function will allow a user to capture data about a shoe and use this data to create shoe object.
    It will request input from user for country, code and product.
    """
    input_country = input("\nPlease enter the country: ")
    input_code = input("Please enter the code: ")
    input_product = input("Please enter the product name: ")

    # Use while loop to verify whether the user entered a valid input for cost and quantity.
    # If the value entered is not an integer and less than or equal to 0, display an error message.
    # The loop will continue until a valid input is received.
    while True:
        try:
            input_cost = int(input("Please enter the cost: "))
            input_quantity = int(input("Please enter the quantity: "))
            if input_cost <= 0 or input_quantity <= 0:
                print("Please enter values greater than 0!\n")
                continue

            # When all the data is collected correctly, a Shoe object is created and appended to 'shoe_list'.
            captured_shoes = Shoe(input_country, input_code, input_product,
                                  str(input_cost), str(input_quantity))
            shoe_list.append(captured_shoes)

            # Open 'inventory.txt' and use 'a' to append the 'captured_shoes'.
            with open("inventory.txt", "a") as file:
                file.write("\n")
                file.write(",".join(captured_shoes.__str__()))
                print("\nShoes successfully added to the list!")
                break

        except ValueError:
            print("\nPlease ensure you are entering whole numbers.")


def view_all():
    """
    This function will iterate over the shoes list and print the details of the shoes.
    """
    head = ["Country", "Code", "Product", "Cost", "Quantity"]

    # Create an empty list 'view_all_list'.
    view_all_list = []

    # Use for loop to iterate through the shoe list and append list of lists to use tabulate module.
    # Display the information in a table in an easy-to-read manner using the Python tabulate module.
    for shoe in shoe_list:
        view_all_list.append(shoe.__str__())
    print("\n\nYour stock details: ")
    print(tabulate(view_all_list, headers=head, tablefmt="simple_grid"))


def re_stock():
    """
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked.
    It will request user to enter the quantity that they want to add to the stock and then update it.
    """
    stock_list = []  # Create an empty list to store the quantity of each shoe.

    # Use for loop to iterate through the list of shoes and use .get_quantity and append to list.
    # Use min() function to determine the lowest quantity.
    for shoe in shoe_list:
        quantity = shoe.get_quantity()
        stock_list.append(int(quantity))
    min_quantity = min(stock_list)

    shoes_to_be_restocked = None
    for shoe in shoe_list:
        if shoe.quantity == str(min_quantity):
            shoes_to_be_restocked = shoe.__str__()

    # Print the low stock details in a table format.
    print("\nLow stock details:")
    head = ["Country", "Code", "Product", "Cost", "Quantity"]
    print(tabulate([shoes_to_be_restocked], headers=head, tablefmt="simple_grid"))

    # Use while loop to ensure that the user enters a valid value (a positive integer).
    # Else, display an error message if the user enters an invalid input.
    while True:
        try:
            restock_quantity = int(input("\nPlease enter quantity to restock: "))
            if restock_quantity > 0:
                shoes_to_be_restocked[4] = str(restock_quantity + min_quantity)
                print("\nStock successfully updated!")
                break
            else:
                print("Restock quantity cannot be 0!")

        except ValueError:
            print("ERROR! Please use whole numbers.")

    # Open 'inventory.txt' using 'r+' for reading and writing.
    with open("inventory.txt", "r+") as file:
        contents = file.readlines()

    # Open 'inventory.txt' for writing.
    # Using for loop, the quantity will be added to the current stock and updated in the file.
    with open("inventory.txt", "w") as file:
        for line in contents:
            line_list = line.strip().split(",")
            if line_list[:4] == shoes_to_be_restocked[:4]:
                file.write(",".join(shoes_to_be_restocked))
                file.write("\n")
            else:
                file.write(line)


def search_shoe():
    """
    This function will search for a shoe from the list using the shoe code
    and return this object so that it will be printed.
    """
    while True:
        # While true, request 'search_code' input from the user.
        # While loop is used to ensure that the user enters a valid code.
        # Create an empty list and use for loop to add all the shoe codes to the list.
        search_shoe_list = []
        search_code = input("Please enter the shoe code you would like to search: ")
        for shoe in shoe_list:
            if shoe.code == search_code:
                search_shoe_list.append(shoe.__str__())

        # If length of 'search_code_list' is more than 0, display the information of that shoe in a table format.
        if len(search_shoe_list) > 0:
            print("\nDetails of the shoe you are looking for:")
            head = ["Country", "Code", "Product", "Cost", "Quantity"]
            print(tabulate(search_shoe_list, headers=head, tablefmt="simple_grid"))
            break

        # Else, if the code they search for is not in the list, print an error message.
        else:
            print("Error! This product does not exist! Please try again.")


def value_per_item():
    """
    This function will calculate the total stock value for each item in the stock.
    Using for loop, the value is calculated using the formula: value = cost * quantity.
    The information is then printed in a user-friendly format for all the shoes.
    """
    product_value_list = []
    for shoe in shoe_list:
        value = int(shoe.cost) * int(shoe.quantity)
        product_value_list.append([shoe.product, str(value)])

    print("\nTotal value per item in stock: ")
    print(tabulate(product_value_list, headers=["Product", "Total Value"], tablefmt="simple_grid"))


def highest_qty():
    """
    This function determines the product with the highest quantity.
    """
    quantities_list = []  # Create an empty list to store shoe quantity.

    # Use for loop to iterate through the list of shoes to get the quantity and append list.
    # Determine the highest quantity using the max() function.
    for shoe in shoe_list:
        quantity = shoe.get_quantity()
        quantities_list.append(int(quantity))
    highest_quantity = max(quantities_list)

    shoes_on_sale = None
    for shoe in shoe_list:
        if shoe.quantity == str(highest_quantity):
            shoes_on_sale = shoe.__str__()

    # The shoe with the highest quantity will now be displayed on sale in a table form.
    print("\n\nDetails of shoes on SALE:")
    head = ["Country", "Code", "Product", "Cost", "Quantity"]
    print(tabulate([shoes_on_sale], headers=head, tablefmt="simple_grid"))


# ==========Main Menu=============
# While loop starts, while condition is true.
# Clear the shoe list to ensure that data is correct on each iteration.
# Call on the read_shoes_data() function.
# Present menu to the user and get user to input a choice for an option from the menu.
while True:
    shoe_list.clear()
    read_shoes_data()
    user_menu = input("""
            User Menu
——————————————————————————————————————————————————————————————
Please select one of the following options:
1. View all stock details
2. Search shoe by the product code
3. View total value of each item
4. View items that are low on stock to re-stock 
5. View items that are on sale (highest quantity shoe)
6. Capture shoes and add this to the stock list
0. Exit 
————————————————————————————————————————————————————————————————
Enter a number here: """)

    # If the user enters 1, call view_all() function.
    if user_menu == "1":
        view_all()

    # Else if the user enters 2, call search_shoe() function.
    elif user_menu == "2":
        search_shoe()

    # Else if the user enters 3, call value_per_item() function.
    elif user_menu == "3":
        value_per_item()

    # Else if the user enters 4, call re_stock() function.
    elif user_menu == "4":
        re_stock()

    # Else if the user enters 5, call highest_qty() function.
    elif user_menu == "5":
        highest_qty()

    # Else if the user enters 6, call capture_shoes() function.
    elif user_menu == "6":
        capture_shoes()

    # Else if the user enters 0, print "Goodbye!" and exit the user menu using .exit().
    elif user_menu == "0":
        print("\nGoodbye!")
        exit()

    # Otherwise, if user enters invalid input in the menu, print error message.
    else:
        print("Invalid input! Please try again!")
