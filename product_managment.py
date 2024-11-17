from custom_exceptions import JewelryStoreException, InsufficientStockException, InvalidPriceException


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        # Шаг 1: Выбрасываем исключение при недостаточном количестве товара
        if quantity > self.stock:
            raise InsufficientStockException(f"Not enough {self.name} in stock.")

        # Шаг 1: Выбрасываем исключение при некорректной квантиティ
        elif quantity <= 0:
            raise ValueError("Invalid quantity. Must be positive integer.")

        # Шаг 1: Возвращаем общую сумму продажи
        else:
            return quantity * self.price

    def set_price(self, new_price):
        # Шаг 1: Выбрасываем исключение при некорректной цене
        if new_price <= 0:
            raise InvalidPriceException("Price must be positive number.")
        else:
            self.price = new_price


def process_order(product_name, quantity):
    try:
        product = Product(product_name, 100, 10)  # Пример цен и количества на складе
        total_cost = product.sell(quantity)
        print(f"Order processed successfully. Total cost: ${total_cost}")
    except InsufficientStockException as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except JewelryStoreException as e:
        print(f"Jewelry Store Error: {e}")


# Тестирование функций
process_order("Gold Ring", 15)
process_order("Diamond Necklace", 5)
process_order("Silver Bracelet", 20)
