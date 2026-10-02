class Item:
    def __init__(self, discount: float = None) -> None:
        self.__name: str = str(input("Item Name: "))
        self.__price: float = float(input("Item Price: "))
        
        if discount is not None:
            self.apply_discount(discount)
    
    def apply_discount(self, discount: float) -> None:
        discount: float = discount/100
        self.__price = self.__price - (self.__price * discount)

    def get_price(self) -> float:
        return self.__price

    def set_price(self, price: float) -> None:
        self.__price = price

    def __str__(self) -> str:
        return f"""
        Item Name: {self.__name}
        Item Price: {self.__price}
        """

class Store:
    def __init__(self, items: list[Item] | None, tax: float = None) -> None:
        if items is None:
            self.__items: list[Item] = []
        else:
            self.__items: list[Item] = items

        if tax is not None:
            self.apply_tax(5)

    def add_item(self, discount: float = None) -> None:
        self.__items.append(Item() if discount is None else Item(discount))
    
    def apply_tax(self, tax: float) -> None:
        for item in self.__items:
            tax = tax / 100
            item.set_price(item.get_price() - (item.get_price() * tax))
    
    def __str__(self) -> str:
        return "".join(str(item) for item in self.__items)

def main() -> None:
    items = [Item(10) for item in range(3)]
    print(Store(items, 5))

main()