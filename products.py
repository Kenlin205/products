products = []
while True:
	name = input("Please enter item name: ")
	if name == "q":
		break
	price = input("Please enter item price: ")
	products.append([name,price])
print(products)
