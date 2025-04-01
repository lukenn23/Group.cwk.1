import pandas as pd
import pickle


#------------------------ Manager Accounts --------------------------------------------------------------------------

managers = [
    {"first_name": "Sarah", "surname": "Smith", "username": "SSmith", "password": "PASSWORD", "role": "Manager", "task": "A"},
    {"first_name": "Akshay", "surname": "Shah", "username": "AShah", "password": "PASSWORD", "role": "Manager", "task": "B"},
    {"first_name": "Huhan", "surname": "Yang", "username": "HYang", "password": "PASSWORD", "role": "Manager", "task": "C"},
    {"first_name": "Jo", "surname": "Admin", "username": "JAdmin", "password": "PASSWORD", "role": "Admin"},  # Junior System Admin
    {"first_name": "Mike", "surname": "Boss", "username": "MBoss", "password": "PASSWORD", "role": "DepartmentManager"}
]


# Passwords initially set to "PASSWORD")

# Save manager list as a pickle file
with open("managers.pkl", "wb") as f:
    pickle.dump(managers, f)

#------------------------ Worker List ------------------------------------------------------------------------------------

# List of worker names
workers = [
    "Thomas Anthony",
    "Wen Chua",
    "Chengze Goh",
    "Pratik Suthar",
    "Francis Grover",
    "Chris Alvarez"
]

# Save the lsit of workers to a file
with open("workers.pkl", "wb") as f:
    pickle.dump(workers, f)

#--------------------- Current Month DataFrame ----------------------------------------------------------------------------

# Store entries fr the current month (Jan 2025)
current_month_df = pd.DataFrame(columns=[
    "Date",             # "2025-01" to begin with
    "Worker",           # Match name to workers list
    "Task",             # A, B, or C
    "Tasks Completed",  # Integer number of tasks done
    "Manager"           # The manager who entered the task
])

#Pre-Set the date column format
current_month_df["Date"] = pd.Series(dtype="str")

# Save the empty DataFrame using pickle
with open("current_month.pkl", "wb") as f:
    pickle.dump(current_month_df, f)

# Final message to confirm everything worked
print("Setup complete. 'managers.pkl', 'workers.pkl', and 'current_month.pkl' have been created.")
