from client import BinanceClient

def main():
    client = BinanceClient()

    print("=== Simple Trading Bot ===")

    symbol = input("Enter Symbol (e.g. BTCUSDT): ").upper()
    side = input("Enter Side (BUY/SELL): ").upper()
    order_type = input("Order Type (MARKET/LIMIT): ").upper()
    quantity = input("Enter Quantity: ")

    price = None
    if order_type == "LIMIT":
        price = input("Enter Price: ")

    print("\nPlacing Order...")

    # ✅ Place Order
    response = client.place_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price
    )

    print("\n=== Order Response ===")
    print(response)

    # ✅ Get Updated Status
    if "orderId" in response:
        order_id = response["orderId"]

        status = client.get_order(symbol, order_id)

        print("\n=== Updated Order Status ===")
        print("Status:", status.get("status"))
        print("Executed Qty:", status.get("executedQty"))
        print("Avg Price:", status.get("avgPrice"))

    else:
        print("❌ Order failed")

if __name__ == "__main__":
    main()