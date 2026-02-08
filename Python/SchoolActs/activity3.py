def BMIcal(height,weight):
    bmi = weight / ((height/100) ** 2)
    return bmi

def grades(mathgrade,englishgrade,sciencegrade):
    avegrade= (mathgrade + englishgrade + sciencegrade )/3
    return avegrade

def healthcal(BMI):
    if BMI < 18.5:
        health = "underweight"
    elif 18.5 <= BMI <= 24.9:
        health = "a healthy weight"
    else:
        health = "overweight"
    return health

def age(year_birth):
    currentyear= 2026
    currentage=currentyear-year_birth
    return currentage


print("--- Fill up Form ---\n")

def biodata():
    name = input("What is your name? ")
    gender = input("What is your gender? ")
    month_birth = input("In what month were you born? ")
    year_birth = int(input("In what year were you born? "))
    day_birth = input("On what day of the month were you born? ")
    address = input("What is your current address? ")
    height = int(input("What is your height in cm? "))
    weight = int(input("What is your weight in kg? "))
    contact_number = input("What is your contact number? ")
    religion = input("What is your religion? ")
    college = input("Which college or university do you attend? ")
    program = input("What program or course are you taking? ")
    mathgrade= float(input("Math Grade :"))
    englishgrade= float(input("English Grade :"))
    sciencegrade= float(input("Science Grade :"))
    avegrade =grades(mathgrade,englishgrade,sciencegrade)
    BMI= BMIcal(height,weight)
    health= healthcal(BMI)
    YearOld= age(year_birth)
    print("\n===============Essay==============\n")
    print(f"My name is {name}. I will be {YearOld}-year-old this year 2026.")
    print(f"I was born on {month_birth} {day_birth}, {year_birth}.")
    print(f"My gender is {gender}, and I currently live at {address}.I practice {religion}.")
    print(f"I stand {height}cm tall and weigh {weight}kg. Based on my BMI of {BMI}, I am {health}.")
    print(f"I can be reached at {contact_number}.Currently My average grade in 3 major subjects are {avegrade}%")
    print(f"Currently, I am pursuing my studies in {program} at {college}.")
    print("\n================End===============\n")

biodata()

