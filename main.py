print('Welcome to the Health App!')
print('Please select an option: ')
prompt = input('1.BMI \n2.Weight Converter \n3.Calories needed \n')

if prompt == "1":
    print("BMI")
elif prompt == "2":
    print("Weight Converter")
elif prompt == "3":
    print("Calories needed")
else:
    print("Invalid input")