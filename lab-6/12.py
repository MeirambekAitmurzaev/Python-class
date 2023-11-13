try:
    def sort_by_price(shopping_list):
        sorted_list = sorted(shopping_list, key=lambda item: item["price"])
        return sorted_list

    # Example usage:
    shopping_list = [
        {"name": "Apple", "price": 100},
        {"name": "Banana", "price": 50},
        {"name": "Orange", "price": 20}
    ]

    sorted_shopping_list = sort_by_price(shopping_list)
    print(sorted_shopping_list)
except ValueError as e:
        print("Invalid input.")