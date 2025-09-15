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


print("\n🔒 Privacy Management:")
print("-" * 25)

public_profile_viewers = all_connections
close_friends_only = your_friends & your_family
blocked_users = {"SpamUser", "ToxicPlayer", "Stranger123"}

def check_content_visibility(viewer,content_type):
    privacy_settings = {
        'posts': your_friends | work_colleagues,
        'photos': your_friends,
        'personal_info': your_friends & your_family,
        'location': your_friends - work_colleagues
    }

    if viewer in blocked_users:
        return False
    return viewer in privacy_settings.get(content_type, set())

test_viewers = ["Ahmed", "John", "SpamUser", "Hassan"]
content_type = ["posts", "photos", "personal_info", "location"]

print("🔍 Content Visibility Test:")
for viewer in test_viewers:
     print(f"   👤 {viewer}:")
     for content in content_type:
         can_view = check_content_visibility(viewer,content)
         status = "✅" if can_view else "❌"
         print(f"      {status} {content}")


print("\n📈 Network Growth Simulation:")
print("-" * 35)

def simulate_network_growth(days=30):
    initial_network = your_friends.copy()
    growth_history = [len(initial_network)]

    for day in range (1, days + 1 ):
        if random.random() < 0.3:
            new_connections = random.randint(1,3)
            for _ in range(new_connections):
                new_friend = f"NewFriend_{day}_{random.randint(1,100)}"
                initial_network.add(new_friend)


        if random.random() < 0.5 and len(initial_network) > 5:
            lost_friend = random.choice(list(initial_network))
            initial_network.discard(lost_friend)

        growth_history.append(len(initial_network))

    return growth_history, initial_network

growth_data, final_network = simulate_network_growth(30)

print(f"📊 Network Growth Over 30 Days:")
print(f"    📅 Starting connections: {growth_data[0]}")
print(f"    📅 Final connections: {growth_data[-1]}")
print(f"    📈 Net growth: {growth_data[-1] - growth_data[0]}")
print(f"    📊 Growth rate: {((growth_data[-1] / growth_data[0]) - 1) * 100:.1f}%")

milestones = [7,14,21,30]
print(f"\n🎯 Growth Milestones:")
for day in milestones:
    if day < len(growth_data):
        print(F"    Day{day:2d}: {growth_data[day]} connections")
        

print("\n📱 Social Media Features:")
print("-" * 30)

your_interests = {"#coding", "#gaming","#sports" "#travel", "#food"}
trending_hastags = {"#coding","#ai", "#travel", "#fitness", "#music", "#food"}
friend_interests = {
    "Ahmed": {"#coding", "#AI", "#tech"},
    "Fatima": {"#travel", "#photography", "#food"},
    "Omar": {"#sports", "#fitness", "#gaming"},
    "Hassan": {"#music", "#travel", "#art"}
}

common_trends = your_interests & trending_hastags
print(f"🔥 Your interests in trending: {common_trends}")

similar_interest_friends = {}
for friend, interests in friend_interests.items():
    common = your_interests & interests
    if common:
        similar_interest_friends[friend] = common

print(f"\n🤝 Friends with similar interests:")
for friend, common in similar_interest_friends.items():
    print(f"    {friend}: {common}")


print("\n🧮 Advanced Network Analysis:")
print("-" * 35)

def comprehensive_network_analysis():
    all_Circles = [your_friends, your_family, work_colleagues, unique_friends, gaming_friends,sports_friends]
    circle_name = ["Personal", "Work", "Gaming","Sports", "Family"]
    
    analysis_results = {}
    
    total_unique = set()
    for circle in all_Circles:
        total_unique.update(circle)

    analysis_results["total_unique_contacts"] =  len(total_unique)

    connection_count = {}
    for person in total_unique:
        count = sum(1 for circle in all_Circles if person in circle)
        connection_count[person] = count

    super_connectors = {person: count for person, count in connection_count.items() if count > 2}


    total_possible_connections = len(all_Circles)
    actual_connections = {person: count for person, count in connection_count.items()}
    analysis_results['super_connectors'] = super_connectors
    analysis_results['average_connections'] = sum(connection_count.values()) / len(connection_count)
    
    return analysis_results

network_insights = comprehensive_network_analysis()

print(f"🌐 Network Insights:")
print(f"   📊 Total unique contacts: {network_insights['total_unique_contacts']}")
print(f"   📈 Average connections per person: {network_insights['average_connections']:.1f}")

