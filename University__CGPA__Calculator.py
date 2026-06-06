# CGPA Calculator

total_credit_units = 0
total_quality_points = 0

num_courses = int(input("How many courses do want to enter? "))
for i in range(num_courses):
    print("\nCourse" , i + 1)

    credit_units = int(input("Enter credit unit: "))
    grade = input("Enter grade (A, B, C, D, E, F): ").upper()
    if grade == "A":
        grade_point = 5
    elif grade == "B":
        grade_point = 4
    elif grade == "C":
        grade_point = 3
    elif grade == "D":
        grade_point = 2
    elif grade == "E":
        grade_point = 1
    else:
        grade_point = 0
        
    quality_points = credit_units * grade_point

    total_credit_units += credit_units
    total_quality_points += quality_points
# Avoid division error
if total_credit_units != 0:
    cgpa = total_quality_points / total_credit_units
    print("\nYour CGPA is:", round(cgpa, 2))
else:
    print("no course entered. ") 

