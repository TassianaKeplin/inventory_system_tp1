from services.inventory_service import inventory_snapshot, calculate_restock_qty_again

def print_inventory():
    data = inventory_snapshot()
    total = 0
    by_category = {}
    print("=== INVENTORY REPORT ===")

    for item in data:
        total = total + item["value"]

        if item["category"] not in by_category:
            by_category[item["category"]] = 0
        by_category[item["category"]] = by_category[item["category"]] + 1

        print("SKU:", item["sku"])
        print("Name:", item["name"])
        print("Category:", item["category"])
        print("Status:", item["status"])
        print("Value:", item["value"])
        print("Supplier:", item["supplier"])
        print("Risk:", item["risk"])
        print("Restock Qty:", item["restock_qty"])
        print("-----------------------")

    print("TOTAL VALUE:", total)
    print("BY CATEGORY:", by_category)

def restock_report():
    data = inventory_snapshot()
    result = []
    for item in data:
        if item["status"] in ["restock", "critical"]:
            result.append({
                "sku": item["sku"],
                "supplier": item["supplier"],
                "qty": item["restock_qty"]
            })
    return result

def supplier_summary():
    data = inventory_snapshot()
    summary = {}
    for item in data:
        if item["supplier"] not in summary:
            summary[item["supplier"]] = 0
        summary[item["supplier"]] = summary[item["supplier"]] + item["value"]
    return summary
