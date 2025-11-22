# Program to calculate average marks of 5 subjects and grade

# Accept marks from the user
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculate average
average = sum(marks) / len(marks)

# Determine grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

# Print results
print("\n--- Result ---")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
