# Task #2
# Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2 ( Take pie as 3.14)
import math

def calculate_circle_area(radius):
    # Using the formula: area = π × r^2
    area = math.pi * (radius ** 2)
    return area

# Taking the radius as input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculating the area and printing the result
area_of_circle = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area_of_circle:.2f}")


