from bmi import calculate_bmi
from welcome_message import greet_message
from stopwatch import print_time

greet_message()
print('Welcome to the Health App!')
print('Please select an option: ')
prompt = input('1.BMI \n2.Weight Converter \n3.Calories needed \n4.Stopwatch')

if prompt == "1":
    calculate_bmi()
elif prompt == "2":
    print("Weight Converter")
elif prompt == "3":
    print("Calories needed")
elif prompt == "4":
    print_time()
else:
    print("Invalid input")