MENU_ITEMS = [
    ("Americano", 99),
    ("Spanish Latte", 129),
    ("Cold Brew Malt", 189),
    ("Affogato", 159),
    ("Caramel Macchiato", 129),
]
VAT_RATE = 0.12


def generate_sku():
    category = input("Category: ").strip()
    product_name = input("Product name: ").strip()

    while not product_name:
        print("Product name cannot be blank.")
        product_name = input("Product name: ").strip()

    while True:
        try:
            stock_qty = int(input("Stock quantity: ").strip())
            if stock_qty > 0:
                break
            print("Enter a positive whole number.")
        except ValueError:
            print("Enter a positive whole number.")

    category_code = category[:3].upper()
    product_code = "".join(product_name.split())[:4].upper()
    sku = f"{category_code}-{product_code}-{stock_qty:03d}"
    print(f"SKU: {sku}")


def create_order():
    print("\nMenu:")
    for number, (name, price) in enumerate(MENU_ITEMS, start=1):
        print(f"{number}. {name} - PHP {price}")

    while True:
        selection = input("Enter item numbers separated by commas: ").strip()
        try:
            selected_numbers = sorted({int(value.strip()) for value in selection.split(",")})
            if not selected_numbers or any(
                number < 1 or number > len(MENU_ITEMS)
                for number in selected_numbers
            ):
                raise ValueError
            break
        except ValueError:
            print(f"Choose one or more numbers from 1 to {len(MENU_ITEMS)}.")

    selected_items = [MENU_ITEMS[number - 1] for number in selected_numbers]
    subtotal = sum(price for _, price in selected_items)
    tax = subtotal * VAT_RATE
    total = subtotal + tax

    print("\n==== Receipt ====")
    for name, price in selected_items:
        print(f"{name}: PHP {price:.2f}")
    print(f"Subtotal: PHP {subtotal:.2f}")
    print(f"VAT (12%): PHP {tax:.2f}")
    print(f"Total: PHP {total:.2f}")


def main():
    generate_sku()
    create_order()


if __name__ == "__main__":
    main()