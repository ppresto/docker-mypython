#!/usr/bin/env python3.7

def hello_world():  #start function with lowercase or _.  Use _ between words.
    print("Hello, World!")
hello_world()

def print_name(name):
    print (f"Name is {name}")
output = print_name("Jessica")  # output gets no value.  functions dont return a value by default.

def add(num1,num2):
    return num1+num2
result = add(4,4)
print (result)

def contact_card(name, age, car_model):
    print (f"{name} is {age} and drives a {car_model}")
    return f"{name} is {age} and drives a {car_model}"

contact_card("patrick",42,"Prius")
contact_card(age=6, car_model='Toy', name='liam')
contact_card("Lucas", car_model="bike", age=6)

def can_drive(age, driving_age=16):
    return age >= driving_age

print(can_drive(15))
print(can_drive(15,14))
