pocket_money = 40.00
while pocket_money > 0:
    price = float(input("how much do you want to spend on this item"))
    pocket_money -= price
    print("you have ${.:2f}" .format(pocket_money))
