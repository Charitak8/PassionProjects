import random

restaurants = ["Italian", "Mexican", "Chinese", "Pizza", "Burger"]

print("Choose your preferences:")
prefer_italian = input("Do you prefer Italian? (yes/no): ").lower() == "yes"
prefer_mexican = input("Do you prefer Mexican? (yes/no): ").lower() == "yes"
prefer_chinese = input("Do you prefer Chinese? (yes/no): ").lower() == "yes"
prefer_pizza = input("Do you prefer Pizza? (yes/no): ").lower() == "yes"
prefer_burger = input("Do you prefer Burger? (yes/no): ").lower() == "yes"

filtered_restaurants = []

if prefer_italian:
    filtered_restaurants.append("Italian")
if prefer_mexican:
    filtered_restaurants.append("Mexican")
if prefer_chinese:
    filtered_restaurants.append("Chinese")
if prefer_pizza:
    filtered_restaurants.append("Pizza")
if prefer_burger:
    filtered_restaurants.append("Burger")

if not filtered_restaurants:
    print("You didn't select any preferences. Choosing a random restaurant.")
    chosen_restaurant = random.choice(restaurants)
else:
    print("Choosing a restaurant based on your preferences.")
    chosen_restaurant = random.choice(filtered_restaurants)

print("Today's lunch destination: " + chosen_restaurant)