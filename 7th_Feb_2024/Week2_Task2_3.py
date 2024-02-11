# Develop a Python script that calculates the square and cube of a given number.
def calculate_square_and_cube(num):
    # Calculating the square and cube
    square = num ** 2
    cube = num ** 3
    return square, cube


num = float(input("Enter a number: "))

# Calculating square and cube using the function
square_result, cube_result = calculate_square_and_cube(num)

# Printing the results
print(f"The square of {num} is: {square_result}")
print(f"The cube of {num} is: {cube_result}")
