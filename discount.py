def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price, discount_amount
    else:
        return price, 0
    
p = float(input("Enter original price: "))
d = float(input("Enter the discount percetage: "))

final_price, discount = calculate_discount (p, d)

print(f"Pay: KES{final_price:.2f}, discount applied is: {discount:.2f}")