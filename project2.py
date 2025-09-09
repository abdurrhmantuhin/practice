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
