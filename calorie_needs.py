def calculate_calorie_needs():
    print("Welcome to your preferred weight calculator!")
    prompt = False
    while prompt == False or not prompt.isnumeric():
        prompt = input("Please type your weight in Pounds: \n")
        if not prompt.isnumeric():
            print("Please enter a number")
    prompt = int(prompt)
    goal = False
    while goal == False or (goal !="1" and goal !="2" and goal !="3"):
        goal = input("What is your goal? \n1.Maintain current weight \n2.Lose weight \n3.Gain weight \n")
        total_calories = prompt*15

        if goal == "1":
            print(f"Your calories to maintain weight is {total_calories}")
        elif goal == "2":
            lose_weight = total_calories - 500
            print(f"Your calories needed to lose weight: {lose_weight}")
        elif goal == "3":
            gain_weight = total_calories + 500
            print(f"Your calories needed to gain weight: {gain_weight}")
        else:
            print("Invalid input, please enter '1', '2' or '3' ")