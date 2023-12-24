# list1=[]
# list2=[]

# while True:
#     numbers = int(input("Въведете числа "))
#     if numbers == 0:
#         break
#     if numbers % 3 == 0 and numbers % 2 == 0:
#         list1.append(numbers)
#     if numbers % 7 ==0 and numbers % 2 != 0:
#         list2.append(numbers)

# sum_list1 = sum(list1[2::2])
# print ("Сумата на четните елементи в първата листа е равна на ", sum_list1)

# sortedlist2 = sorted(list2, reverse=True)
# product_list2 = list2[0] * list2[-1]
# print ("Произвведението на най-голямото и най-малкото число е равно на ", product_list2)


class Product:
    def __init__(self, manufacturer, product_code, price_per1, amount):
        self.manufacturer = manufacturer
        self.product_code = product_code
        self.price_per1 = price_per1
        self.amount = amount

all_products = {
    "4a": Product("Xiaomi", "4a", 50, 0),
    "4c": Product("Xiaomi", "4c", 60, 0),
    "ac1200": Product("TP-Link", "ac1200", 30, 0),
    "ac1900": Product("TP-Link", "ac1900", 40, 0),
}

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product, amount):
        product.amount = amount
        self.products.append((product, amount))        

cart = ShoppingCart()

buy_options = input("Hello! Would you like to buy a new product? YES/NO ").lower()
if buy_options == "yes":
    while True:
        product_code = input(f"Here is our selection.\n Xiaomi 4a \n Xiaomi 4c \n TP-Link ac1200 \n TP-Link ac1900 \nBy writing the product code you are choosing to add it to your basket. ").lower()
        if product_code in all_products:
            quantity = int(input("What quantity do you want "))
            if quantity > 0:
                cart.add_product(all_products[product_code], quantity)
            else:
                print("Invalid quantity. Quantity must be greater than 0.")
        else:
            print("Invalid product code. Try again")

        continue_option = input("Would you like to add another product? YES/NO ").lower()
        if continue_option != "yes":
            break

    total_price = sum(product[0].price_per1 * product[1] for product in cart.products)
    total_price_with_vat = total_price * 1.2
    delivery_cost = 5
    final_price = total_price_with_vat + delivery_cost

    print("Thank you for shopping with us! Your order: ")
    for product, amount in cart.products:
        print(f"{product.manufacturer} - {product.product_code} - Quantity: {amount} - Price: {product.price_per1}")

    print(f"Total Price: {final_price}")

else:
    print("Thank you! See you next time.")