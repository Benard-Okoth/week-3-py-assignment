#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

# Prompt the user to enter the original price and the discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage (20% or higher): "))

# calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# print the final price after applying the discount or the original price if no discount was applied
if final_price == original_price:
    print(f"No discount was applied. The original price is: {original_price}")
else:    
    print(f"The final price after applying the discount is: {final_price}") 


