def convert_weight():
    prompt = False
    
    print("What would you like to convert? \n1. Pounds to Kilograms \n2. Kilograms")
    prompt = input("Please answer either '1' or '2'")
    if prompt == "1":
        num = input("Please enter your weight in Pounds: ")
        print(f'This is your weight in kilograms: {num*0.45359237} ')

    elif prompt == "2":
        num = input("Please enter your weight in Kilograms: ")
        print(f"This is your weight in Pounds: {num*2.2} ")

    else: 
        print("Invalid option, please enter '1' or '2'")