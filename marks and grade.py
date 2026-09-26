name=input("Enter student name:")
marks=int(input("Enter your marks:"))

if marks>=75:
    grade="A"
elif marks>=65:
    grade="B"
elif marks>=50:
    grade="C"
else:
    grade="F"
    
    
print("student name:",name)
print("Marks:",marks)
print("Grade:",grade)

