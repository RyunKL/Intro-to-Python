# Lab Professor: Reza
# Ryan Lee | 101296633
# Menu Page displays all options user can take
def menu_page():
    print("---------------------------------------")
    print("| 1) Create Employee                   |")
    print("| 2) Create Item                       |")
    print("| 3) Make Purchase                     |")
    print("| 4) All Employee Summary              |")
    print("| 5) Exit                              |")
    print("---------------------------------------")


# arrays used to store personal information
employee_info = []
item_info = []
item_price = 0
discount = 0


# --- INPUT VALIDATION FUNCTIONS ---
# function that checks for empty inputs
def get_valid_input(prompt_message):
    while True:
        user_input = input(prompt_message)
        if user_input:
            return user_input
        print("Input can not be empty. Please try again.")


# function that checks inputs to be integer datatype
def get_valid_number(prompt_message):
    while True:
        user_input = input(prompt_message)
        if user_input and user_input.isnumeric():
            return int(user_input)  # return integer
        print("Please enter a number: ")


# function that accepts two arguments, an input message and an array of accepted values
def get_valid_type(prompt_message, types):
    while True:
        user_input = input(prompt_message)
        if user_input and user_input in types:
            return user_input
        print("Please enter one of the following value: " + ', '.join(types))


# --- INPUT VALIDATION FUNCTIONS FOR MAKE PURCHASE ---
# function that searches whether the input chosen exists or not
def search_array(array, category_index, user_input):
    for category in array:
        if category[category_index] == user_input:
            return True
    return False


# function that searches item array and returns the price of selected item
def get_price(item_id):
    global item_price
    for item in item_info:
        if item[0] == item_id:
            item_price = item[2]
    return item_price


# function that searches employee array and returns the calculated discount
def get_discount(discount_id):
    global discount
    for employee in employee_info:
        if discount_id == employee[6] and employee[2] == "manager":
            discount = 0.1 + (employee[3] * 0.02)
            if discount > 0.2:
                discount = 0.2
        elif discount_id == employee[6] and employee[2] == "hourly":
            discount = employee[3] * 0.02
            if discount > 0.1:
                discount = 0.1
    return discount


# function that updates the total purchases and total discounts an employee makes and updates the array
def update_total_purchases(discount_id, item_discount, purchased_cost):
    for employee in employee_info:
        if discount_id == employee[6]:
            if employee[5] < 200:
                employee[5] += item_discount
                employee[4] += purchased_cost
                if employee[5] > 200:
                    employee[5] -= item_discount
                    print("Employee has exceeded the allowed discounts, purchase failed")
                    break
                print("Success! Employee has purchased item!")
            else:
                print("Employee has exceeded the allowed discounts, purchase failed")


# function that asks user for input and calls on the functions that preforms the desired task user wants
def main_menu(choice):
    while 0 < choice < 5:
        if choice == 1:
            create_employee()
            return_input = get_valid_type("Do you wish to go back to main menu? (y/n): ", ["y", "n"])
            if return_input == 'y':
                menu_page()
                choice = get_valid_number("Please Select an option (1 - 5): ")
                while choice < 1 or choice > 5:
                    choice = get_valid_number("Please enter a valid option (1 - 5): ")
                main_menu(choice)
                break
            break
        if choice == 2:
            create_item()
            return_input = get_valid_type("Do you wish to go back to main menu? (y/n): ", ["y", "n"])
            if return_input == 'y':
                menu_page()
                choice = get_valid_number("Please select an option (1 - 5): ")
                while choice < 1 or choice > 5:
                    choice = get_valid_number("Please enter a valid option (1 - 5): ")
                main_menu(choice)
                break
            break
        if choice == 3:
            make_purchase()
            return_input = get_valid_type("Do you wish to go back to the main menu? (y/n): ", ["y", "n"])
            if return_input == 'y':
                menu_page()
                choice = get_valid_number("Please Select an option (1 - 5): ")
                while choice < 1 or choice > 5:
                    choice = get_valid_number("Please enter a valid option (1 - 5): ")
                main_menu(choice)
                break
            break
        if choice == 4:
            all_employee_summary()
            return_input = get_valid_type("Do you wish to go back to the main menu? (y/n): ", ["y", "n"])
            if return_input == 'y':
                menu_page()
                choice = get_valid_number("Please Select an option (1 - 5): ")
                while choice < 1 or choice > 5:
                    choice = get_valid_number("Please enter a valid option (1 - 5): ")
                main_menu(choice)
                break
            break
    print("You've successfully exited.")


