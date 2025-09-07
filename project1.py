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


print("\n🔍 data type analysis:")
print("-" * 30 )
print(f"Name  type: {type(name)}")
print(f"Age type: {type(age)}")
print(f"Height type: {type(height)}")
print(f"Student status type: {type(is_student)}")
print(f"Lucky number type: {type(lucky_number)}")

print ("\n🧮 Calculations and Analysis: ")
print("=" * 40 )

current_year = datetime.datetime.now().year
calculated_age = current_year - birth_year
print(calculated_age)
# height_m = height / 100 
# bmi = weight / (height_m ** 2 )

# is_adult = age >= 18 
# is_teenager = 13 <= age <= 19 
# is_senior = age >= 50

# is_underweight = bmi <= 18.5
# is_normal = 18.5 <= age <= 25 
# is_overweight = 25 <= bmi <= 30 
# is_obese = bmi >= 30


# status, category, helth_status = "Active", "User", "Healthy"
# default_score = perfect_score = max_score = 100

# print ("\n🔍 Advanced Analysis:")
# print("-" * 25)


# if calculated_age == age :
#     print (f"✅ Age verification: Correct!")
# else:
#     print (f"❌ Age verification: there's a {abs(calculated_age - age )} year diffrence!")