print(f"\n⭐ Super Connectors (in 3+ circles):")
for person, connections in network_insights['super_connectors'].items():
    print(f"   👤 {person}: appears in {connections} circles")


print("\n" + "="*60)
print("🎓 PROJECT COMPLETION SUMMARY")
print("="*60)

print("\n📚 Sets Concepts Mastered:")
sets_concepts = [
    "✅ Set Creation and Basic Properties",
    "✅ Set Membership Testing (in, not in)",
    "✅ Set Union Operations (|, union)",
    "✅ Set Intersection Operations (&, intersection)", 
    "✅ Set Difference Operations (-, difference)",
    "✅ Set Symmetric Difference (^, symmetric_difference)",
    "✅ Set Methods (add, remove, discard, pop, clear)",
    "✅ Set Comprehension",
    "✅ Set Comparison and Relationships",
    "✅ Real-world Network Analysis",
    "✅ Privacy and Security with Sets"
]

for concept in sets_concepts:
    print(f"   {concept}")


print(f"\n📊 Project Statistics:")
print(f"   🌐 Total unique network contacts: {len(all_connections)}")
print(f"   👥 Different social circles: 6")
print(f"   🔗 Cross-circle connections identified: {sum(sum(overlaps.values()) for overlaps in social_analysis['social_overlap'].values()) // 2}")
print(f"   🤖 Friend recommendations generated: {len(friend_recommendations)}")
print(f"   🔒 Privacy levels implemented: 4")

print(f"\n🚀 Skills Ready for Machine Learning:")
ml_ready_skills = [
    "Unique data identification and deduplication",
    "Set operations for data filtering",
    "Network analysis and graph theory basics",
    "Intersection analysis for common patterns",
    "Efficient membership testing",
    "Data relationship mapping"
]

for skill in ml_ready_skills:
    print(f"   ✅ {skill}")

print(f"\n💡 Real-world Applications Learned:")
applications = [
    "🔍 Data deduplication in datasets",
    "📊 Finding common features between groups",
    "🌐 Social network analysis",
    "🔒 Permission and access control systems",
    "📈 Market segmentation analysis",
    "🎯 Recommendation system foundations"
]

for app in applications:
    print(f"   {app}")

print(f"\n🎯 Next Steps:")
next_challenges = [
    "Master Dictionaries (Project 7)",
    "Advanced Loops and Iterations (Project 8)",
    "String Processing (Project 9)",
    "File Handling and Data Persistence",
    "Move to NumPy for numerical sets",
    "Learn NetworkX for advanced graph analysis"
]

for step in next_challenges:
    print(f"   📌 {step}")

print(f"\n⚡ Performance Insights:")
print("-" * 25)

import time 
def performance_comparison():
    large_list = list(range(10000))
    large_set = set(range(10000))
    test_values = [1, 5000, 9999, 15000]
    
    print(f"🔍 Membership Testing Performance:")
    print(f"   Dataset size: 10,000 items")
    for value in test_values:
        start_time = time.time()
        for _ in range(1000):
            result_list = value in large_list
        list_time =  time.time() - start_time

        start_time = time.time()
        for _ in range(1000):
            result_set = value in large_set
        set_time = time.time() - start_time

        speedup = list_time / set_time if set_time > 0 else float ("inf")
        print(f"   Testing {value}: Set is {speedup:.1f}x faster")

performance_comparison()

print(f"\n🧬 Advanced Set Applications:")
print("-" * 35)

def analyze_interest_compatibility():
    
    interest_database = {
        "Ahmed": {"coding", "AI", "tech", "gaming", "sci-fi"},
        "Fatima": {"travel", "photography", "food", "art", "nature"},
        "Omar": {"sports", "fitness", "gaming", "cars", "adventure"},
        "Hassan": {"music", "travel", "art", "history", "culture"},
        "Karim": {"gaming", "coding", "anime", "tech", "movies"},
        "Nadia": {"books", "writing", "coffee", "travel", "languages"},
        "Rashid": {"sports", "business", "finance", "networking", "leadership"},
        "Layla": {"fashion", "beauty", "travel", "photography", "lifestyle"}
    }

    your_detailed_interests = {"coding", "gaming", "tech", "travel", "sports", "music"}
    compatibility_scores = {}
    
    for person, intersts in interest_database.items():
        common_interests = your_detailed_interests & interests
        total_unique_interests = your_detailed_interests | interests

        compatibility_score = len(common_interests) / len(total_unique_interests)
        compatibility_scores[person] = {
            'score': compatibility_score,
            'common': common_interests,
            'unique_to_them': interests - your_detailed_interests,
            'unique_to_you': your_detailed_interests - interests
        }


    return compatibility_scores


