Guets = ["Amo", "Craig", "Sammy", "Jake", "Preach", "Donald"]
print(f"Heyy there {(Guets[0])}! Hope you're having a great day and I wanted to let you know that you're invited to dinner with me.")
print(f"Whats up {(Guets[1])}! Just wanted to invite you over to dinner at my place.")
print(f"Greetings my friend {(Guets[2])}. Hope everything is well there. This is an invite to dinner with me")
print(f"What's good {(Guets[3])}! You're invited to a special dinner with me on Friday")
print(f"Heyy {(Guets[4])}! Hope you're well my man and this is just to invite you to a nice dinner with me on Friday")
print(f"Whats up {(Guets[5])}! Just wanted to invite you over to dinner at my place.")

# 3.5: Changing Guest List
# Sammy can't make it
cant_make_it = "Sammy"
print(f"\nRegrettably, {cant_make_it} can't make it to dinner.")

# Replacing Sammy with a new guest, "Thabo"
Guets[2] = "Thabo"

# Re-inviting everyone
print("\n--- Updated Invitations ---")
for guest in Guets:
    print(f"Hey {guest}, you're still invited to dinner!")

# --- 3-6: More Guests (Bigger Table) ---
print("\nGreat news! I found a bigger table, so more friends are coming.")

Guets.insert(0, "Lesedi")      # Add to start
Guets.insert(3, "Neo")         # Add to middle
Guets.append("Zoe")            # Add to end

print("\n--- Larger Party Invitations ---")
for guest in Guets:
    print(f"What's up {guest}! I found a bigger table, come join us!")

# --- 3-7: Shrinking Guest List ---
print("\nOh no! The table won't arrive in time. I can only invite two people.")

# Use pop() until only 2 guests remain
# We use a while loop to keep popping until the list length is 2
while len(Guets) > 2:
    removed_person = Guets.pop()
    print(f"Sorry {removed_person}, I can't invite you to dinner this time.")

# Tell the final two they are still in
print(f"\n{Guets[0]}, you're still invited!")
print(f"{Guets[1]}, you're still invited!")

# Use del to empty the list
del Guets[1]
del Guets[0]

# Check if it's empty
print("\nFinal Guest List check:", Guets)