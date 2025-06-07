# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Access the dataset from Power BI
# Load the dataset (replace with your actual data source)
# Example: Load from a CSV file
dataset = pd.read_csv("stuff.csv")
df = dataset

# Data manipulation using pandas
# Example: Grouping data by a column and summing another column
grouped_data = df.groupby("Category")["Sales"].sum().reset_index()

# Plotting the data using matplotlib
plt.figure(figsize=(10, 6))
plt.bar(grouped_data["Category"], grouped_data["Sales"], color="skyblue")
plt.title("Sales by Category", fontsize=16)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()
