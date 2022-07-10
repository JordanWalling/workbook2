from bmi import calculate_bmi
from weight_converter import convert_weight
from welcome_message import greet_message
from stopwatch import print_time

greet_message()
print('Welcome to the Health App!')
print('Please select an option: "1", "2", "3" or "4" ')
prompt = input('1.BMI \n2.Weight Converter \n3.Calories Needed \n4.Stopwatch\n')

if prompt == "1":
    calculate_bmi()
elif prompt == "2":
    convert_weight()
elif prompt == "3":
    print("Calories needed")
elif prompt == "4":
    print_time()
else:
    print("Invalid input")