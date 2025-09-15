import random
from datetime import datetime, timedelta

print("👥 Welcome to Social Network Friend Manager 👥")
print("=" * 55)

print("\n🌟 Creating User Profiles and Friend Networks...")

your_friends = {
    "Ahmed", "Fatima", "Omar", "Aisha", "Hassan", 
    "Zara", "Karim", "Nadia", "Rashid", "Layla"
}

your_family = {
    "Hassan", "Zara", "Uncle Ali", "Aunt Sarah", 
    "Cousin Ahmad", "Sister Maryam"
}

work_colleagues = {
    "John", "Sarah", "Ahmed", "Lisa", "Omar", 
    "Emily", "David", "Fatima", "Mike"
}

university_friends = {
    "Karim", "Nadia", "Alex", "Maya", "Rashid", 
    "Sophie", "Hassan", "Emma", "Daniel"
}

gaming_friends = {
    "GamerX", "ProPlayer", "Ahmed", "CoolGamer", 
    "Karim", "EliteSniper", "Hassan", "GameMaster"
}

sports_friends = {
    "Captain Ali", "Omar", "Team_Mate1", "Rashid", 
    "Coach Ahmed", "Player5", "Nadia"
}

print("✅ Friend networks created!")
print(f"Your friends: {len(your_friends)} peoples")
print(f"family members: {len(your_family)} peoples")
print(f"Work colleagues: {len(work_colleagues)} peoples")
print(f"university friends: {len(university_friends)} peoples")
print(f"gaming friends: {len(gaming_friends)} peoples")
print(f"sports friends: {len(sports_friends)} peoples")

print("\n🔍 Set Properties Analysis:")
print("-" * 35)

duplicate_list = ["Ahmed", "Ahmed", "Fatima", "Omar", "Ahmed", "Aisha"]
unique_friends = set(duplicate_list)

print(f"📋 Original list with duplicates: {duplicate_list}")
print(f"🎯 Unique friends after conversion: {unique_friends}")
print(f"📊 Removed {len(duplicate_list) - len(unique_friends)} duplicates")

print(f"\n🔍 Membership Testing:")
test_names =  ["Ahmed", "John", "RandomPerson", "Fatima"]

for name in test_names:
    in_friends = name in your_friends
    in_colleagues = name in work_colleagues
    print (f"   {name}: Friends={in_friends}, colleagues={in_colleagues}")

    
print("\n🔗 Set Operations Analysis:")
print("-" * 32)

all_contacts = your_friends.union(work_colleagues, university_friends)
print(f"total unique contacts (Union):{len(all_contacts)} people")

all_social_contacts = your_friends | unique_friends | gaming_friends
print(f"🎮 All social contacts: {len(all_social_contacts)} people")

friends_and_colleagues = your_friends.intersection(work_colleagues)
friends_and_uni = your_friends.intersection(university_friends)
family_and_friends = your_family.intersection(your_friends)


print(f"\n🤝 Common Connections:")
print(f"    Friends who are also colleagues: {friends_and_colleagues}")
print(f"    Friends from university days: {friends_and_uni}")
print(f"    Family members who are friends: {family_and_friends}")

common_gaming_sports = gaming_friends & sports_friends
print(f"    Gaming + sports overlap:{common_gaming_sports}")

work_only_friends = work_colleagues.difference(your_friends)
friends_not_colleagues = your_friends.difference(work_colleagues)

print(f"\n🔄 Unique Groups:")
print(f"     Colleagues who aren't personal friends: {work_only_friends}")
print(f"     Personal friends not from work: {friends_not_colleagues}")

exclusive_contacts = your_friends.symmetric_difference(work_colleagues)
print(f"   Either friends OR colleagues (not both): {exclusive_contacts}")

print("\n🛠️  Set Methods in Action:")
print("-" * 28)
temp_friends = your_friends.copy()
temp_colleagues = work_colleagues.copy()

print("➕ Adding new connections:")
temp_friends.add("New Friend")
temp_friends.add("Ahmed")
print(F"    added 'new friends': {len(temp_friends)} total friends")

new_connections = {"Friend1", "Friend2", "Friend3"}
temp_friends.update(new_connections)
print(f"    added multiple connections: {len(temp_friends)} total friends")

print(f"\n➖ Removing connections:")
if "New Friend" in temp_friends:
    temp_friends.remove("New Friend")
    print("   Removed 'New Friend' using remove()")