compatibility_analysis = analyze_interest_compatibility()

print(f"🎯 Interest Compatibility Analysis:")
sorted_compatibility = sorted(compatibility_analysis.items(), 
                            key=lambda x: x[1]['score'], reverse=True)

for person, data in sorted_compatibility[:5]:
    score_percent = data['score'] * 100
    print(f"\n   👤 {person}: {score_percent:.1f}% compatible")
    print(f"      🤝 Common: {data['common']}")
    if data['unique_to_them']:
        print(f"      🆕 They like: {list(data['unique_to_them'])[:3]}")


print(f"\n🧹 Data Cleaning with Sets:")
print("-" * 30)

def clean_contact_data():
    raw_contacts = [
        "ahmed@email.com", "AHMED@EMAIL.COM", "fatima@test.com",
        "omar@work.com", "ahmed@email.com", "Fatima@Test.com",
        "", "invalid-email", "hassan@company.com", None,
        "zara@home.com", "OMAR@WORK.COM"
    ]

    valid_emails = set()
    invalid_entries = set()

    for contact in raw_contacts:
        if contact and isinstance(contact, str) and "@" in contact:
            clean_contact = contact.lower().strip()
            if "." in clean_contact.split("@")[1]:
                valid_emails.add(clean_contact)
            else:
                invalid_entries.add()
        else:
            if content:
                invalid_entries.add(str(contact))

    return valid_emails, invalid_entries, len(raw_contacts) - len(valid_emails) - len(invalid_entries)

clean_emails, invalid_emails, empty_count = clean_contact_data()

print(f"📧 Email Cleaning Results:")
print(f"   📥 Raw entries: 12")
print(f"   ✅ Valid unique emails: {len(clean_emails)}")
print(f"   ❌ Invalid entries: {len(invalid_emails)}")
print(f"   🗑️  Empty/None entries: {empty_count}")

print(f"\n📋 Clean email list:")
for email in sorted(clean_emails):
    print(f"   ✉️  {email}")


print(f"\n🏆 FINAL CHALLENGE: Social Media Influencer Analysis")
print("=" * 60)

def influencer_analysis():
    influencers = {
        'TechGuru': {'AI', 'coding', 'tech', 'innovation', 'startups'},
        'FoodieLife': {'cooking', 'restaurants', 'travel', 'food', 'culture'},
        'FitnessKing': {'workout', 'nutrition', 'sports', 'health', 'motivation'},
        'TravelQueen': {'travel', 'photography', 'adventure', 'culture', 'nature'},
        'GameMaster': {'gaming', 'tech', 'streaming', 'esports', 'reviews'}
    }

    your_content = {'tech', 'gaming', 'travel', 'food', 'coding'}
    results = {}

    for influencer, content in influencers.items():
        overlap = your_content & content
        unique_to_them = content - your_content
        coverage = len(overlap) / len(your_content)
        diversity = len(unique_to_them) 


        results[influencer] = {
            'relevance_score': coverage * 100,
            'discovery_potential': diversity,
            'shared_interests': overlap,
            'new_content': unique_to_them
        }

    return results
influence_analysis = influencer_analysis()

print(f"\n📊 Influencer Recommendation Results:")

sorted_influencers = sorted(influence_analysis.items(), 
                          key=lambda x: x[1]['relevance_score'], reverse=True)

for rank, (influencer, data) in enumerate(sorted_influencers, 1):

    print(f"\n{rank}. 🌟 {influencer}:")
    print(f"   📈 Relevance: {data['relevance_score']:.1f}%")
    print(f"   🔍 Discovery Potential: {data['discovery_potential']} new topics")
    print(f"   🤝 Shared Interests: {data['shared_interests']}")
    if data['new_content']:
        print(f"   🆕 New Content: {list(data['new_content'])}")


print(f"\n" + "="*33)
print("     🎉 PROJECT COMPLETE 🎉")
print("="*33)