# ============== Selwyn Panel Beaters MAIN PROGRAM ==============
# Student Name: Jiahua(Edward) XIECAO
# Student ID : 1158993
# NOTE: Make sure your two files are in the same folder
# =================================================================================

import spb_data    # spb_data.py MUST be in the SAME FOLDER as this file!
                    # spb_data.py contains the data
import datetime     # We areusing date times for this assessment, and it is
                    # available in the column_output() fn, so do not delete this line
import re

# Data variables
#col variables contain the format of each data column and help display headings
#db variables contain the actual data
col_customers = spb_data.col_customers
db_customers = spb_data.db_customers
col_services = spb_data.col_services
db_services = spb_data.db_services
col_parts = spb_data.col_parts
db_parts = spb_data.db_parts
#col_bills is useful for displaying the headings when listing bills
col_bills = spb_data.col_bills


def next_id(db_data):
    #Pass in the dictionary that you want to return a new ID number for, this will return a new integer value
    # that is one higher than the current maximum in the list.
    return max(db_data.keys())+1

def column_output(db_data, cols, format_str):
    # db_data is a list of tuples.
    # cols is a dictionary with column name as the key and data type as the item.
    # format_str uses the following format, with one set of curly braces {} for each column:
    #   eg, "{: <10}" determines the width of each column, padded with spaces (10 spaces in this example)
    #   <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
    #   The following example is for 3 columns of output: left-aligned 5 characters wide; centred 10 characters; right-aligned 15 characters:
    #       format_str = "{: <5}  {: ^10}  {: >15}"
    #   Make sure the column is wider than the heading text and the widest entry in that column,
    #       otherwise the columns won't align correctly.
    # You can also pad with something other than a space and put characters between the columns, 
    # eg, this pads with full stops '.' and separates the columns with the pipe character '|' :
    #       format_str = "{:.<5} | {:.^10} | {:.>15}"
    print(format_str.format(*cols))
    for row in db_data:
        row_list = list(row)
        for index, item in enumerate(row_list):
            if item is None:      # Removes any None values from the row_list, which would cause the print(*row_list) to fail
                row_list[index] = ""       # Replaces them with an empty string
            elif isinstance(item, datetime.date):    # If item is a date, convert to a string to avoid formatting issues
                row_list[index] = str(item)
        print(format_str.format(*row_list))


def list_customers():
    # List the ID, name, telephone number, and email of all customers

    # Use col_Customers for display
   
    # Convert the dictionary data into a list that displays the required data fields
    #initialise an empty list which will be used to pass data for display
    display_list = []
    #Iterate over all the customers in the dictionary
    for customer in db_customers.keys():
        #append to the display list the ID, Name, Telephone and Email
        display_list.append((customer,
                             db_customers[customer]['details'][0],
                             db_customers[customer]['details'][1],
                             db_customers[customer]['details'][2]))
    format_columns = "{: >4} | {: <15} | {: <12} | {: ^12}"
    print("\nCustomer LIST\n")    # display a heading for the output
    column_output(display_list, col_customers, format_columns)   # An example of how to call column_output function

    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output


def list_parts():
    # List the ID, name, cost of all parts
    display_list = []
    for part_id in db_parts.keys():
        display_list.append((part_id, db_parts[part_id][0], db_parts[part_id][1]))
    format_str = "{: <5} | {: ^10} | {: >15}"
    print("\nParts List\n")
    column_output(display_list, col_parts, format_str)



def list_services():
    # List the ID, name, cost of all services
    display_list = []
    for service_id in db_services.keys():
        display_list.append((service_id, db_services[service_id][0], db_services[service_id][1]))
    format_str = "{: <5} | {: ^20} | {: >15}"
    print("\nServices List\n")
    column_output(display_list, col_services, format_str)



def add_customer_name():
    valid = False
    first_name = input("Enter new customer first name(or X to return menu): ").strip(" ")
    if back_to_menu(first_name.strip("").upper()):
        return valid, first_name

    last_name = input("Enter new customer last name(or X to return menu): ").strip(" ")
    if back_to_menu(last_name.strip(" ").upper()):
        return valid, last_name

    if first_name.isalpha() and last_name.isalpha():
        valid = True
    full_name = first_name + " " + last_name
    return valid, full_name.title()

def add_customer_phone_number():
    valid = False
    phone_number = input("Enter new customer phone number(or X to return menu): ")
    if phone_number.isdigit():
        valid = True
    return valid, phone_number

def add_customer_email():
    valid = False
    email = input("Enter new customer email(or X to return menu): ")
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        valid = True
    return valid, email

def add_customer(id, name, phone, email):
    # Add a customer to the db_customers database, use the next_id to get an id for the customer.
    db_customers[id] = {"details": [name, phone, email]}
    print(f"New Customer-{new_customer_id} {new_customer_name} is added successfully!")

def add_job():
    # Add a Job to a customer
    # Remember to validate part and service ids

    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def bills_to_pay():
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def pay_bill():
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

# function to display the menu
def disp_menu():
    print("==== WELCOME TO SELWYN PANEL BEATERS ===")
    print(" 1 - List Customers")
    print(" 2 - List Services")
    print(" 3 - List Parts")
    print(" 4 - Add Customer")
    print(" 5 - Add Job")
    print(" 6 - Display Unpaid Bills")
    print(" 7 - Pay Bill")
    print(" X - eXit (stops the program)")

def back_to_menu(text):
    if text == "X":
        return True
    return False

# ------------ This is the main program ------------------------

# Display menu for the first time, and ask for response
disp_menu()

# Don't change the menu numbering or function names in this menu
# Repeat this loop until the user enters an "X"
finish = False
while not finish:
    response = input("Please enter menu choice: ").upper()
    if response == "X":
        finish = True
    if response == "1":
        list_customers()
    elif response == "2":
        list_services()
    elif response == "3":
        list_parts()
    elif response == "4":
        added = False
        valid_customer = {"name": None, "phone": None, "email": None}
        while not added:
            new_customer_id = next_id(db_customers)

            if valid_customer["name"] is None or valid_customer["name"] is False:
                if valid_customer["name"] is False:
                    print("The new customer name is not valid. Please type the name in letters.\n")
                valid_name, new_customer_name = add_customer_name()
                valid_customer["name"] = valid_name
                if back_to_menu((new_customer_name.strip(" ").upper())):
                    break

            if valid_customer["phone"] is None or valid_customer["phone"] is False:
                if valid_customer["phone"] is False:
                    print("The new customer phone number is not valid. Please type the phone number in digit.\n")
                valid_phone, new_customer_phone = add_customer_phone_number()
                valid_customer["phone"] = valid_phone
                if back_to_menu(new_customer_phone.strip(" ").upper()):
                    break

            if valid_customer["email"] is None or valid_customer["email"] is False:
                if valid_customer["email"] is False:
                    print("The new customer email address is not valid. Please type the email in this format 'example@domain.com'\n")
                valid_email, new_customer_email = add_customer_email()
                valid_customer["email"] = valid_email
                if back_to_menu(new_customer_email.strip(" ").upper()):
                    break

            if False not in valid_customer.values():
                add_customer(new_customer_id, new_customer_name, new_customer_phone, new_customer_email)
                added = True

    elif response == "5":

        add_job()
    elif response == "6":
        bills_to_pay()
    elif response == "7":
        pay_bill()
    else:
        print("\n***Invalid response, please try again (enter 1-6 or X)")

    print("")
    disp_menu()

print("\n=== Thank you for using Selywn Panel Beaters! ===\n")
