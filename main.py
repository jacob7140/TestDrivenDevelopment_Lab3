from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = input('What is your product: ')
    unit_price = Invoice().inputNumber("Please enter a unit price: ")
    qnt = Invoice().inputNumber("Please enter quantity of the product: ")
    discount = Invoice().inputNumber("Discount percent (%): ")
    tax = Invoice().inputNumber("Tax rate (%): ")
    repeat = Invoice().inputAnswer("Another product (y,n): ")
    result = Invoice().addProduct(qnt, unit_price, discount, tax)
    products[product] = result
    if repeat == "n":
        break

total_amount = Invoice().totalTaxPurePrice(products)

print("Your total pure price is: ", total_amount)
