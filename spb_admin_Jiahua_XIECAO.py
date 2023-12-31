# ============== Selwyn Panel Beaters MAIN PROGRAM ==============
# Student Name: Jiahua (Edward) XIECAO
# Student ID : 1158993
# NOTE: Make sure your two files are in the same folder
# =================================================================================

import spb_data  # spb_data.py MUST be in the SAME FOLDER as this file!
# spb_data.py contains the data
import datetime  # We areusing date times for this assessment, and it is
import re

# available in the column_output() fn, so do not delete this line

# Data variables
# col variables contain the format of each data column and help display headings
# db variables contain the actual data
col_customers = spb_data.col_customers
db_customers = spb_data.db_customers
col_services = spb_data.col_services
db_services = spb_data.db_services
col_parts = spb_data.col_parts
db_parts = spb_data.db_parts
# col_bills is useful for displaying the headings when listing bills
col_bills = spb_data.col_bills


def next_id(db_data):
    # Pass in the dictionary that you want to return a new ID number for, this will return a new integer value
    # that is one higher than the current maximum in the list.
    return max(db_data.keys()) + 1


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
            if item is None:  # Removes any None values from the row_list, which would cause the print(*row_list) to fail
                row_list[index] = ""  # Replaces them with an empty string
            elif isinstance(item, datetime.date):  # If item is a date, convert to a string to avoid formatting issues
                row_list[index] = str(item)
        print(format_str.format(*row_list))


def list_customers():
    # List the ID, name, telephone number, and email of all customers

    # Use col_Customers for display

    # Convert the dictionary data into a list that displays the required data fields
    # initialise an empty list which will be used to pass data for displaya
    display_list = []
    # Iterate over all the customers in the dictionary
    for customer in db_customers.keys():
        # append to the display list the ID, Name, Telephone and Email
        display_list.append((customer,
                             db_customers[customer]['details'][0],
                             db_customers[customer]['details'][1],
                             db_customers[customer]['details'][2]))
    format_columns = "{: >4} | {: <15} | {: <12} | {: ^12}"
    print("\nCustomer LIST\n")  # display a heading for the output
    column_output(display_list, col_customers, format_columns)  # An example of how to call column_output function


def back_to_menu(text):
    if text.strip(" ").upper() == "X":
        return True
    return False


def list_parts():
    # List the ID, name, cost of all parts
    display_list = []
    for part_id in db_parts.keys():
        display_list.append((part_id, db_parts[part_id][0], db_parts[part_id][1]))
    display_list.sort(key=lambda data: data[1])
    format_str = "{: <5} | {: ^10} | {: >15}"
    print("\nParts List\n")
    column_output(display_list, col_parts, format_str)


def list_services():
    # List the ID, name, cost of all services
    display_list = []
    for service_id in db_services.keys():
        display_list.append((service_id, db_services[service_id][0], db_services[service_id][1]))
    display_list.sort(key=lambda data: data[1])
    format_str = "{: <5} | {: ^20} | {: >15}"
    print("\nServices List\n")
    column_output(display_list, col_services, format_str)


def validate_customer_name(customer):
    valid = customer["name"]
    if valid is None or valid is False:
        if valid is False:
            print("The new customer name is not valid. Please type the name in letters.\n")
        first_name = input("Enter new customer first name(or X to return to menu): ").strip(" ")
        if back_to_menu(first_name):
            return customer, first_name

        last_name = input("Enter new customer last name(or X to return to menu): ".strip(" "))
        if back_to_menu(last_name):
            return customer, last_name

        if first_name.isalpha() and last_name.isalpha():
            valid = True
        else:
            valid = False
        full_name = first_name + " " + last_name
        customer["name"] = valid
        return customer, full_name.title()


def validate_customer_phone(customer):
    valid = customer["phone"]
    if valid is None or valid is False:
        if valid is False:
            print("The new customer phone number is not valid. Please type the phone number in digit.\n")
        phone_number = input("Enter new customer phone number(or X to return menu): ")
        if phone_number.isdigit():
            valid = True
        else:
            valid = False
        customer["phone"] = valid
        return customer, phone_number


