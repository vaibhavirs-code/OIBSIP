## BMI Calculator
try:
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in meters): "))
    if weight <= 0 or height <= 0:
        print("Please enter valid values of weight and height.")

    else:
        bmi = weight / (height * height)
        print("\nYour BMI is:", round(bmi, 2))
        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

except ValueError:
    print("Invalid input! Please enter numbers only.")