num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))
num3 = int(input("Enter your third number:"))
print("First number:",num1)
print("Second number:",num2)
print("Third number:",num3)

if num1 >= num2 and num1 >= num3:
    largest_number=num1
elif num2 >= num1 and num2 >= num3:
     largest_number=num2
elif num3 >= num1 and num3 >= num2:
     largest_number=num3
     
print("Largest number:",largest_number)
