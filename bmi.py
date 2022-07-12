def calculate_bmi():
    height = False
    weight = False
    print("To calculate your Body Mass Index or BMI, your height and weight is needed")
    while height == False:
        height = float(input("Please enter your height in metres: "))
    while weight == False:
        weight = float(input("Please enter your weight in kilograms: "))
    bmi = weight/height**2
    print(f"Your BMI is: {round(bmi,2)}")

    if bmi <18.50:
        print("You are Underweight")
    elif bmi >=18.50 and bmi <= 24.99:
        print("You are in the health range bracket!")
    elif bmi >= 25.00 and bmi <= 29.99:
        print("According to your BMI, you are Overweight.")
    else:
        print("According to the BMI, You are Obese.")