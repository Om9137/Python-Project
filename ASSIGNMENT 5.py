'''Task 1: Create a Dictionary of Student Marks'''
# Create a dictionary with student names as keys and their marks as values

student_marks = {
    "Amit": 89,
    "Priya": 76,
    "Rahul": 92,
    "Sneha": 85,
    "Vikram": 81
}

# Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Retrieve and display the corresponding marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
         
else:
    print(f"Sorry, no records found for {student_name}.")




'''Task 2: Demonstrate List Slicing '''
# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extract the first five elements
extracted_list = numbers[:5]

# Step 3: Reverse the extracted elements
reversed_list = extracted_list[::-1]

# Step 4: Print both lists
print("Original list", numbers)
print("Extracted 1st five list:", extracted_list)
print("Reversed Extracted list:", reversed_list)
