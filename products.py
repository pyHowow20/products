# 記帳小程式
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ') #取得price是字串
	products.append([name, price]) #把小清單P放入大清單procucts
print(products)

for p in products:
	print(p[0], '的價格是 ', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n') # 欄位名稱
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #字串可以+合併