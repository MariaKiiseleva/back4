from custom_exceptions import OrderProcessingError

def process_order_with_finally(product_name, quantity):
    try:
        # Имитация обработки заказа
        if "error" in product_name.lower():
            raise OrderProcessingError("Error occurred during order processing")
        return f"Order processed successfully for {product_name}"
    except OrderProcessingError as e:
        print(f"Error: {e}")
        # Логика обработки ошибки
        return f"Order failed: {str(e)}"
    finally:
        # Шаг 3: Блок finally для завершения работы функции
        print("Order processing completed")

# Тестирование функции
print(process_order_with_finally("Gold Ring", 5))
print(process_order_with_finally("Diamond Necklace with error", 10))
