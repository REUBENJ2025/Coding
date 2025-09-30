purchase_amount = float(input("Purchase amount: £"))
if purchase_amount >= 130:
    discount = 0.2 * purchase_amount  # 20% discount
    final_amount = purchase_amount - discount
    print("Congratulations! You have a 20% discount.") 
    print(f"Final amount: £{final_amount:.2f}")
    next
if purchase_amount > 100:
    discount =+ 5  # Additional £5 discount
    final_amount = final_amount - discount
    print(f"fYou get £5 off for spending over £100, your final amount is: £{final_amount:.2f}")
elif purchase_amount > 80:
    discount = 0.05 * purchase_amount  # 5% discount
    final_amount = purchase_amount - discount
    print(f"You get a 5% discount, your final amount is: £{final_amount:.2f}")
else:
    print("Sorry, no discount applies to this purchase.") #Prints no discount applied depending on input

