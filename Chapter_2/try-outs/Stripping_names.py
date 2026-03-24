# Store the name with a tab (\t) and a newline (\n)
name = "\t  Albert Einstein  \n"

# Print the name once to show the whitespace
print("Original:")
print(f"'{name}'")

# Print the name using each of the three stripping functions
print("\nUsing lstrip() (removes left space):")
print(f"'{name.lstrip()}'")

print("\nUsing rstrip() (removes right space):")
print(f"'{name.rstrip()}'")

print("\nUsing strip() (removes all outer space):")
print(f"'{name.strip()}'")