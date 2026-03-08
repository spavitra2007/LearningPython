
file_path = "students.csv"

print("--- Full File Content ---")
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

print("\n--- Detailed Student Data ---")
# Re-opening or seeking to start to process lines
with open(file_path, "r", encoding="utf-8") as file:
    header = next(file).strip().split(",")
    print(f"Header row: {header}")
    
    student_count = 0
    for line in file:
        line = line.strip()
        if not line:
            continue
            
        student_count += 1
        columns = line.split(",")
        
        print(f"\nStudent {student_count}:")
        print(f"    Name       = {columns[0]}")
        print(f"    Age        = {columns[1]}")
        print(f"    Department = {columns[2]}")
        print(f"    Score      = {columns[3]}")
        
        # Safety check: handle rows with missing data
        if len(columns) > 4:
            print(f"    Attendance = {columns[4]}")
        else:
            print("    Attendance = [Missing Data]")

# Checking if students already exist (by name) before appending
with open("students.csv", "a+", encoding="utf-8") as file:
    file.seek(0)
    existing_data = file.read()
    
    # Check if Name already exists in the file
    if "Henry," not in existing_data:
        file.write("Henry,23,Maths,81,95\n")
        print("Added new data for Henry.")
    else:
        print("Henry already exists in the file.")
    
    if "Sophia," not in existing_data:
        file.write("Sophia,22,Arts,76,88\n")
        print("Added new data for Sophia.")
    else:
        print("Sophia already exists in the file.")


with open("students.csv", "r", encoding="utf-8") as file:
    updated_content = file.read()

print("\n--- Updated students.csv Content ---")
print(updated_content)
import pandas as pd

# Read the CSV file you created in Notepad
df = pd.read_csv("students.csv")

print("\n  📊 Pandas Table View:")
print(df)

print(f"\n  Total Students : {len(df)}")
print(f"  Average Score  : {df['Score'].mean():.1f}")
print(f"  Highest Score  : {df['Score'].max()}")
print(f"  Lowest Score   : {df['Score'].min()}")

# Add a new column
df["Status"] = df["Score"].apply(lambda s: "PASS" if s >= 40 else "FAIL")
df.to_csv("students_final.csv", index=False)
final = pd.read_csv("students_final.csv")
print(final)
df.to_excel("students_final.xlsx", index=False)
print("\nExcel file 'students_final.xlsx' has been created.")


import os
os.startfile("students_final.xlsx")



