def convert_weight():
    prompt = input("What would you like to convert? \n1. Pounds to Kilograms \n2. Kilograms")

    if prompt == "1":
        num = input("Please enter your weight in Pounds: ")
        print('This is your weight in kilograms: ')

    elif prompt == "2":
        num = input("Please enter your weight in Kilograms: ")
        print("This is your weight in Pounds: ")