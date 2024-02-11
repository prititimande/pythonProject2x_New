def classify_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
    else:
        return "Scalene"

# Taking the side lengths as input from the user
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Classifying the triangle based on side lengths and printing the result
classification = classify_triangle(side1, side2, side3)
print(f"The triangle is classified as: {classification}")