def validate_customer_email(customer):
    valid = customer["email"]
    if valid is None or valid is False:
        if valid is False:
            print("The new customer email address is not valid. Please type the email "
                  "in this format 'example@domain.com'\n")
        email = input("Enter new customer email(or X to return menu): ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            valid = True
        else:
            valid = False
        customer["email"] = valid
        return customer, email

def validate_customer_bill(customer_id, date):
    if date in db_customers[customer_id]["jobs"].keys():
        return True
    else:
        return False


def add_customer():
    # Add a customer to the db_customers database, use the next_id to get an id for the customer.
    # Remember to add all required dictionaries.
    customer_added = False
    valid_customer = {"name": None, "phone": None, "email": None}
    while not customer_added:
        new_customer_id = next_id(db_customers)

        # ask the name if it is empty and check its validation
        if not valid_customer["name"]:
            valid_customer, new_customer_name = validate_customer_name(valid_customer)
            if back_to_menu(new_customer_name):
                break

        # ask the phone if it is empty and check its validation
        if not valid_customer["phone"]:
            valid_customer, new_customer_phone = validate_customer_phone(valid_customer)
            if back_to_menu(new_customer_phone):
                break

        # ask the email if it is empty and check its validation
        if not valid_customer["email"]:
            valid_customer, new_customer_email = validate_customer_email(valid_customer)
            if back_to_menu(new_customer_email):
                break

        if False not in valid_customer.values():
            db_customers[new_customer_id] = {"details": [new_customer_name, new_customer_phone, new_customer_email]}
            db_customers[new_customer_id]["jobs"] = {}
            customer_added = True
            print(f"New Customer-{new_customer_id} {new_customer_name} is added successfully!")


def find_customer(found):
    list_customers()
    customer_id = input("Enter customer id(or X to return menu): ")
    if back_to_menu(customer_id):
        return found, customer_id
    try:
        if int(customer_id) not in db_customers.keys():
            print(f"{customer_id} can not be found. Please enter a valid customer id.")
        else:
            found = True
    except ValueError:
        print(f"{customer_id} can not be found. Please enter a valid customer id.")
    return found, customer_id


def add_services(services_added, services, cost):
    list_services()
    service_to_add = input("Enter service id(X to return menu or Enter to next step): ")
    if back_to_menu(service_to_add):
        return services_added, service_to_add, cost
    try:
        if service_to_add == "":
            services_added = True
        elif int(service_to_add) not in db_services.keys():
            print(f"{service_to_add} can not be found. Please try a valid service id.")
        else:
            services += (int(service_to_add),)
            cost += db_services[int(service_to_add)][1]
            print(f"{db_services[int(service_to_add)][0]} added successfully!")
        return services_added, services, cost
    except ValueError:
        print(f"{service_to_add} can not be found. Please enter a valid service id")
        return services_added, services, cost


def add_parts(parts_added, parts, cost):
    list_parts()
    part_to_add = input("Enter part id(X to return menu or Enter to next step): ")
    if back_to_menu(part_to_add):
        return parts_added, part_to_add, cost
    try:
        if part_to_add == "":
            parts_added = True
        elif int(part_to_add) not in db_parts.keys():
            print(f"{part_to_add} can not be found. Please try a valid service id.")
        else:
            # if int(part_to_add) in parts:
            #     print(f"{db_parts[int(part_to_add)][0]} was added before.")
            # else:
            parts += (int(part_to_add),)
            cost += db_parts[int(part_to_add)][1]
            print(f"{db_parts[int(part_to_add)][0]} added successfully!")
        return parts_added, parts, cost
    except ValueError:
        print(f"{part_to_add} can not be found. Please enter a valid service id")
        return parts_added, parts, cost


def add_job():
    # Add a Job to a customer
    cost = 0
    customer_found = False
    services_added = False
    parts_added = False
    services = ()
    parts = ()
    while not customer_found:
        customer_found, customer_id = find_customer(customer_found)
        if back_to_menu(customer_id):
            break

    while not services_added and customer_found:
        services_added, services, cost = add_services(services_added, services, cost)
        try:
            if back_to_menu(services):
                break
        except AttributeError:
            continue

    while not parts_added and services_added and customer_found:
        parts_added, parts, cost = add_parts(parts_added, parts, cost)
        try:
            if back_to_menu(parts):
                break
        except AttributeError:
            continue

    if customer_found and services_added and parts_added:
        job_date = datetime.date.today()
        db_customers[int(customer_id)]["jobs"] = {job_date: [services, parts, cost, False]}
        print(f"Customer {customer_id}'s job added successfully!")


def bills_to_pay(customer_id=None):
    display_list = []
    if customer_id is None:
        for customer_id in db_customers.keys():
            name = db_customers[customer_id]["details"][0]
            phone = db_customers[customer_id]["details"][1]
            for job_date in db_customers[customer_id]["jobs"].keys():
                job = db_customers[customer_id]["jobs"][job_date]
                if job[3] is False:
                    display_list.append((name, phone, job_date, job[2]))
    else:
        name = db_customers[customer_id]["details"][0]
        phone = db_customers[customer_id]["details"][1]
        for job_date in db_customers[customer_id]["jobs"]:
            if db_customers[customer_id]["jobs"][job_date][3] is False:
                cost = db_customers[customer_id]["jobs"][job_date][2]
                display_list.append((name, phone, job_date, cost))

    format_columns = "{: >15} | {: <10} | {: <12} | {: ^12}"
    print("\nUnpaid bill LIST\n")  # display a heading for the output
    column_output(display_list, col_bills, format_columns)  # An example of how to call column_output function


def pay_bill():
    # find customer
    customer_found = False
    while not customer_found:
        customer_found, customer_id = find_customer(customer_found)
        if back_to_menu(customer_id):
            break

    if False not in [data[3] for data in db_customers[int(customer_id)]["jobs"].values()]:
        print(f"Customer{int(customer_id)} {db_customers[int(customer_id)]["details"][0]} no outstanding bill.")
    else:
        while True:
            bills_to_pay(int(customer_id))
            date_string = input("Enter the bill date to pay:")
            if back_to_menu(date_string):
                break
            try:
                date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
                valid = validate_customer_bill(int(customer_id), date_object)

                name = db_customers[int(customer_id)]["details"][0]
                if valid:
                    db_customers[int(customer_id)]["jobs"][date_object][3] = True
                    print(f"Customer {name}'s bill on {date_object} is paid!")
                    break
                else:
                    print(f"Customer {name} doesn't have a bill on {date_object}")
            except ValueError:
                print("Enter bill date in this format (year-month-day)")


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


# ------------ This is the main program ------------------------

# Display menu for the first time, and ask for response
disp_menu()
response = input("Please enter menu choice: ").upper()

# Don't change the menu numbering or function names in this menu
# Repeat this loop until the user enters an "X"
while response != "X":
    if response == "1":
        list_customers()
    elif response == "2":
        list_services()
    elif response == "3":
        list_parts()
    elif response == "4":
        add_customer()
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
    response = input("Please select menu choice: ").upper()

print("\n=== Thank you for using Selywn Panel Beaters! ===\n")
