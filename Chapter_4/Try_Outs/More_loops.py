my_foods = ['pizza', 'falafel', 'carrot cake']

# Create a copy of the list
friend_foods = my_foods[:]

# Add a new food to each list to show they are separate
my_foods.append('cannoli')
friend_foods.append('ice cream')

# Loop through the first list
print("My favorite foods are:")
for food in my_foods:
    print(f"- {food.title()}")

# Loop through the second list
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food.title()}")