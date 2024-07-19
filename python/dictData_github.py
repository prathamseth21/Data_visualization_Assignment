from tabulate import tabulate
students_dict = {
    'std01': {'studentName': 'Ashish Kumar', 'Standard': '10th', 'Age': 15, 'Hindi': 67, 'English': 89, 'Maths': 87, 'Science': 89, 'Computer': 90, 'Total': 422},
    'std02': {'studentName': 'Abhishek Kumar', 'Standard': '10th', 'Age': 14, 'Hindi': 85, 'English': 45, 'Maths': 48, 'Science': 90, 'Computer': 45, 'Total': 313},
    'std03': {'studentName': 'Aman', 'Standard': '10th', 'Age': 15, 'Hindi': 23, 'English': 56, 'Maths': 78, 'Science': 78, 'Computer': 67, 'Total': 302},
    'std04': {'studentName': 'Rahul', 'Standard': '10th', 'Age': 14, 'Hindi': 45, 'English': 67, 'Maths': 45, 'Science': 45, 'Computer': 56, 'Total': 258},
    'std05': {'studentName': 'Ruby', 'Standard': '10th', 'Age': 13, 'Hindi': 89, 'English': 67, 'Maths': 89, 'Science': 93, 'Computer': 65, 'Total': 403},
    'std06': {'studentName': 'Suman', 'Standard': '10th', 'Age': 13, 'Hindi': 90, 'English': 46, 'Maths': 67, 'Science': 67, 'Computer': 67, 'Total': 337},
    'std07': {'studentName': 'Saurabh', 'Standard': '10th', 'Age': 15, 'Hindi': 45, 'English': 23, 'Maths': 34, 'Science': 45, 'Computer': 34, 'Total': 181},
    'std08': {'studentName': 'Sumit', 'Standard': '10th', 'Age': 14, 'Hindi': 23, 'English': 45, 'Maths': 67, 'Science': 78, 'Computer': 90, 'Total': 303},
    'std09': {'studentName': 'Kamlesh', 'Standard': '10th', 'Age': 15, 'Hindi': 45, 'English': 56, 'Maths': 78, 'Science': 99, 'Computer': 67, 'Total': 345},
    'std10': {'studentName': 'Rohan', 'Standard': '10th', 'Age': 15, 'Hindi': 34, 'English': 12, 'Maths': 24, 'Science': 45, 'Computer': 56, 'Total': 171}
}

headers = ['stdId']+list(students_dict['std01'].keys())
data = [[stdId] + list(details.values()) for stdId, details in students_dict.items()]

print(tabulate(data, headers = headers, tablefmt ='pretty'))

               
# Extract student details and sort by Maths score
top_math_scorers = sorted(students_dict.values(), key=lambda x: x['Maths'], reverse=True)[:4]

# Prepare data for tabulate
headers = ["studentName", "Age"]
rows = [[student['studentName'], student['Age']] for student in top_math_scorers]

# Display table
print(tabulate(rows, headers=headers, tablefmt="grid"))
# Sort students by Computer score in ascending order
bottom_computer_scorers = sorted(students_dict.values(), key=lambda x: x['Computer'])[:3]

# Prepare data for tabulate
headers = ["stdId", "studentName", "Age"]
rows = [[stdId, student['studentName'], student['Age']] for stdId, student in students_dict.items() if student in bottom_computer_scorers]

# Display table
print(tabulate(rows, headers=headers, tablefmt="grid"))
