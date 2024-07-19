from tabulate import tabulate
import pandas as pd
# stuData = [["stdId", 'stdName', "standard", 'age', 'hindi','english','math','science','computer','total'],
#            ['std101','Ashish Kumar', '10th', 15, 67,89,87,89,90,422],
#            ['std102','Abhishek Kumar', '10th', 14,85,45,48,90,45,313],
#            ['std103','Aman', '10th', 15,23,56,78,78,67,302],
#            ['std104','Rhul', '10th', 14,45,67,45,45,56,258],
#            ['std105','Ruby', '10th', 13,89,67,89,93,65,403],
#            ['std106','Suman', '10th', 13,90,46,67,67,67,337],
#            ['std107','Saurabh', '10th', 15,45,23,34,45,34,181],
#            ['std108','Sumit', '10th', 14,23,45,67,78,90,303],
#            ['std109','Kamlesh', '10th', 15,45,56,78,99,67,345],
#            ['std110','Rohan', '10th', 15,34,12,24,45,56,171],
#         ]

record1 = ["stdId", 'stdName', "standard", 'age', 'hindi','english','math','science','computer','total']
record2 = ['std101','Ashish Kumar', '10th', 15, 67,89,87,89,90,422]
record3 = ['std102','Abhishek Kumar', '10th', 14,85,45,48,90,45,313]
record4 = ['std103','Aman', '10th', 15,23,56,78,78,67,302]
record5 = ['std104','Rahul', '10th', 14,45,67,45,45,56,258]
record6 = ['std105','Ruby', '10th', 13,89,67,89,93,65,403]
record7 = ['std106','Suman', '10th', 13,90,46,67,67,67,337]
record8 = ['std107','Saurabh', '10th', 15,45,23,34,45,34,181]
record9 = ['std108','Sumit', '10th', 14,23,45,67,78,90,303]
record10 = ['std109','Kamlesh', '10th', 15,45,56,78,99,67,345]
record11= ['std110','Rohan', '10th', 15,34,12,24,45,56,171]

stuData = [record1, record2, record3, record4, record5, record6, record7, record8, record9,record10, record11]
        

# for row in range(len(stuData)) :
#     print(stuData[row])

headers = stuData[0]
data = stuData[1 : ]

print(tabulate(data, headers = headers, tablefmt ='pretty'))

# print(pd.DataFrame(data, columns = headers))


                                                  #question : 1
# print("Name of students whose marks in english is greater than 60")

# for record in range(1,len(stuData)):
#     if(stuData[record][5] > 60):
#         print(stuData[record][1])

# EngData = [(record[1], record[5]) for record in stuData]

# header1 = EngData[0]
# data1 = EngData[1:]

# print(tabulate(data1, headers = header1, tablefmt ='pretty'))

# for record in range(1,len(EngData)):
#     if(EngData[record][1] > 60):
#         print(EngData[record][0])


                                                 #question : 2
# print("display students name and age of top four scorer of maths ")

# students = [(record[1], record[3], record[6]) for record in stuData]

# header2 = students[0]

# students = sorted(students[1:], key = lambda x : x[2], reverse = True)

# print(tabulate(students, headers = header2, tablefmt = 'pretty'))

# for student in students[:4]:
#     print(f"Name : {student[0]}, Age: {student[1]}")



                                               #question : 3
# print("display name , id and age of students who are bottom three scorer in computer : ")

# students = [(record[0], record[1], record[3], record[8]) for record in stuData]

# header3 = students[0]

# print(tabulate(students[1:], headers = header3, tablefmt ='pretty'))

# students = sorted(students[1:], key = lambda x : x[3])

# print(tabulate(students, headers = header3, tablefmt ='pretty'))

# for student in students[:3] :
#     print(f"ID : {student[0]}, Name : {student[1]}, Age : {student[2]}")








