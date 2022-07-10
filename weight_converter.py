def convert_weight():
    prompt = False
    while prompt == False or (prompt != "1" and prompt != "2"):
        print("What would you like to convert? \n1. Pounds to Kilograms \n2. Kilograms")
        prompt = input("Please answer either '1' or '2'")
        if prompt == "1":
            num = float(input("Please enter your weight in Pounds: "))
            print(f'This is your weight in kilograms: {round(num*0.45359237,2)} ')

        elif prompt == "2":
            num = float(input("Please enter your weight in Kilograms: "))
            print(f"This is your weight in Pounds: {round(num*2.2,2)} ")

        else: 
            print("Invalid option, please enter '1' or '2'")