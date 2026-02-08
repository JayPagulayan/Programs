print("--- Fill up Form ---\n")

name = input("What is your name? ")
age = int(input("How old are you? "))
gender = input("What is your gender? ")
month_birth = input("In what month were you born? ")
year_birth = int(input("In what year were you born? "))
day_birth = input("On what day of the month were you born? ")
nationality = input("What is your nationality? ")
address = input("What is your current address? ")
place_birth = input("Where were you born? ")
height = int(input("What is your height in cm? "))
weight = int(input("What is your weight in kg? "))
contact_number = input("What is your contact number? ")
religion = input("What is your religion? ")
mothers_name = input("What is your mother's name? ")
fathers_name = input("What is your father's name? ")
college = input("Which college or university do you attend? ")
program = input("What program or course are you taking? ")

if year_birth >= 2010:
    gen = "Gen Alpha"
elif year_birth >= 1997:
    gen = "Gen Z"
elif year_birth >= 1981:
    gen = "Millennial"
else:
    gen = "Gen X or older"

height_m = height / 100
bmi = weight / (height_m ** 2)
if bmi < 18.5:
    health = "underweight"
elif 18.5 <= bmi <= 24.9:
    health = "at a healthy weight"
else:
    health = "overweight"


if age < 18:
    stage = "a minor"
elif age < 60:
    stage = "a legal adult"
else:
    stage = "a senior citizen"
print("\n------------------------")
print(f"My name is {name}. I am a {age}-year-old {gender} from {place_birth}, and I currently live at {address}.")
print(f"As a member of {gen}, I was born on {month_birth} {day_birth}, {year_birth}.")
print(f"I hold {nationality} citizenship, practice {religion}, and I am considered {stage} under the law.")
print(f"I stand {height}cm tall and weigh {weight}kg. Based on my BMI of {bmi:.1f}, I am {health}.")
print(f"I am the child of {fathers_name} and {mothers_name}, and I can be reached at {contact_number}.")
print(f"Currently, I am pursuing my studies in {program} at {college}.")