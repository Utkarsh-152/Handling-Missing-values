import pandas as pd
import numpy as np

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
        data[column].fillna(np.random.choice(data[column].dropna()), inplace=True)
elif choice == 5:
    # Assign missing values as a string "Missing"
    data.fillna("Missing", inplace=True)
elif choice == 6:
    data.dropna(inplace=True)
else:
    print("Invalid choice.")

print("Missing values handled. Updated data:")


print("The distortion is:")
for column in selected_columns:
    plt.figure(figsize=(8, 6))
    plt.hist(data[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
