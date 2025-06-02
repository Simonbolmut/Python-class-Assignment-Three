def calculate_discount(price, discount_percent):
    # Only apply the discount if it's 20% or more
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, no discount applied
        return price

# Get user input for price and discount
try:
    price_input = input("Enter the original price of the item: ")
    discount_input = input("Enter the discount percentage: ")

    # Convert inputs to float
    original_price = float(price_input)
    discount_percent = float(discount_input)

    # Calculate final price using the function
    final_price = calculate_discount(original_price, discount_percent)

    # Display the result to the user
    if discount_percent >= 20:
        print(f"Discount applied! The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${original_price:.2f}")

except ValueError:
    print("Oops! Please enter valid numbers for price and discount.")
