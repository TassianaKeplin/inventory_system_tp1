def stock_value(product):
    return product["stock"] * product["price"]

def stock_value_duplicate(product):
    return product["stock"] * product["price"]

def risk_level_from_value(value):
    if value > 10000:
        return "high"
    elif value > 5000:
        return "medium"
    return "low"

def risk_level_from_value_again(value):
    if value > 10000:
        return "high"
    elif value > 5000:
        return "medium"
    return "low"
