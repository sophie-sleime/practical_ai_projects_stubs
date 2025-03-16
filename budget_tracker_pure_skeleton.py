
# Mini Budget Tracker
# A simple program to track expenses using dictionaries

# TODO: Create a dictionary to store budget information with these keys:
# - "total": for storing the total budget (start at 0)
# - "spent": for tracking total amount spent (start at 0)
# - "categories": an empty dictionary to track spending by category


# TODO: Create the set_budget function that:
# - Takes parameter: amount (float)
# - Updates the 'total' key in the budget dictionary to the amount
# - Prints a message confirming the budget was set


# TODO: Create the add_expense function that:
# - Takes parameters: category (str) and amount (float)
# - Adds the amount to the total spent (budget["spent"])
# - Checks if the category already exists in the categories dictionary
# - If it exists, adds the amount to that category
# - If it doesn't exist, creates it and sets it to the amount
# - Prints a message confirming the expense was added


# TODO: Create the get_remaining function that:
# - Takes no parameters
# - Calculates and returns the difference between total budget and total spent


# TODO: Create the show_summary function that:
# - Takes no parameters
# - Prints a header for the budget summary
# - Shows the total budget, total spent, and remaining amount
# - Checks if there are any categories with expenses
# - If there are, prints each category and its amount
# - If not, prints a message that no expenses have been recorded


# TODO: Create the main program that:
# - Prints a welcome message
# - Creates a menu loop with these options:
#   1. Set budget
#   2. Add expense
#   3. Show summary
#   4. Exit
# - For option 1: Gets budget amount from user, calls set_budget
# - For option 2: Gets category and amount from user, calls add_expense
# - For option 3: Calls show_summary
# - For option 4: Prints goodbye message and exits
# - For invalid options: Shows error message
