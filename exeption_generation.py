class OrderGenerationError(Exception):
    """Вызывается при ошибке генерации заказа"""
    pass

def generate_order(item, quantity):
    # Шаг 5: Генерация исключения при некорректном элементе
    if item == "error":
        raise OrderGenerationError("Simulated order generation error")
    else:
        return f"Generated order for {item}"

try:
    print(generate_order("Gold Ring", 5))
    print(generate_order("Diamond Necklace", 10))
    print(generate_order("error", 15))
except OrderGenerationError as e:
    print(f"Error: {e}")
finally:
    print("Order generation completed")

# Обработка всех возможных исключений
try:
    print(generate_order("Silver Bracelet", 20))
except (ValueError, TypeError, OrderGenerationError) as e:
    print(f"All exceptions caught: {e}")
finally:
    # Шаг 5: Блок finally для завершения работы функции
    print("All operations completed")
