
# Simple Study Timer
# A basic program for tracking study time using lists

# TODO: Create two empty lists to store our study data
# - One list for subject names
# - One list for minutes studied


# TODO: Create the add_session function that:
# - Takes parameters: subject (str) and time (int)
# - Appends the subject to the subjects list
# - Appends the time to the minutes list
# - Prints a message confirming the addition


# TODO: Create the total_study_time function that:
# - Takes no parameters
# - Calculates and returns the sum of all minutes studied


# TODO: Create the subject_study_time function that:
# - Takes parameter: subject_name (str)
# - Creates a variable to keep track of the total time for this subject
# - Loops through the subjects list
# - If the current subject matches subject_name, adds the corresponding time to your total
# - Returns the total time for this subject


# TODO: Create the show_all_sessions function that:
# - Takes no parameters
# - Prints a header for the study sessions
# - Checks if there are any sessions recorded
# - If no sessions, prints a message and returns
# - Otherwise, loops through the lists and prints each session
# - Prints the total study time using the total_study_time function


# TODO: Create the main program that:
# - Prints a welcome message
# - Creates a menu loop with these options:
#   1. Add study session
#   2. View all sessions
#   3. Check subject study time
#   4. Exit
# - For option 1: Gets subject and minutes from user, calls add_session
# - For option 2: Calls show_all_sessions
# - For option 3: Gets subject from user, calls subject_study_time, displays result
# - For option 4: Prints goodbye message and exits
# - For invalid options: Shows error message
