my_pizzas = ["Pepperoni", "Margherita", "BBQ Chicken"]

# Create a true copy using a slice [:]
friend_pizzas = my_pizzas[:]

# Add a new pizza to the original list
my_pizzas.append("Meat Lovers")

# Add a different pizza to the friend's list
friend_pizzas.append("Vegetarian")

# Prove they are separate by looping through both
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")