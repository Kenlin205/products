products = []
# List all buying items.
with open("products.csv","r",encoding = "utf-8") as f:
	for line in f:
		if "item,price" in line:
			continue
		name, price = line.strip().split(",")
		products.append([name, price])
print(products)

# User input 
while True:
	name = input("Please enter item name: ")
	if name == "q":
		break
	price = input("Please enter item price: ")
	price = int(price)
	products.append([name, price])
print(products)

# Print all buying record.
for p in products:
	print(p[0],"price is ",p[1])
# recode to csv files.
with open("products.csv", "w", encoding = "utf-8") as f:
	f.write("item,price\n")
	for p in products:
		f.write(p[0] + "," + str(p[1]) + "\n")
