"""

        program: Warehouse management system
        author: Nora Guerrero
        Description:
        1- Register new item
            id (auto generated)
            title (str)
            category (str)
            price (float)
            stock (int)

        2 - Display Catalog
        3 - Update stock
        4 - Remove item from catalog
        5 - Print Total stock value
        6 - Report - out of stock

"""
#imports
from menu import clear, print_menu, print_header, print_item
from item import Item
import pickle

#Global Vars
catalog = []
data_file = 'warehouse.data'
last_id = 1

def serialize_catalog():
    global data_file
    writer = open('warehouse.data', 'wb') #create open a file to write binary
    pickle.dump(catalog, writer)
    writer.close() #close stream, realease the file
    print("**Data serialized!**")

def deserialize_catalog():
    try:
        global data_file
        global last_id
        reader = open(data_file, 'rb')
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)
        
        last_item = catalog[-1]
        last_id = last_item.id + 1
        print("** Deserialized " + str(len(catalog)) + "items" )

    except:
        print("Error, cannot load data!")


def register_item():
    global last_id
    try: 
        print_header("Register New Item")
        title = input("Please provide the Title: ")
        cat = input("Please provide the Category: ")
        price = float(input("Please provide the Price: "))
        stock = int(input("Please provide the Stock: "))

        id = last_id
        item = Item(id, title, cat, price, stock)
        catalog.append(item)

        how_many = len(catalog)
        print("You now have: "+ str(how_many)+ "item on catalog")

    #item.id = id
    #item.title = title
    #item.category = cat
    #item.price = price
    #item.stock = stock 

    #You are missing this:
    except ValueError:
        print('Error: incorrect value, try again')
    except:
        print("Error, Something went wrong")

def update_stock():
    try:
        display_catalog()
        id = input("Please provide the Item id: ")
        found = False
        for item in catalog:
            if(str(item.id)== id):
                found = True
                val = input("please provide new stock value: ")
                item.stock = int(val)
                print("stock value updated!")
            
            if(not found):
                print("**Error: Invalid ID, verify and try again!")
    except  ValueError:
        print('Error: Invalid ID, verify and try again')
    except:
        print("Error, Something went wrong")

def update_price():
    try:
        display_catalog()
        id = input("Please provide the Item id: ")
        found = False
        for item in catalog:
            if(str(item.id)== id):
                found = True
                val = input("please provide new price value: ")
                item.price = float(val)
                print("Price value updated!")
            
            if(not found):
                print("**Error: Invalid ID, verify and try again!")
    except  ValueError:
        print('Error: Invalid ID, verify and try again')
    except:
        print("Error, Something went wrong")


def display_catalog():
    print_header("Your Current Catalog")
    for item in catalog:
        print_item(item)
        #print(
        #     str(item.id).rjust(3)
        #   + " | " + item.title.ljust(25) 
        #   + " | " + item.category.ljust(12) 
        #   + " | " + str(item.stock).rjust(12)
        #   + " | $" + str(item.price).rjust(15)
          
        #)

        #print('_' * 80)


def display_out_of_stock():
    print_header("Items currently out of stock")
    for item in catalog:
        if(item.stock == 0):
            print_item(item)

def total_stock_value():
    total = 0.0
    for item in catalog:
        total += item.price * item.stock

    print("Total Value: " + str(total))        

#Delete on python from list
# By index from catalog [2]
# by item    
def delete_item():
    display_catalog()
    id - input("Please input item id:")
    found - False
    for item in catalog:
        if(str(item.id)--id):
            found - True
            print_item(item)
            del catalog[int(id)--1]
            found 
            print ("item deleted")


#instructions
deserialize_catalog()
input("Press enter to continue")

opc= ''
while(opc!='x'):
    clear()
    print_menu()

    opc = input('Please chose an option: ')


    #if comparisons
    if (opc == '1'):
        register_item()
        serialize_catalog()
    elif (opc == '2'):
        display_catalog()
    elif (opc == '3'):
        update_stock()
        serialize_catalog()
    elif (opc == '6'):
        display_out_of_stock()
    elif (opc == '7'):
        total_stock_value()   


    input("Press enter to continue")

