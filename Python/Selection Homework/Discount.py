purchase_amount = float(input("Purchase amount: £"))
if purchase_amount >= 100:
    discount = 0.1 * purchase_amount  # 10% discount
    final_amount = purchase_amount - discount
    print("Congratulations! You have a 10% discount.") 
    print(f"Final amount: £{final_amount:.2f}")
else:
    print("Sorry, no discount applies to this purchase.")
