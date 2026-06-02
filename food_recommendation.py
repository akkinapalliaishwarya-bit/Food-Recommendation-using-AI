foods = [
    {"name": "Biryani", "type": "Non-Veg", "taste": "Spicy"},
    {"name": "Paneer Butter Masala", "type": "Veg", "taste": "Spicy"},
    {"name": "Ice Cream", "type": "Veg", "taste": "Sweet"},
    {"name": "Chicken Curry", "type": "Non-Veg", "taste": "Spicy"},
    {"name": "Gulab Jamun", "type": "Veg", "taste": "Sweet"},
    {"name": "Fried Rice", "type": "Veg", "taste": "Spicy"}
]

food_type = input("Enter type (Veg/Non-Veg): ")
taste = input("Enter taste (Spicy/Sweet): ")

recommendations = []

for food in foods:
    if food["type"].lower() == food_type.lower() and food["taste"].lower() == taste.lower():
        recommendations.append(food["name"])

if recommendations:
    print("\nRecommended Food Items:")
    for item in recommendations:
        print(item)
else:
    print("No matching food found.")