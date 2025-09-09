import random
from datetime import datetime 
print ("🍽️  Welcome to Tuhin's Restaurant Management System 🍽️")
print ("=" * 60)


print("\n📋 Creating Initial Menu...")

appetizers = ["Chicken wings", "Mozzarella Sticks", "Garlic Bread", "Soup of the Day"]
main_courses = ["Beef Steak", "Grilled Chicken", "Fish Curry", "Vegetable Biryani", "Pasta"]
desserts = ["Chocolate Cake", "Ice Cream", "Tiramisu", "Fruit Salad"]
beverages = ["Coffee", "Tea", "Soft Drink", "Fresh Juice", "Water"]


appetizer_prices = [8.99, 6.50, 4.99, 5.50]
main_course_prices = [25.99, 18.50, 22.00, 16.99, 14.50]
dessert_prices = [7.99, 4.50, 8.99, 6.50]
beverage_prices = [3.50, 2.50, 2.99, 4.50, 1.00]

restaurant_info = ["tuhin restaurant",2005 , True , 4.9 , ["fine dining", "family friendly"]]

print ("✅ Initial menu created successfully!")


print("\n🔧 List Methods in Action:")
print("=" * 30)
print("➕ Adding new items...\n")

appetizers.append("Spring Rolls")
appetizer_prices.append(7.99)
print(f"Added Spring Rolls to appetizers: {len(appetizers)} items now")

main_courses.insert(0,"today's special")
main_course_prices.insert(0,28.99)
print(f"Added Today's Special at the beginning")


new_beverages = ["Smoothie", "Milkshake", "Energy Drink"]
new_beverages_prices = [5.99, 6.50, 7.99]
beverages.extend(new_beverages)
beverage_prices.extend(new_beverages_prices)
print(f"Extended beverages menu: {len(beverages)} items now")

print("\n➖ removing items....")
if "Soup of the Day" in appetizers:
    soup_index = appetizers.index("Soup of the Day")
    remove_item = appetizers.pop(soup_index)
    remove_price = appetizer_prices.pop(soup_index)
    print (f"Removed: {remove_item} (${remove_price})")

if len(desserts) > 2:
    del desserts[-1]
    del dessert_prices[-1]
    print ("removed last item")

beckup_beverages = beverages.copy()
temp_list = ["temp1", "temp2", "temp3"]
temp_list.clear()
print(f"Cleared temp list, now has {len(temp_list)} items")


print("\n✂️  List Slicing Operations:")
print("-" * 35)

print(f"First 3 main courses:{main_courses[:3]}")
print(f"last 2 deserts: {desserts[-2:]}")
print(f"middle appetizers:{appetizers[1:-1]}")

print(f"Every 2nd main beverage:{beverages[::2]}")
print(f"reversed main courses: {main_courses[::-1]}")

featured_items = main_courses [0:2]
budget_options = [item for i, item in enumerate(main_courses) if main_course_prices [i] < 20.00 ]

print(f"featured items: {featured_items}")
print(f"budget options: {budget_options}")


print("\n⚡ List Comprehension Examples:")
print("=" * 40)

expensive_items = [item for i, item in enumerate(main_courses) if main_course_prices[i] > 20.00]
affordable_dessertn = [item for i, item in enumerate(desserts) if dessert_prices[i] < 7.00]

print(f"💎 Expensive main courses: {expensive_items}")
print(f"🍰 Affordable desserts: {affordable_dessertn}")

discounted_main_prices = [round(price * 0.8,2) for price in main_course_prices]
price_with_tax = [round(price * 1.15,2) for price in appetizer_prices]

print(f"💸 Discounted main course prices: {discounted_main_prices}")
print(f"💰 Appetizer prices with tax:{price_with_tax}")

premium_items = [f"{item} (premium)" for i, item in enumerate(main_courses) if main_course_prices [i] > 22.00]
combo_suggestions = [f"{app}+{main}" for app in appetizers[:2] for main in main_courses[:2]]

print(f"👑 Premium items: {premium_items}")
print(f"🍽️  Combo suggestions: {combo_suggestions[:4]}")


print("\n📊 Advanced Menu Structure (Nested Lists):")
print("=" * 50)

complete_menu = [
    ["Appetizers", appetizers, appetizer_prices],
    ["Main Courses", main_courses, main_course_prices],
    ["Desserts", desserts, dessert_prices],
    ["Beverages", beverages, beverage_prices]
]


for category_data in complete_menu:
    category_name , items , prices = category_data
    print(f"\n🍴 {category_name.upper()}:")
    print("="*20)
    for i in range(len(items)):
        print(f"  {i+1}. {items[i]:<20} - ${prices[i]:>6.2f}")

