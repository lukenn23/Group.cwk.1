import pickle
import pandas as pd
import os

if os.path.exists("historic_data.pkl"):
    with open("historic_data.pkl", "rb") as f:
        historic_df = pickle.load(f)
    print("✅ historic_data.pkl FOUND")
    print("Number of rows:", len(historic_df))
    print(historic_df.head())
else:
    print("❌ historic_data.pkl NOT FOUND")


#Load managers from file

with open("managers.pkl", "rb") as f: # Open the file and load the list of managers
    managers = pickle.load(f)

#Load workers from file
with open("workers.pkl", "rb") as f:
    workers = pickle.load(f)

#function to save data after changes have been made
def save_all():
    with open("managers.pkl", "wb") as f:
        pickle.dump(managers, f)

    with open("workers.pkl", "wb") as f:
        pickle.dump(workers, f)

# Admin menu function
def admin_menu(user):
    while True:
        print("\n--- Junior System Admin Menu ---")
        print("1. Add new task manager")
        print("2. Reset manager password")
        print("3. Add new worker")
        print("4. Delete a manager")
        print("5. Delete a worker")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            # Add new manager
            first = input("Enter first name: ")
            last = input("Enter surname: ")
            task = input("Enter task they manage (A, B, or C): ").upper()
            username = first[0] + last  # First initial + surname
            password = "PASSWORD" # Default password
            role = "Manager"

            # Add new manager dictionary
            new_manager = {
                "first_name": first,
                "surname": last,
                "username": username,
                "password": password,
                "role": role,
                "task": task
            }
            managers.append(new_manager) # Add manager to the list
            print("New manager added with username:", username)
            save_all() # Save the new updated file

        elif choice == "2":
            # Reset password
            uname = input("Enter username of manager to reset: ").strip()
            found = False
            for m in managers: # Search through all the managers
                if m["username"] == uname and m["role"] == "Manager": # 
                    m["password"] = "PASSWORD" # Reset to default "PASSWORD"
                    found = True
                    print("Password has been reset to 'PASSWORD'.")
                    save_all()
                    break
            if not found:
                print("Manager not found.") # Error message if manager is not in the file

        elif choice == "3":
            # Add new worker
            first = input("Enter worker's first name: ")
            last = input("Enter worker's surname: ")
            full_name = first + " " + last
            if full_name in workers:
                print("Worker already exists.")
            else:
                workers.append(full_name)
                print("Worker added:", full_name)
                save_all() # Save the uodated file

        elif choice == "4":
            # Delete manager
            uname = input("Enter username of manager to delete: ").strip()
            original_len = len(managers)
            managers[:] = [m for m in managers if m["username"] != uname] # Only keep the managers that dont't match the username
            if len(managers) < original_len: # If a manger is deleted
                print("Manager deleted.")
                save_all() # Save updated file 
            else:
                print("Manager not found.") # No need to save again as file isnt changed

        elif choice == "5":
            # Delete worker
            name = input("Enter full name of worker to delete: ")
            if name in workers:
                workers.remove(name)
                print("Worker deleted.") # Confirm to the user that worker has been deleted
                save_all()
            else:
                print("Worker not found.")

        elif choice == "6":
            print("Exiting admin menu.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")




