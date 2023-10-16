budget = int(input())
prices = 0
while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    current_price = float(command)
    if prices + current_price > budget:
        print("You went in overdraft!")
        break
    prices += current_price
