# Get user input for the price and quantity
price_input = input("Enter the price of one item: ")
quantity_input = input("Enter the quantity you want: ")

# Convert the string inputs to appropriate data types
price = float(price_input)
quantity = int(quantity_input)

# Calculate the total cost
total = price * quantity

# Print a friendly summary using an f-string
print(f"{quantity} items at {price:.2f} each = {total:.2f}")