# function that prompts user input on an employee and appends it to an array
def create_employee():
    choice = 'y'
    while choice == 'y':
        # user inputs all the various fields for new employee
        employee_id = get_valid_number("Enter Employee ID: ")
        # checks the array if employee entered exists. If it does program will prompt user for another
        while search_array(employee_info, 0, employee_id):
            employee_id = get_valid_number("Employee ID already in use, Please input another: ")
        employee_name = get_valid_input("Enter Employee Name: ")
        employee_type = get_valid_type("Enter Employee Type: ", ["manager", "hourly"])
        employee_years_worked = get_valid_number("Enter Employee Total Years Worked: ")
        employee_total_purchased = 0
        employee_total_discounts = 0
        employee_discount_number = get_valid_number("Enter Employee's Discount Number: ")
        while search_array(employee_info, 6, employee_discount_number):
            employee_discount_number = get_valid_number("Employee discount number already in use,"
                                                        " Please input another: ")
        # append the new input as an employee in our array
        employee_info.append(
            [employee_id, employee_name, employee_type, employee_years_worked, employee_total_purchased,
             employee_total_discounts,
             employee_discount_number, 0])
        print("Employee with ID " + str(employee_id) + " is successfully added.")
        choice = get_valid_type("Do you wish to add another employee? (y/n) ", ["y", "n"])
        if choice != 'y':
            print("You've successfully exited")


def create_item():
    choice = 'y'
    while choice == 'y':
        # user inputs all the various fields for the new item
        item_id = get_valid_number("Please enter the Item Number: ")
        while search_array(item_info, 0, item_id):
            item_id = get_valid_number("item ID already in use, please input another: ")
        item_name = get_valid_input("Please enter the Item Name: ")
        item_cost = get_valid_number("Please enter the Item Price: ")
        # append function to add item to our current array of items
        item_info.append([item_id, item_name, item_cost, 0])
        print("Item with ID " + str(item_id) + " has been successfully added.")
        choice = get_valid_type("Do you wish to add another item? (y/n): ", ["y", "n"])
        if choice != 'y':
            print("You've successfully exited.")


# function that preforms task 3 makes purchases
def make_purchase():
    choice = 'y'
    while choice == 'y':
        # prints the item_info array
        print("Item Number: , Item Name: , Item Price: ")
        for item in item_info:
            print("[" + str(item[0]) + ", " + str(item[1]) + ", " + str(item[2]) + "]")
        user_input_id = get_valid_number("Please enter the item Number you wish to purchase: ")
        # searches the item_info for the specific category requested
        while not search_array(item_info, 0, user_input_id):
            user_input_id = get_valid_number("Item does not exist, please enter a valid item number: ")
        user_input_discount_num = get_valid_number("Please enter your employee discount number: ")
        while not search_array(employee_info, 6, user_input_discount_num):
            user_input_discount_num = get_valid_number("Discount number does not exist, please enter a valid discount "
                                                       "number: ")
        # these lines of code get the discount price % and $ amount and update the employee array
        purchase_price = get_price(user_input_id)
        employee_discount = get_discount(user_input_discount_num)
        item_discount = purchase_price * employee_discount
        final_cost = purchase_price - item_discount
        item_discount = round(item_discount, 2)
        final_cost = round(final_cost, 2)
        update_total_purchases(user_input_discount_num, item_discount, final_cost)
        choice = get_valid_type("Another Purchase? (y/n): ", ["y", "n"]).lower()
        if choice != 'y':
            print("You've successfully exited.")


# prints the employee_info array
def all_employee_summary():
    print('Employee Number: ,Employee Name: ,Years Worked: ,Total Purchases: ,Total Discounts: ,Discount Number: ')
    for employee in employee_info:
        print("[" + str(employee[0]) + ", " + str(employee[1]) + " ," + str(employee[2]) + ", " + str(employee[3]) +
              ", {:0.2f}".format(employee[4]) + ", {:0.2f}".format(employee[5]) + ", " + str(employee[6]) + "]")


# functions are called
menu_page()
user_choice = get_valid_number("Please select an option (1 - 5):  ")
while user_choice < 1 or user_choice > 5:
    user_choice = get_valid_number("Please enter a valid option (1 - 5): ")
main_menu(user_choice)
