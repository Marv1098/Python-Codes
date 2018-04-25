class ItemToPurchase:
    def __init__(self, item_name, item_price, item_quantity):
        self.__productname = item_name
        self.__price = item_price
        self.__quantity = item_quantity

    def get_productname(self):
        return self.__productname

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_item_cost(self):
        cost = self.__price * self.__quantity
        return cost


class Customer(ItemToPurchase):
    def __init__(self, customer_name, shopping_date):
        self.__customer_name = customer_name
        self.__shopping_date = shopping_date
        self.__shopping_cart = []

    def add_item(self, item):
        self.__shopping_cart.append(item)

    def remove_item(self, item_name):
        for item in self.__shopping_cart:
            if item.get_productname() == item_name:
                self.__shopping_cart.remove(item)
                print(item_name, 'has been removed')
            else:
                print('Item not in shopping cart')

    def get_total(self):
        total = 0
        for item in self.__shopping_cart:
            total = total + item.get_item_cost()
        return total

    def show_receipt(self):
        print('Checking Out')
        print('Customer Name:', self.__customer_name)
        print('Shopping Date:', self.__shopping_date)
        for item in self.__shopping_cart:
            print(item.get_quantity(), item.get_productname(),'@', item.get_price())

def main():

    customer = Customer('Mark', '12 November')
    number_of_items = int(input('Number of items you want to add: '))
    for index in range(number_of_items):
        item_name = input('Item Name: ')
        item_price = float(input('Item Price: '))
        item_quantity = int(input('Item Quantity: '))
        Item = ItemToPurchase(item_name, item_price, item_quantity)
        customer.add_item(Item)

    number_of_items = int(input('Number of items you want to remove: '))
    for index in range(number_of_items):
        item_name = input('Item name: ')
        customer.remove_item(item_name)
        print('\n')

    customer.show_receipt()
    print('Your Total is:$', customer.get_total())
main()