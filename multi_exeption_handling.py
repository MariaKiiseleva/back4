# multi_exception_handling.py

from custom_exceptions import JewelryStoreException, InsufficientStockException, InvalidPriceException


def handle_multiple_exceptions(product_name, quantity, price):
    try:
        product = Product(product_name, price, 10)  # Пример цен и количества на складе
        total_cost = product.sell(quantity)

        if "error" in product_name.lower():
            raise InsufficientStockException("Simulated error in stock")

        if price < 100:
            raise InvalidPriceException("Price too low")

        return f"Order processed successfully. Total cost: ${total_cost}"
    except InsufficientStockException as e:
        print(f"Insufficient Stock Exception: {e}")
    except InvalidPriceException as e:
        print(f"Invalid Price Exception: {e}")
    except JewelryStoreException as e:
        print(f"Jewelry Store Error: {e}")


# Тестирование функции
print(handle_multiple_exceptions("Gold Ring", 15, 150))
print(handle_multiple_exceptions("Diamond Necklace", 5, 50))
print(handle_multiple_exceptions("Silver Bracelet", 20, 80))
