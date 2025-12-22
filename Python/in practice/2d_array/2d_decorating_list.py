purchases = [["Matt Pink Paint", "Decorating", 6.99],
             ["Floral Wallpaper", "Decorating", 7.99],
             ["Magnolia Gloss Paint", "Decorating", 5.49],
             ["Weed Killer", "Gardening", 2.99],
             ["Picture Frame", "Decorating", 8.99],
             ["Plug Socket", "Electrics", 6.99],
             ["Doorbell", "Electrics", 15.99],
             ["Matt White Paint", "Decorating", 4.99],
             ["Tiles", "Decorating", 19.99],
             ["Grass Seed", "Gardening", 1.99],
             ["Lawn Mower", "Gardening", 129.99]
             ]

total_price = 0
current_decorating_price = 0
total_decorating_price = 0
electronic_price = 0
total_gardening_price = 0

total_price = 0

for i in range(0, 11):
    if purchases[i][1] == "Decorating":
        current_decorating_price = current_decorating_price + purchases[i][2]
        print(f"{purchases[i][0]} £{purchases[i][2]}")
        total_decorating_price = total_decorating_price + purchases[i][2]

    if current_decorating_price >= 20 and purchases[i][1] == "Gardening":
        discount_price = purchases[i][2] * 0.1
        discount_price_out = round(discount_price, 2)
        print(f"{purchases[i][0]} £{purchases[i][2]}")
        print(f"-£{discount_price_out} discount")
        gardening_price = purchases[i][2] - discount_price
        total_gardening_price += gardening_price

    if purchases[i][1] == "Electrics":
        electronic_price = electronic_price + purchases[i][2]
        print(f"{purchases[i][0]} £{purchases[i][2]}")

total_price = total_decorating_price + total_gardening_price + electronic_price

print("\n-------------")

total_price = round(total_price, 2)
print(f"TOTAL: {total_price}")


