# 記帳小程式
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
    p = [name, price]
	products.append(p) #把小清單P放入大清單procucts
#	products.append([name, price])
print(products)
print(products[1])
print(products[0][1])