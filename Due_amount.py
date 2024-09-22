def calculate(product, price, given):
    if product == "electronics" or product == "electronic":
        tax = 1.2
    elif product == "furniture" or product == "furnitures":
        tax = 1.5
    elif product == "food" or product == "foods":
        tax = 1.1
    elif product == "clothing" or product == "cloth":
        tax = 1.3
    else:
        tax = 1.1
    price = price * tax
    due_amount = given - price
    print(int(due_amount), "(includes tax)")
print("Categories:")
print("1. Electronics")
print("2. Furniture")
print("3. Food")
print("4. Clothing")
product = input("Enter product type: ").lower()
price = float(input("Enter price of item: "))
given = float(input("Enter money paid: "))
calculate(product, price, given)