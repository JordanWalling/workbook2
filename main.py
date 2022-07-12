import time
from bmi import calculate_bmi
from stopwatch import print_start_time
from calorie_needs import calculate_calorie_needs
from weight_converter import convert_weight
from welcome_message import greet_message


greet_message()
print('Welcome to the Health App!')

print('Please select an option: "1", "2", "3" or "4" ')
prompt = input('1.BMI \n2.Weight Converter \n3.Calories Needed \n4.Stopwatch\n')
while prompt != "1" or prompt != "2" or prompt != "3" or prompt != "4":
    if prompt == "1":
        calculate_bmi()
    elif prompt == "2":
        convert_weight()
    elif prompt == "3":
        calculate_calorie_needs()
    elif prompt == "4":
        input("To start the stopwatch, please press 'Enter/ Return': ")
        start_time = time.time()

        print('Time is running....')
                
        input('To stop the stopwatch, please press "Return/ Enter": ')
        stop_time = time.time()
        print_start_time(stop_time - start_time)
    else:
        print("Invalid input")