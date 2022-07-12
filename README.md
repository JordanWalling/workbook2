# Workbook 2
---


[Github Repository](https://github.com/JordanWalling/workbook2)

## Project Title 
---
The project will be called The Health App. The Health App was created for fitness enthusiasts and the general population. 

## The Health App Features
---

To start the app, the user enters "python3 main.py" into the terminal. The app will start and the user will be presented with a welcome message and four options. These four options are:
1. BMI
2. Weight Converter 
3. Calories Needed
4. Stopwatch 

The user will have to enter "1", "2", "3" or "4" depending on what option the user is interested in. If the numbers 1,2,3 or 4 are NOT entered, the question will be repeated until one of the four numbers are entered. 

### #1 - BMI
---

When #1 - BMI is selected, a message will appear informing the user that they have selected the Body Mass Index (BMI) Calculator. The user will need to input their height in metres (for example 178cm = 1.78m) and also input their weight in kilograms (kg). If weight in kilograms is unknown, please see The Weight Converter feature. Once the weight and height has been entered, the calculator will present the BMI. Depending on the BMI results, the calculator will also present whether based on the results, the user is Underweight, in the Healthy range, Overweight or Obese. On completion, the app will close. If anything other than a numerical value is entered, the questions will be repeated until a number has been entered.

## #2 - Weight Converter 
---
By selecting "2" as an option on the main.py page, the user is taken to the "Weight Converter" section. Here the user is given 2 options on what they would like to convert: 
1. Pounds to Kilograms
2. Kilograms to Pounds

Selecting "1" will convert the users pounds to kilograms and selecting "2" will convert kilograms to pounds. This will be useful if the user doesn't know their weight in kilograms for the BMI calculator. Once their weight is entered, their weight will be converted and presented and the app will close. The inputs will loop until a proper answer is given in numerical value. 

## #3 - Calories Needed
---

Depending on the users needs, they might want to either Lose, Maintain or Gain weight. The Calories needed section assists with that. To locate to the Calories Needed section the user will need to select "3" on the main.py page. The user will then be requested to enter their weight in pounds. Once entered, the user will then be asked "what is your goal?" and presented with 3 options:
1. Maintain current weight 
2. Lose weight 
3. Gain weight 

Judging by what the user input whether its "1" to Maintain current weight, "2" to Lose weight or "3" to Gain weight, the weight calculator will present the required calories needed for their goals. If an answer besides "1" "2" or "3" is given, the question will be repeated until given "1" "2" or "3". The app will then close. 

## #4 - Stopwatch
---

The last feature presented on the Health App is the Stopwatch. This can be accessed by entering the option "4" on the main.py page. Once "4" is entered, the user will be prompted "To start the stopwatch, please press 'Enter/Return':". The stopwatch will not start unless the 'Enter' button is pressed. The stopwatch will start and will not stop until the 'Enter' button is pressed again. The time will then be presented as:
"Time spent: 0h: 0m: 0s"
This feature is great so that the user can time how long it takes to perform an exercise, such as running a certain distance. At completion, the app will close. 

## Help Documentation
---

Steps to download the program:
1. Click on the Github repository located at the start of this README file. 
2. Click on the "Code" dropdown button. 
3. Copy the URL under the "Clone" section and copy the HTTPS link. 
4. Open Terminal. 
5. Change the current working directory to the location where you would like to clone the repository. 
6. Type "git clone" followed by the HTTPS link copied in step 3. 
7. Press Enter to create clone. 

To run the program in the terminal:
1. Locate the folder that the program is saved inside. Enter "ls" and find "main.py" to make sure you are in the right location. The python files "bmi", "weight_converter", "calorie_needs", "stopwatch" and "welcome_message" should be located in the same folder. 
2. To start the program, enter "python3 main.py". Typing "python3 main.py" will run the program each time. 

## System/Hardware Requirements
---
The Terminal:
The Terminal is required so that the Health App program can be run.
Install python:
To run the Health App program, python needs to be installed from inside the terminal. For assistance on how to download python on the terminal, go to [Real Python](https://realpython.com/installing-python/). 

## Implementation Plan
--- 

![Overview of Health App](./screenshots/Screen%20Shot%202022-07-12%20at%204.30.43%20pm.png)

![Main Page](./screenshots/Screen%20Shot%202022-07-12%20at%204.31.48%20pm.png)

![Stopwatch](./screenshots/Screen%20Shot%202022-07-12%20at%204.32.28%20pm.png)

![Weight Converter](./screenshots/Screen%20Shot%202022-07-12%20at%204.32.59%20pm.png)

![Calories Needed](./screenshots/Screen%20Shot%202022-07-12%20at%204.33.56%20pm.png)

![BMI](./screenshots/Screen%20Shot%202022-07-12%20at%204.34.18%20pm.png)

![Welcome Message](./screenshots/Screen%20Shot%202022-07-12%20at%204.34.49%20pm.png)