
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        #in this function, initialise the following attributes:
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity         
        
    def get_cost(self):
        # add the code to return the cost of the shoe in this method
        return f"The cost of the {self.product} shoes are {self.cost}"

    def get_quantity(self):
        # add the code to return the quantity of the shoes
        return f"The quantity of the {self.product} shoes are {self.quantity}"

    def __str__(self):
        # add a code to returns a string representation of a class
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

#==========Functions outside the class==============
def read_shoes_data():
    # this function will open the file inventory.txt
    # read the data from this file,
    # create a shoes object with this data
    # extend this object into the shoes list
    # one line in this file represents data to create one object of shoes          
    # create a list of list from each line and delete list[0] since the 1st line are headings
    # use the try-except in this function for error handling
    # except if the file doesnt exist
    # finally close text doc
    inventory_data = None
    try:
        inventory_data = open('inventory.txt', 'r')
        
    except FileNotFoundError:
        print("The text document does not exist.")

    finally:
        inventory_list = [i.strip("\n").split(",") for i in inventory_data]
        del inventory_list[0]
        # need a list external to def to save the list for capture_shoes()
        shoe_obj_data.extend(inventory_list) 
        
        if inventory_data != None:
            inventory_data.close()

def capture_shoes():
    # this function will allow a user to capture data about a shoe
    # index the shoe_obj_data list 
    # use this data to create a shoe object
    # and append this object inside to the shoe list.    
    for entry in shoe_obj_data:
        country = entry[0] 
        code = entry[1] 
        product = entry[2] 
        cost = entry[3] 
        quantity = entry[4]     
        inventory_obj = Shoe(country, code, product, cost, quantity)
        shoe_list.append([inventory_obj.country, inventory_obj.code,
                          inventory_obj.product, inventory_obj.cost,
                          inventory_obj.quantity])        
          
def view_all(shoe_list):
    # this function will iterate over the shoes list and
    # print the details of the shoes returned from the __str__ function. 
    # optional: you can organise your data in a table format. use if-elif-else
    # by using Python’s tabulate module.
    view_table = input("Do you want to view the data in a table? y/n \n:").lower()
    print()
    print("- View all shoe details -")
    print('-' * 50)
    if view_table == 'n':
        for shoe in shoe_list:    
            country = shoe[0] 
            code = shoe[1] 
            product = shoe[2] 
            cost = shoe[3] 
            quantity = shoe[4]     
            inventory_obj = Shoe(country, code, product, cost, quantity)
            print(inventory_obj)        
    
    elif view_table == 'y':
        for shoe in shoe_list:    
            country = shoe[0] 
            code = shoe[1] 
            product = shoe[2] 
            cost = shoe[3] 
            quantity = shoe[4]     
            inventory_obj = Shoe(country, code, product, cost, quantity)
        # do a pip install in Windows comand centre (search cmd)
        # import tabulate
        from tabulate import tabulate
        # place headers in a list and use a table format
        print(tabulate(shoe_list, headers = ['Country', 'Code', 'Product', 'Cost', 'Quantity'], tablefmt = 'fancy_grid'))                    
    
    else:
        print("Invalid input. Please try again.")
        view_all(shoe_list)           
    print()
    
def re_stock():    
    # this function will find the shoe object with the lowest quantity,
    # which are the shoes that need to be re-stocked.
    # create a list to append quantities
    quantity_list = []
    for shoe in shoe_list:
        quantity_list.append(shoe[4])

    # cast list to int to use min()
    quantity_list_int = [int(i) for i in quantity_list]    

    # cast min() to str to use next() & avoid StopIteration
    # use next() to return the next item in an iterator
    lowest_quantity = str(min(quantity_list_int))
    low_quant_idx = (next(shoe for shoe in shoe_list if shoe[4] == lowest_quantity))
    print() 
    print(f"The shoe with the lowest quantity is {low_quant_idx} with {lowest_quantity} shoes.")

    # ask the user if they want to add this quantity of shoes and then update it    
    choose_restock = input("Do you want to restock? y/n \n:").lower()
    if choose_restock == 'y':
        restock_amount = input("How many shoes do you want to add?:\t")
        # assign new value to quantity
        # this quantity should be updated on the file for this shoe
        # create a new object
        # call get_quantity() method after creating new object
        quantity = int(lowest_quantity) +  int(restock_amount)        
        country = low_quant_idx[0]
        code = low_quant_idx[1]
        product = low_quant_idx[2]
        cost = low_quant_idx[3]    
        restock_shoe = Shoe(country, code, product, cost, quantity)
        print(restock_shoe.get_quantity())
        print()
    
        # append new obj to shoes list
        shoe_list.append([restock_shoe.country, restock_shoe.code,
                          restock_shoe.product, restock_shoe.cost,
                          restock_shoe.quantity])

        # did not del() old obj from shoes list to keep original data
        # write new obj to text doc in append mode to keep the original doc unchanged                           
        with open('inventory.txt', 'a') as f:
            f.write(f"{restock_shoe.country}, {restock_shoe.code}, {restock_shoe.product}, {restock_shoe.cost}, {restock_shoe.quantity}\n")
        f.close()

    else:
        print()
        main_menu()
        
