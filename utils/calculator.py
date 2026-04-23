from config import HIGH_VALUE_LIMIT, MEDIUM_VALUE_LIMIT

def stock_value(product):
    return product["stock"] * product["price"]

def risk_level_from_value(value):
    if value > HIGH_VALUE_LIMIT:
        return "high"
    elif value > MEDIUM_VALUE_LIMIT:
        return "medium"
    return "low"