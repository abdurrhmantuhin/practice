import datetime

print("🎯  Welcome to personal information maneger 🎯")
print ("=" * 50)

print ("\n📝 Please enter your basic infomation: ")
print("=" * 40 )

name = str(input("Enter your full Name: "))
nickname = input("Enter your nickname ")

age = int(input("Enter your age: "))
birth_year = int(input("Enter your birht year: "))

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

is_student = input("Are you a student? (yes or no): ").lower() == "yes"

lucky_number = complex(input("Enter your lucky number (can be complex like 5 + 3j): "))

print("=" * 40 )
print("\n🔍 data type analysis:")
print("-" * 30 )
print(f"Name  type: {type(name)}")
print(f"Age type: {type(age)}")
print(f"Height type: {type(height)}")
print(f"Student status type: {type(is_student)}")
print(f"Lucky number type: {type(lucky_number)}")

print ("\n🧮 Calculations and Analysis: ")
print("-" * 40 )

current_year = datetime.datetime.now().year
calculated_age = current_year - birth_year

height_m = height / 100 
bmi = weight / (height_m ** 2 )

is_adult = age >= 18 
is_teenager = 13 <= age <= 19 
is_senior = age >= 50

is_underweight = bmi <= 18.5
is_normal = 18.5 <= age <= 25 
is_overweight = 25 <= bmi <= 30 
is_obese = bmi >= 30


status, category, helth_status = "Active", "User", "Healthy"
default_score = perfect_score = max_score = 100

print ("\n🔍 Advanced Analysis:")
print("-" * 25)


if calculated_age == age :
    print (f"✅ Age verification: Correct!")
else:
    print (f"❌ Age verification: there's a {abs(calculated_age - age )} year diffrence!")


print (f"📊 BMI: {bmi:.2f}")
if is_underweight:
    bmi_catgory = "Underweigth!"
    helth_advice = "Consider gaining some weight"
elif is_normal:
    bmi_catgory = "Normal"
    helth_advice = "Maintain your current weigh"
elif is_overweight:
    bmi_catgory = "Ovare weight!"
    helth_advice = "Consider losing some weight!"
else:
    bmi_catgory = "Obese"
    helth_advice = "Consult a doctor for weight management!"

print (f"📋 BMI Category: {bmi_catgory}")
print(f"💡 Health Advice: {helth_advice}")

print(f"\n👥 Age Category Analysis: ")
if is_teenager:
    age_category = "Teenager"
elif is_adult and not is_senior:
    age_category = "Adult"
elif is_senior:
    age_category = "Senior"
else :
    age_category = "Child"

print (f'📊 Age Category: {age_category}')

print(f"\n📋 Complete Data Summary:")
print ("=" * 40)

summary_name = name 
summary_age = age
summary_height = height
summary_weight = weight
summary_bmi = round(bmi , 2)
summary_category = age_category
summary_student = is_student
summary_lucky = lucky_number

print(f"📝 Name: {summary_name} (type:{type(summary_name).__name__} )")
print(f"🔢 Age: {summary_age} (type:{type(summary_age).__name__} )")
print(f"📏 heigth: {summary_height} cm (type:{type(summary_height).__name__} )")
print(f"⚖️ weight: {summary_weight} km (type:{type(summary_weight).__name__} )")
print(f"📊 BMI: {summary_bmi} (type:{type(summary_bmi).__name__} )")
print(f"👥 Category: {summary_category} (type:{type(summary_category).__name__} )")
print(f"🎓 Student: {summary_student} (type:{type(summary_student).__name__} )")
print(f"🍀 Lucky Number: {summary_lucky} (type:{type(summary_lucky).__name__} )")


APP_NAME = "Personal info Manager"
VERSION = "1.0"
AUTHOR = "TUHIN"

def display_app_info():
    """function to demonstrate gloabal variable usage """
    global APP_NAME, VERSION, AUTHOR
    print(f"\n🔧 Application info:")
    print(f"App: {APP_NAME}")
    print(f"Version: {VERSION}")
    print(f"Author: {AUTHOR}")
display_app_info()



print(f"\n🔄 Type Conversion Examples:")
print("-" * 35)

age_str = str(age)
age_float = float(age)
age_bool = bool(age)

print(f"Age as str : '{age_str}' (type: {type(age_str).__name__})")
print(f"Age as float : '{age_float}' (type: {type(age_float).__name__})")
print(f"Age as bool : '{age_bool}' (type: {type(age_bool).__name__})")

print(f"\n🎉 Final Report Card for {name}")
print("=" * 50)


report_line1 = f"Name: {name} | Age: {age} | Category: {age_category}"
report_line2 = f"Height: {height}cm | Weight: {weight}kg | BMI: {bmi:.1f}"
report_line3 = f"Student {'Yes' if is_student else 'NO'} | Lucky number:{lucky_number}"


print(f"📄 {report_line1}")
print(f"📄 {report_line2}")
print(f"📄 {report_line3}")

health_score = 0 
if is_normal:
    health_score += 50
if is_adult:
    health_score += 20 
    if not is_senior or age < 55:
        health_score += 20
health_score += min(10, age // 10 ) 

print(f"🏆 Health Score: {health_score}/100")
print(f"✅ Project Completed Successfully!")
print(f"📚 Concepts Learned: Variables, Data Types, String Formatting, Type Conversion, Boolean Logic")


def save_profile ():
    """Save profile to a text file"""
    filename = f"{name.replace(' ', '_')}_profile.txt"

    with open (filename,'w') as file :
        file.write(f"Personal Profile: {name}")
        file.write(f"Age: {age}\n")
        file.write(f"BMI: {bmi:.2f}\n")
        file.write(f"Category: {age_category}\n")
        file.write(f"Health Score: {health_score}/100\n")

    print(f"💾 Profile saved to {filename}") 