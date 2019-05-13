#!/usr/bin/env python3.7

# https://docs.python.org/3/library/index.html

# BMI = (weight in kg / height in meters squared)
# Imperial version: BMI * 703  (using pounds and inches)

def gather_info():
    height = float(input("What is your height? (inches or meters)"))
    weight = float(input("What is your weight? (pounds or kilograms)"))
    system = input("Are your measurements in metric or imperial units? ").lower().strip()

    #Return tuple
    return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    """
    Return the body mass index (BMI) for the given inputs.
    """

    if system == 'metric':
        bmi = (weight /(height ** 2))
    else:
        bmi = 703 * (weight /(height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(weight, system=system, height=height)
        print(f"Your BMI is {bmi}")
        print(f"Your BMI as an integer is {bmi // 1}")
        break
    elif system.startswith('m'):
        bmi = calculate_nmi(weight, height)
        print(f"Your BMI is {bmi}")
        print(f"Your BMI as an integer is {bmi // 1}")
        break
    else:
        print("Error: Unknown measurement system.  Please use imperial or metric.")
