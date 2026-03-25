Sites = ["Ethiopia", "Carthage", "Zanzibar", "Cape Town", "Sinai"]
print(Sites)

# List in alphabetical order
print(sorted(Sites))

# List in original order
print(Sites)

#List in reverse alphabetical order
print("\nReverse-Alphabetical (sorted) :", sorted(Sites, reverse= True))

# Original order still intact
print("Original order still exists:", Sites)

# Permanent. It flips the list backwards.
Sites.reverse()
print("\nList after first reverse():", Sites)

# Reverse again to get back to the start
Sites.reverse()
print("List back to original after second reverse():", Sites)

# Using sort() (Alphabetical)
# Permanent
Sites.sort()
print("\nAlphabetical (sort):", Sites)

# Using sort() (Reverse-Alphabetical)
# Permanent.
Sites.sort(reverse=True)
print("Reverse-alphabetical (sort):", Sites)