def search_shoe():
    # this function will search for a shoe from the list with the shoe code and any()
    # return this object to print
    # use next() to return the next item in an iterator
    print()
    print("The details of the requested shoe will display.")
    enter_code = input("Enter the shoe code:\t").upper()

    # import tabulate to print the shoe details
    # use floatfmt since obj is a single list & each column has various number formatting
    confirm_code = any(enter_code in shoe for shoe in shoe_list)
    if confirm_code == True:
        shoe_locate = (next(shoe for shoe in shoe_list if shoe[1] == enter_code))    
        from tabulate import tabulate        
        print(tabulate([shoe_locate], headers = ['Country', 'Code', 'Product', 'Cost', 'Quantity'], tablefmt = 'fancy_grid', floatfmt = (".1f", ".3f")))

    # print out the an error message if the code is not in the list                
    else:
        print("Invalid code. Please try again.")
        search_shoe()
    print()            

def value_per_item():
    # this function will calculate the total value for each item
    # use the formula: value = cost * quantity.
    # cast str to float and int to multiply numbers
    # round() the value
    for shoe in shoe_list: 
        import math
        value = round(float(shoe[3]) * int(shoe[4]), 2)
        shoe.append(value)        
    
    # print this information on the console for all the shoes
    # import tabulate
    from tabulate import tabulate
    # dont put list name in [] or table prints incorrectly
    print(tabulate(shoe_list, headers = ['Country', 'Code', 'Product', 'Cost', 'Quantity', 'Total value'], tablefmt = 'fancy_grid'))    
    print()
    
def highest_qty():
    # write code to determine the product with the highest quantity 
    # create a list to append quantities
    quantity_list = []
    for shoe in shoe_list:
        quantity_list.append(shoe[4])

    # cast list to int to use max()
    quantity_list_int = [int(i) for i in quantity_list]    

    # cast max() to str to use next() & avoid StopIteration
    highest_quantity = str(max(quantity_list_int))
    
    # use next() to return the next item in an iterator
    # print this shoe as being for sale
    hi_quant_idx = (next(shoe for shoe in shoe_list if shoe[4] == highest_quantity))
    print() 
    print(f"The shoe with the highest quantity is {hi_quant_idx} with {highest_quantity} shoes.")
    print(f"{hi_quant_idx[2]} is for sale.")
    print()

def show_cost():
    # call method if the user wants to view product costs
    # create the objects from the shoe_list data by indexing sublists
    # print out the cost str
    for shoe in shoe_list:    
        country = shoe[0] 
        code = shoe[1] 
        product = shoe[2] 
        cost = shoe[3] 
        quantity = shoe[4]     
        inventory_obj = Shoe(country, code, product, cost, quantity)
        print(inventory_obj.get_cost())
    print()

#==========Main Menu=============

# print out a welcome statement
print("Welcome to the program for the shoes held in stock.")
print()

# create a list that holds the data to create shoe objects
shoe_obj_data = []

# create a list to store a list of objects of shoes.
shoe_list = []

# call functions to read data from inventory.txt and create objects from them
read_shoes_data() 
capture_shoes()

# create a menu that executes the functions above
# this menu should be inside the while loop
def main_menu():    
    while True: 
        menu = input('''Enter an option from the menu
va - view all
rs - restock
s - search for shoe
c - product cost
iv - item values
hq - for sale
q - quit
:\t
''').lower()

        if menu == 'va':        
            view_all(shoe_list)

        elif menu == 'rs':
            re_stock()

        elif menu == 's':
            search_shoe()

        elif menu == 'c':
            show_cost()

        elif menu == 'iv':            
            value_per_item()

        elif menu == 'hq':        
            highest_qty()

        elif menu == 'q':
            # use sys.exit() to prevent another loop if quitting & exit the program
            import sys
            print("Goodbye")
            sys.exit()            

        else:
            print("You have made a wrong choice. Please Try again.\n")

# call the menu function            
main_menu()
