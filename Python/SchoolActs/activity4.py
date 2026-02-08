def calculate_bmi(height_cm, weight_kg):
    bmi = weight_kg / ((height_cm / 100) ** 2)
    return bmi

def determine_health_status(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi <= 24.9:
        return "a healthy weight"
    else:
        return "overweight"

def calculate_average(m, e, s):
    return (m + e + s) / 3

def calculate_age(year_birth):
    current_year = 2026
    return current_year - year_birth

def generate_report():
    print("--- Personal & Academic Data Entry ---\n")
    
    name = input("Name: ")
    year_birth = int(input("Birth Year: "))
    height = float(input("Height (cm): "))
    weight = float(input("Weight (kg): "))
    
    print("\n--- Subject Grades ---")
    m = float(input("Math: "))
    e = float(input("English: "))
    s = float(input("Science: "))
    
    age = calculate_age(year_birth)
    bmi_value = calculate_bmi(height, weight)
    health_label = determine_health_status(bmi_value)
    final_avg = calculate_average(m, e, s)
    
    print("\n" + "="*15 +"Summary_Report" + "="*15)
    print(f"Personal Profile: {name} is {age} years old this year.")
    print(f"Physical Stats: With a height of {height}cm and weight of {weight}kg,")
    print(f"the resulting BMI is {bmi_value:.2f}, classified as {health_label}.")
    print(f"Academic Performance: The average grade across Math, English,")
    print(f"and Science is {final_avg:.2f}%.")
    print("="*43 + "\n")

generate_report()
# def BMI():
    # name = input("What is your name? ")
    # age = int(input("How old are you?"))
    # weight = float(input("What is your weight in kg? "))
    # height = float(input("What is your height in meters?"))
    # print("I'm", name)
    # print(age, "years old")
    # print("Your BMI is ", weight/height**2)
# BMI()

# x = float(input("Math grade:"))
# y = float(input("EngIish grade:"))
# z = float(input("Science grade:"))

# def grades():
    ag =(x+y+z)/3
    # print("Your Average grade is ", ag)
    # if ag >=95 and ag <= 100:
        # print("You are excellent")
    # else:
        # print("Keep up the good work")
# grades()