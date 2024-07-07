# Get the charge for the food from the user
food_charge = float(input("Enter the charge for the food: "))

# Calculate the tip and tax
tip = food_charge * 0.18
tax = food_charge * 0.07

# Calculate the total amount
total = food_charge + tip + tax

# Display the amounts
print(f"Food Charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${tax:.2f}")
print(f"Total Amount: ${total:.2f}")
