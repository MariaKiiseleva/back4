from product_management import process_order
from order_processing import process_order_with_finally
from multi_exception_handling import handle_multiple_exceptions
from exception_generation import generate_order


def run_all_functions():
    print("Running all functions...")

    # Шаг 1: Производство товаров
    print("\nProduct Management:")
    process_order("Gold Ring", 15)
    process_order("Diamond Necklace", 5)
    process_order("Silver Bracelet", 20)

    # Шаг 2: Обработка заказов с блоком finally
    print("\nOrder Processing with Finally Block:")
    process_order_with_finally("Gold Ring", 5)
    process_order_with_finally("Diamond Necklace with error", 10)

    # Шаг 3: Обработка нескольких типов исключений
    print("\nMulti-Exception Handling:")
    handle_multiple_exceptions("Gold Ring", 15, 150)
    handle_multiple_exceptions("Diamond Necklace", 5, 50)
    handle_multiple_exceptions("Silver Bracelet", 20, 80)

    # Шаг 4: Генерация исключений и их обработка
    print("\nException Generation:")
    generate_order("Gold Ring", 5)
    generate_order("Diamond Necklace", 10)
    generate_order("error", 15)

    # Шаг 5: Обработка всех возможных исключений
    print("\nHandling all exceptions:")
    generate_order("Silver Bracelet", 20)
    generate_order("Invalid Item", "invalid")
    generate_order("Non-numeric Quantity", "10")


if __name__ == "__main__":
    run_all_functions()
