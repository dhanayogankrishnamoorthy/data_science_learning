fibonacci = int(input("How many Fibonacci numbers do you want? "))
a = 0
b = 1
for i in range(fibonacci):
    print(a)
    c = a + b
    a = b
    b = c
