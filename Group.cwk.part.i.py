import pandas as pd

# Name Mapping, Convert names into 1 format

name_mapping = {
    "Anthony": "Thomas Anthony",
    "Chua": "Wen Chua",
    "Goh": "Chengze Goh",
    "Suthar": "Pratik Suthar",
    "Grover": "Francis Grover",
    "Alvarez": "Chris Alvarez",
    "Thomas": "Thomas Anthony",
    "Partik": "Pratik Suthar",
    "Chengze": "Chengze Goh",
    "Chris": "Chris Alvarez",
    "Wen": "Wen Chua",
    "Francis": "Francis Grover",
    "Pratik": "Pratik Suthar"
}


# --------------------------- Task A -----------------------------------------------------------------------------

df_a = pd.read_csv("TaskA.csv") # Load CSV

df_a["Worker"] = df_a["Worker"].map(name_mapping) # Standardise worker names
df_a["Tasks Completed"] = df_a["Tasks Completed"].fillna(0).astype(int) # Replace missing values with an integer 0
# Add columns for task type and manager name for future tasks
df_a["Task"] = "A"
df_a["Manager"] = "Sarah Smith"

# Standardize date
df_a["Date"] = pd.to_datetime(df_a["Date"], format="%b-%y")
df_a["Date"] = df_a["Date"].dt.strftime("%Y-%m")

# Order columns to match final structure
df_a = df_a[["Date", "Worker", "Task", "Manager", "Tasks Completed"]]



#----------------------------- Task B ------------------------------------------------------------------------------

df_b = pd.read_csv("TaskB.csv") # Load CSV for Task B
df_b["Unnamed: 0"] = df_b["Unnamed: 0"].ffill() # Fill in missing dates by cipying doen previous date
df_b.columns = ["Date", "Worker", "Tasks Completed"] # Rename columns for clarity
df_b["Worker"] = df_b["Worker"].map(name_mapping) # Standardise names
df_b["Tasks Completed"] = df_b["Tasks Completed"].fillna(0).astype(int) # Fill missing values with an integer 0
# Add task and manager information
df_b["Task"] = "B"
df_b["Manager"] = "Akshay Shah"

# Standardize date
df_b["Date"] = pd.to_datetime(df_b["Date"], format="%b-%y")
df_b["Date"] = df_b["Date"].dt.strftime("%Y-%m")

# Rename columns
df_b = df_b[["Date", "Worker", "Task", "Manager", "Tasks Completed"]]

#---------------------------- Task C ------------------------------------------------------------------------------

df_c = pd.read_csv("TaskC.csv")# Load Task C CSV
df_c = df_c.melt(id_vars=["Unnamed: 0"], var_name="Worker", value_name="Tasks Completed")# Convert wide format (months as rows, workers as columns) to long format
df_c.rename(columns={"Unnamed: 0": "Date"}, inplace=True) # Rename columns
df_c["Worker"] = df_c["Worker"].map(name_mapping) # Standardize worker names
df_c["Tasks Completed"] = df_c["Tasks Completed"].fillna(0).astype(int) # Fill missing values and convert to integer 0
# Add Task and Manager
df_c["Task"] = "C"
df_c["Manager"] = "Huhan Yang"

# Standardize date format
df_c["Date"] = pd.to_datetime(df_c["Date"], format="%b-%y")
df_c["Date"] = df_c["Date"].dt.strftime("%Y-%m")

# Reorder columns
df_c = df_c[["Date", "Worker", "Task", "Manager", "Tasks Completed"]]


#----------------------------------------------------------------------------------------------------------------

# Combine all tasks into a single DataFrame
historic_df = pd.concat([df_a, df_b, df_c], ignore_index=True)

# Save as a pickle file to be used in later task
historic_df.to_pickle("historic_df.pkl")

print(historic_df.head())





                        
