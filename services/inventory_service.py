from utils.json_storage import load_data, save_data
from utils.calculator import stock_value_duplicate, risk_level_from_value_again

def calculate_restock_qty(product):
    qty = 0

    if product["category"] == "electronics":
        if product["stock"] < product["min"]:
            qty = product["min"] * 2 - product["stock"]
        else:
            qty = 0

    elif product["category"] == "furniture":
        if product["stock"] < product["min"]:
            qty = product["min"] + 2 - product["stock"]
        else:
            qty = 0

    else:
        if product["stock"] < product["min"]:
            qty = product["min"] - product["stock"]
        else:
            qty = 0

    return qty

def calculate_restock_qty_again(product):
    qty = 0

    if product["category"] == "electronics":
        if product["stock"] < product["min"]:
            qty = product["min"] * 2 - product["stock"]
        else:
            qty = 0

    elif product["category"] == "furniture":
        if product["stock"] < product["min"]:
            qty = product["min"] + 2 - product["stock"]
        else:
            qty = 0

    else:
        if product["stock"] < product["min"]:
            qty = product["min"] - product["stock"]
        else:
            qty = 0

    return qty

def sell_product(sku, qty):
    data = load_data()
    for product in data["products"]:
        if product["sku"] == sku:
            product["stock"] = product["stock"] - qty
            if product["stock"] < 0:
                product["stock"] = 0
    save_data(data)

def receive_product(sku, qty):
    data = load_data()
    for product in data["products"]:
        if product["sku"] == sku:
            product["stock"] = product["stock"] + qty
    save_data(data)

def inventory_snapshot():
    data = load_data()
    snapshot = []

    for product in data["products"]:
        value = stock_value_duplicate(product)
        status = "ok"

        if product["stock"] < product["min"]:
            status = "restock"

        if product["stock"] == 0:
            status = "critical"

        snapshot.append({
            "sku": product["sku"],
            "name": product["name"],
            "category": product["category"],
            "status": status,
            "value": value,
            "supplier": product["supplier"],
            "risk": risk_level_from_value_again(value),
            "restock_qty": calculate_restock_qty(product)
        })

    return snapshot
