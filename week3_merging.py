import pandas as pd

# First dataset
students = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Name": ["Ravi", "Priya", "Rahul"]
})

# Second dataset
marks = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Marks": [85, 92, 78]
})

# Merge both datasets using Student_ID
merged_data = pd.merge(students, marks, on="Student_ID")

# Display the merged dataset
print("MERGED DATASET:")
print(merged_data)