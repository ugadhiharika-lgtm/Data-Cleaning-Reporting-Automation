import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Employee_ID": [101, 102, 103, 103, 104, None],
    "Name": ["John", "Alice", "Bob", "Bob", "David", "Emma"],
    "Salary": [50000, 60000, None, None, 55000, 70000],
    "Department": ["HR", "IT", "IT", "IT", "Finance", None]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values
df["Employee_ID"] = df["Employee_ID"].fillna(0)
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Department"] = df["Department"].fillna("Unknown")

print("\nCleaned Data:")
print(df)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

# Generate summary report
summary = df.describe(include="all")
summary.to_csv("summary_report.csv")

# Visualization
df["Department"].value_counts().plot(kind="bar")

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("department_chart.png")

print("\nAutomation Completed Successfully!")
print("Files Generated:")
print("1. cleaned_data.csv")
print("2. summary_report.csv")
print("3. department_chart.png")