def manager_menu(user):
    task_letter = user["task"] # Task A B or C
    manager_name = user["first_name"] + " " + user["surname"]

    #Load current month DataFrame
    try:
        with open("current_month.pkl", "rb") as f:
            current_df = pickle.load(f)
    except:
        current_df = pd.DataFrame(columns=["Date", "Worker", "Task", "Tasks completed", "Manager"]) # If the file doesn't exist, create new DataFrame

    # Create the menu
    while True:
        print("\n--- Task Manager Menu ---")
        print("1. Add a task entry")
        print("2. View current entries")
        print("3. Edit a task entry")
        print("4. Delete a task entry")
        print("5. View historic data")
        print("6. Change password")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip() # Prompt user to select an otion from the menu

        if choice == "1":
            worker = input("Enter full name of worker: ")
            tasks_done = int(input("Enter the number of tasks completed: "))
            
            #Format new dictionary  
            new_entry = {
                "Date": "2025-01",
                "Worker": worker,
                "Task": task_letter,
                "Tasks Completed": tasks_done,
                "Manager": manager_name
            }

            current_df = pd.concat([current_df, pd.DataFrame([new_entry])], ignore_index=True)# Add new line to DataFrame
            print("Entry Added! ")

        elif choice =="2":
            # Only the rows added by this manager
            view_df = current_df[(current_df["Task"] == task_letter) & (current_df["Manager"] == manager_name)] # Filter to show rows relevant to the manager
            print("\nYour current entries for this month: ")
            print(view_df)

        elif choice == "3":
            print("Here are your entries: ")
            manager_entries = current_df[(current_df["Task"] == task_letter) & (current_df["Manager"] == manager_name)] # Only entries relevant to this manager
            print(manager_entries)

            index_to_edit = int(input("Enter the index number of the entry to edit(Starting from 0): ")) # Choose the entry the manager wants to edit
            if index_to_edit in current_df.index:
                new_value = int(input("Enter new number of tasks completed: "))
                current_df.at[index_to_edit, "Tasks Completed"] = new_value
                print("Entry updated.") # Confirm entry has been edited
            else:
                print("Invalid index.")

        elif choice == "4":
            print("Here are your entries: ")
            manager_entries = current_df[(current_df["Task"] == task_letter) & (current_df["Manager"] == manager_name)]
            print(manager_entries)

            index_to_delete = int(input("Enter the index number of the entry to delete: "))
            if index_to_delete in current_df.index:
                current_df = current_df.drop(index=index_to_delete)
                print("Entry deleted.")
            else:
                print("Invalid index.")

        elif choice == "5":
            try: # Load the historic data from file
                with open("historic_data.pkl", "rb") as f:
                    historic_df = pickle.load(f)
                filtered = historic_df[historic_df["Task"] == task_letter] # Show entries for the manager's task
                print("Historic data for your task:")
                print(filtered)
            except:
                print("No historic data found.")

        elif choice == "6":
            new1 = input("Enter new password: ")
            new2 = input("Confirm new password: ")
            if new1 == new2: # Find the manager in the list 
                for m in managers:
                    if m["username"] == user["username"]:
                        m["password"] = new1
                        print("Password updated.")
                        save_all()
                        break
            else:
                print("Passwords did not match.")

        elif choice == "7":
             # Save updated current month entries
            with open("current_month.pkl", "wb") as f:
                pickle.dump(current_df, f)
            print("Exiting manager menu.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
        


def department_menu(user):
    #Load current month data if it exists
    try:
        with open("current_month.pkl", "rb") as f:
            current_df = pickle.load(f)
    except:
        current_df = pd.DataFrame(columns=["Date", "Worker", "Task", "Tasks Completed", "Manager"])

    #Load historic data if it exists
    try:
        with open("historic_data.pkl", "rb") as f:
            historic_df = pickle.load(f)
    except:
        historic_df = pd.DataFrame(columns=["Date", "Worker", "Task", "Tasks Completed", "Manager"])

    # Create menu
    while True:
        print("\n--- Departmental Manager Menu ---")
        print("1. View all historic data")
        print("2. Finalize current month and start new month")
        print("3. View summary data (e.g. totals per worker)")
        print("4. Estimate revenue")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice =="1":
            if historic_df.empty:
                print("No historic data available.")
            else:
                print(historic_df)

        
        elif choice == "2":
            if current_df.empty:
                print("No data to finalize.")
            else:
                # Combine task entries by worker and task (summarize within the month)
                grouped = current_df.groupby(["Date", "Worker", "Task", "Manager"], as_index=False)["Tasks Completed"].sum()

                # Add to historic data
                historic_df = pd.concat([historic_df, grouped], ignore_index=True)

                # Save updated historic data
                with open("historic_data.pkl", "wb") as f:
                    pickle.dump(historic_df, f)

                # Prepare new empty DataFrame for next month
                next_month_df = pd.DataFrame(columns=["Date", "Worker", "Task", "Tasks Completed", "Manager"])
                with open("current_month.pkl", "wb") as f:
                    pickle.dump(next_month_df, f)

                print("Month finalized and new current month started.")

        elif choice == "3":
            if historic_df.empty:
                 print("No data available.")
            else:
                # Group by worker and task, then sum the completed tasks
                summary = historic_df.groupby(["Worker", "Task"])["Tasks Completed"].sum().reset_index()

                # Pivot the table so each task becomes a column (A, B, C)
                summary_pivot = summary.pivot(index="Worker", columns="Task", values="Tasks Completed").fillna(0)

                print("Summary of total tasks completed by each worker (A, B, C):")
                print(summary_pivot)

        elif choice == "4":
            try:
                # Ask revenue per task type
                rev_a = float(input("Enter revenue per Task A: "))
                rev_b = float(input("Enter revenue per Task B: "))
                rev_c = float(input("Enter revenue per Task C: "))

                rates = {"A": rev_a, "B": rev_b, "C": rev_c}

                if historic_df.empty:
                    print("No data available.")
                else:
                    # Add revenue column based on task type
                    historic_df["Revenue"] = historic_df.apply(lambda row: row["Tasks Completed"] * rates.get(row["Task"], 0), axis=1)

                    revenue_summary = historic_df.groupby("Worker")["Revenue"].sum().reset_index()
                    print("Estimated revenue per worker:")
                    print(revenue_summary)
            except:
                print("Error: Please enter valid numbers.")


        elif choice == "5":
            print("Exiting departmental manager menu.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
    


#Create a log in function
def login():
    while True:
        print("\nLogin to the System")
        
        # Ask for login details
        username = input("Enter your username: ").strip()
        password = input("Enter yout password: ").strip()

        # Check against list of saved managers
        for manager in managers:
            if manager["username"] == username and manager["password"] == password:
                print("\nLogin successful.") # If details match
                print("Welcome,", manager["first_name"], manager ["surname"])
                return manager # return full manager dctionary

        print("Invalid login. Please try again.\n")
        


#Main Program
while True:
    user = login() # Call the login function

    if user:
        role = user["role"] # Get the role of the user

        # Route the user to the correct menu based on their role
        if role == "Admin":
            print("\n You are logged in as a Junior Sysytem Administrator.")
            admin_menu(user)
            break

        elif user["role"] == "Manager":
            print("You are logged in as a Task Manager for Task", user["task"])
            manager_menu(user)
            break

        elif user["role"] == "DepartmentManager":
            print("You are logged in as the Departmental Manager.")
            department_menu(user)
            break

        else:
            print("Unknown role. Exiting the program")
    
