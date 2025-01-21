import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# Read data from CSV file
file_path = input("Enter the file path: ")
data = pd.read_csv(file_path)

# Display columns to the user for selection
print("Available columns:")
print(data.columns)
selected_columns = input("Enter column names separated by commas: ").split(',')

# Select only the columns entered by the user
data = data[selected_columns]

print("The missing values in the selected columns are:")
print(data.isnull().sum())

# Prompt user for the method to fill missing values
print("\nChoose how you want to fill your null values:")
print("1: Mean")
print("2: Mode")
print("3: Median")
print("4: Random")
print("5: Assign it as Missing")
print("6: Delete them")
print("7: Grouped Fill")
print("8: K-Nearest Neighbors (KNN)")
print("9: Multiple Imputation by Chained Equations (MICE)")

choice = int(input("Enter your choice: "))

# Handle missing values based on user choice
if choice == 1:
    data.fillna(data.mean(), inplace=True)
elif choice == 2:
    data.fillna(data.mode().iloc[0], inplace=True)
elif choice == 3:
    data.fillna(data.median(), inplace=True)
elif choice == 4:
    for column in data.columns:
        if data[column].dtype in ['float64', 'int64']:  # Random choice for numeric data
            data[column].fillna(np.random.choice(data[column].dropna()), inplace=True)
        else:  # Random choice for categorical data
            data[column].fillna(np.random.choice(data[column].dropna()), inplace=True)
elif choice == 5:
    # Assign missing values as a string "Missing"
    data.fillna("Missing", inplace=True)
elif choice == 6:
    data.dropna(inplace=True)
elif choice == 7:
    group_by_column = input("Enter the column name to group by: ")
    if group_by_column in data.columns:
        for column in data.columns:
            data[column] = data[column].fillna(data.groupby(group_by_column)[column].transform('mean'))
    else:
        print(f"Column {group_by_column} not found.")
elif choice == 8:
    imputer = KNNImputer(n_neighbors=5)
    data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
elif choice == 9:
    imputer = IterativeImputer(max_iter=10, random_state=0)
    data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
else:
    print("Invalid choice.")

print("Missing values handled. Updated data:")
print(data.head())
