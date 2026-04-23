from services.report_service import print_inventory, restock_report, supplier_summary
from services.inventory_service import sell_product, receive_product

def main():
    while True:
        print("1 - Print inventory")
        print("2 - Sell product")
        print("3 - Receive product")
        print("4 - Restock report")
        print("5 - Supplier summary")
        print("6 - Exit")

        op = input("Choose: ")

        if op == "1":
            print_inventory()
        elif op == "2":
            sku = input("SKU do produto: ")
            qty = int(input("Quantidade: "))
            sell_product(sku, qty)
            print("Venda registrada.")
        elif op == "3":
            sku = input("SKU do produto: ")
            qty = int(input("Quantidade: "))
            receive_product(sku, qty)
            print("Recebimento registrado.")
        elif op == "4":
            print("RESTOCK:", restock_report())
        elif op == "5":
            print("SUPPLIERS:", supplier_summary())
        elif op == "6":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
