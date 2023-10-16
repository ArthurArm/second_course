placed_orders = int(input())
total = 0

for _ in range(placed_orders):
    per_capsule = float(input())
    days = int(input())
    caps_per_day = int(input())
    coffee = per_capsule * days * caps_per_day
    if per_capsule == 0.01-100.00:
        continue
    if days == 1-31:
        continue
    if caps_per_day == 1-2000:
        continue
    total += coffee
    print(f"The price for the coffee is: ${coffee:.2f}")


print(f"Total: ${total:.2f}")
