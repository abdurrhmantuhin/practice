import datetime

print("Welcome to personal information manger!")
print("=" * 39)

name = str(input("Enter your name: "))
nick_name = (input("entet your nickname: "))
age = int(input("Enter your age: "))
birth_year = int(input("Enter yourbirth year: "))
is_student = (input("are you student? (yes or no)")).lower() == "yes"
college = (input("enter your college name: "))
city = (input("enter your city:"))

print(f"your name: {name} and data type : {type(name)}")
print(f"your nickname: {nick_name} and data type : {type(nick_name)}")
print(f"your age: {age} and data type : {type(age)}")
print(f"your birth year: {birth_year} and data type : {type(birth_year)}")
print(f"your student status: {is_student} and data type : {type(is_student)}")
print(f"your collage: {college} and data type : {type(college)}")
print(f"your city: {city} and data type : {type(city)}")


print ("=" * 27)
print (f"Calculations and Processing")
print ("=" * 27)
print("prossesing please wait...")

adult = age >= 18
teenager = 13 <= age <= 19
senior = age < 50
calculet_year = datetime.datetime.now().year
calculet_age = calculet_year - birth_year

status , category , health_status = "Active" , "User" , "Healtha"

print("\n your complete profile ")
print("=" * 35)

print(f"name:{name}({nick_name})")
print(f"age:{age} years old")
print(f"birth year:{birth_year}")
print(f"student status:{is_student}")
print(f"collage name:{college}")
print(f"city:{city}")

print(f"\n🔍 Advanced Analysis:")
print("-" * 25)

if calculet_age == age:
    print(f"✅ Age verification: Correct")
else:
    print(f"❌ Age verification: There's a {abs(calculet_age - age)} year difference")

print(f"\n📋 Complete Data Summary:")
print("=" * 40)

APP_NAME = "Personal Info Manager"
VERSION = "2.9"
AUTHOR = "TUHIN"

def display_app_info():
    """Function to demonstrate global variable usage"""
    global APP_NAME, VERSION, AUTHOR
    print(f"\n🔧 Application Info:")
    print(f"App: {APP_NAME}")
    print(f"Version: {VERSION}")
    print(f"Author: {AUTHOR}")

display_app_info()
