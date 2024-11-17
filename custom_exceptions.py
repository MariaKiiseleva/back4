class JewelryStoreException(Exception):
    """Базовое пользовательское исключение для ювелирного магазина"""
    pass

class InsufficientStockException(JewelryStoreException):
    """Вызывается, когда товара недостаточно на складе"""
    pass

class InvalidPriceException(JewelryStoreException):
    """Вызывается при некорректной цене товара"""
    pass

class OrderProcessingError(JewelryStoreException):
    """Ошибка при обработке заказа"""
    pass
