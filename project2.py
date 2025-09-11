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

print("\n📈 Menu Statistics:")
print("=" * 25)

total_price = len(appetizers) + len(main_courses) + len(desserts) + len(beverages)
all_price = appetizer_prices + main_course_prices + dessert_prices + beverage_prices

print(f"📊 Total menu items: {total_price}")
print(f"💰 Average price: $ {sum(all_price) / len(all_price):.2f}")
print(f"💎 Most expensive: ${max(all_price):.3f}")
print(f"💵 Cheapest: $ {min(all_price):.2f}")


category_stats = []
for category_data in complete_menu:
    category_name , items ,  prices = category_data
    avg_price = sum(prices) / len (prices)
    category_stats.append([category_name, len(items) , avg_price])


print(f"\n📋 Category Breakdown:")
for stat in category_stats:
    name, count, avg = stat 
    print(f"{name:<15}:{count:>2} items , avg ${avg:>6.2f}")




def search_menu (keyword):
    """Search for items containg keywords"""
    results = []


    all_items = appetizers + main_courses + desserts + beverages
    all_categories = (["Appetizers"] * len(appetizers)+
                      ["main courses"] * len(main_courses) +
                      ["deserts"] * len(desserts) +
                      ["beverages"] * len(beverages))
    

    for i, item in enumerate(all_items):
        if keyword.lower() in item.lower():
            results.append(f"{item} ({all_categories[i]})")
    

    return results

def calculate_order_total(order_items):
    total = 0.0
    item_details = []


    all_items = appetizers + main_courses + desserts + beverages
    all_prices = appetizer_prices + main_course_prices + dessert_prices + beverage_prices
    items_price_dict = dict(zip(all_items , all_prices))

    for item in order_items:
        if item in items_price_dict:
            price = items_price_dict[item]
            total += price 
            item_details.append(f"{items}:${price:.2f}")
        else:
            item_details.append(f"{item}: item not found")
        

    return total, item_details

def get_daily_special():
    all_items = appetizers + main_courses + desserts + beverages
    all_prices = appetizer_prices + main_course_prices + dessert_prices + beverage_prices

    special_indices = random.sample(range(len(all_items)), min(3, len(all_items)))
    specials = []
    for i in special_indices:
        original_price = all_prices[i]
        discounted_price = original_price * 0.85
        specials.append([all_items[i], original_price, discounted_price])

    return specials


print("\n🔍 Menu Operations Demo:")
print("=" * 35)

search_result =  search_menu("chicken")
print(f"🔍 Search for 'chicken': {search_result}")

sample_order = ["Checken Wings", "Beef Steak", "Coffee"]
order_total, order_details = calculate_order_total(sample_order)
print(f"\n🧾 Sample Order:")
for detail in order_details:
    print(f"  {detail}")
print(f"  total: ${order_total:.2f}")


daily_specials = get_daily_special()
print(f"\n⭐ Today's Specials:")
for special in daily_specials:
    item, original, discounted = special
    savings = original - discounted
    print(f"      {item}: ${original:.2f} → ${discounted:.2f}(save ${savings:.2f})")



print("\n📊 Menu Sorting Options:")
print("-" * 30)

# Sort by price (create sorted versions without modifying originals)
sorted_mains_by_price = sorted(zip(main_courses, main_course_prices), key=lambda x: x[1])
sorted_desserts_alphabetical = sorted(desserts)

print("💰 Main courses by price (low to high):")
for item, price in sorted_mains_by_price:
    print(f"   {item}: ${price:.2f}")

print(f"\n🔤 Desserts alphabetically: {sorted_desserts_alphabetical}")

# Reverse sorting
expensive_first = sorted(zip(appetizers, appetizer_prices), key=lambda x: x[1], reverse=True)
print(f"\n💎 Appetizers by price (high to low):")
for item, price in expensive_first:
    print(f"   {item}: ${price:.2f}")
    


print("\n🚀 Advanced List Features:")
print("=" * 30)

original_menu = main_courses.copy()
modified_menu = main_courses[:]

modified_menu.append("new fusion dish")
modified_menu.sort()

print(f"Original menu length: {len(original_menu)}")
print(f"Modified menu length: {len(modified_menu)}")
print(f"Lists are different: {original_menu != modified_menu}")