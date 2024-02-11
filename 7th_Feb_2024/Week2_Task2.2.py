# Create a program that takes two numbers as input and prints whether the first number is greater than, less than,
# or equal to the second number.

a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))

if a > b:
    print("A is Greater than B")
elif a < b:
    print (f"A is less than B")
else:
    print(f"A and B are equal")


