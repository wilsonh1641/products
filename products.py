# 建立記帳城市專案(+二維清單)
# 清單內存清單 = 二維清單
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': # 逃出迴圈
		break
	price = input('請輸入商品價格: ') 

	#p = [] # 內部小清單
	#p.append(name)
	#p.append(price)
	#p = [name, price]
	#products.append(p)

	products.append([name, price])
print(products)

products[0][0]
