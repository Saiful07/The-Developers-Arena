# Personal Information Manager
# Authoe : Saiful Islam
# Displays Perosnal Information

# Welcome message
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# Store static information
name = "Saiful Islam"
age = 23
city = "Meghahatuburu"
hobby = "Playing Volleyball"

# Get user input
print()
print("Please tell me about yourself:")
print("-" * 30)

favorite_food = input("What is your favorite food? ").strip()
while favorite_food == "":
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite color? ").strip()

favorite_color = input("What's your favorite color? ").strip()
while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ").strip()

# Calculate age in months
age_in_months = age * 12

# Display all information
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print()

# Goodbye message
print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)