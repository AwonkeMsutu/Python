buffet_foods = ("Roast Beef", "Mashed Potatoes", "Green Beans", "Cornbread", "Fried Chicken")

# 2. Use a for loop to print each food
print("Original Menu:")
for food in buffet_foods:
    print(f"- {food}")

# 3. Try to modify an item (uncomment the line below to see the error)
# buffet_foods[0] = "Steak" 
# Python will throw a TypeError: 'tuple' object does not support item assignment.

# 4. The restaurant changes its menu (overwriting the entire tuple)
buffet_foods = ("Steak", "Mashed Potatoes", "Roasted Carrots", "Cornbread", "Fried Chicken")

# 5. Print the revised menu
print("\nRevised Menu:")
for food in buffet_foods:
    print(f" {food}")