temp_friends.discard("NonExistent")
temp_friends.discard("Friend1")
print("   Used discard() safely")

if temp_friends:
    popped_friend = temp_friends.pop()
    print(f"   Randomly removed: {popped_friend}")

temp_set = {"temp1","temp2","temp3"}
temp_set.clear()
print(f"   Cleared temp set: {len(temp_set)} elements")

print("\n🧠 Advanced Set Analysis:")
print("-" * 30)

def analyze_social_circles():
    all_people = (your_friends | work_colleagues | university_friends |
                  gaming_friends | sports_friends)
    
    analysis = {
        'total_connections' : len(all_people) , 
        'close_friends' : your_friends,
        'professional_network' : work_colleagues,
        'social_overlap' : {},
        'network_strength' : {}
    }

    circles = {
        'Personal': your_friends,
        'Work': work_colleagues,
        'University': university_friends,
        'Gaming': gaming_friends,
        'Sports': sports_friends
    }

    for name1, circle1 in circles.items():
        analysis['social_overlap'][name1] = {}
        for name2, circle2 in circles.items():
            if name1 != name2:
                overlap = circle1 & circle2
                analysis['social_overlap'][name1][name2] = len(overlap)

    return analysis, all_people

social_analysis, all_connections = analyze_social_circles()

print(f"📊 Social Network Statistics:")
print(f"   🌐 Total unique connections: {social_analysis['total_connections']}")


print(f"\n🔗 Cross-Circle Connections:")
for circle1, overlaps in social_analysis['social_overlap'].items():
    for circle2, count in overlaps.items():
        if count > 0:
            print(f"   {circle1} ↔ {circle2}: {count} mutual connections")



print("\n⚡ Set Comprehension Examples:")
print("-" * 34)

short_names = {name for name in your_friends if len(name) <= 5}
long_name =  {name for name in your_friends if len(name) > 5}

print(f"📝 Short names (≤5 chars): {short_names}")
print(f"📝 Long names (>5 chars): {long_name}")

vowel_names = {name for name in all_connections if name[0].upper() in 'AEIOU'}
consonant_names = {name for name in all_connections if name[0].upper() not in 'AEIOU'}

print(f"🔤 Names starting with vowels: {vowel_names}")
print(f"🔤 Names starting with consonants: {len(consonant_names)} names")

gaming_usernames = {name for name in gaming_friends if not name.isalpha()}
print(f"🎮 Gaming usernames: {gaming_usernames}")



print("\n🤖 Smart Friend Recommendations:")
print("-" * 38)


def recommend_friends():
    potential_friends = set()
    friend_networks = {
            "Ahmed": {"Ali", "Sara", "Omar", "Maya"},
        "Fatima": {"Layla", "Noor", "Hassan", "Zara"},
        "Omar": {"Ahmed", "John", "Lisa", "Mike"},
        "Hassan": {"Fatima", "Ali", "Cousin Ahmad"},
        "Karim": {"Alex", "Maya", "Sophie", "Daniel"}
 }

    recommendations = {}

    for friend in your_friends:
        if friend in friend_networks:
            friend_of_friends = friend_networks[friend] - your_friends - {friend}
            for potential in friend_of_friends:
                if potential not in recommendations:
                    recommendations[potential] = []
            recommendations[potential].append(friend)
    return recommendations

friend_recommendations = recommend_friends()

print("💡 People you might know:")
for person, mutual_friends in friend_recommendations.items():
    print(f"   👤 {person} (through: {', '.join(mutual_friends)})")


print("\n👥 Group Management:")
print("-" * 25)

birthday_party_invites = your_friends | your_family
work_party_invites = work_colleagues | {name for name in your_friends if name in work_colleagues}
study_group = university_friends & your_friends
gaming_tournament = gaming_friends - {"GamerX"}

print(f"🎂 Birthday party invites: {len(birthday_party_invites)} people")
print(f"💼 Work party invites: {len(work_party_invites)} people")
print(f"📚 Study group: {study_group}")
print(f"🏆 Gaming tournament players: {len(gaming_tournament)} people")

birthday_work_conflict = birthday_party_invites & work_party_invites
if birthday_work_conflict:
    print(f"⚠️  People invited to both events: {birthday_work_conflict}")
