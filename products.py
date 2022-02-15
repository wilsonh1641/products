# 建立記帳城市專案(+二維清單)
# 清單內存清單 = 二維清單
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': # 逃出迴圈
		break
	price = input('請輸入商品價格: ') 
	#轉換型別
	prine = int(price)
	#p = [] # 內部小清單
	#p.append(name)
	#p.append(price)
	#p = [name, price]
	#products.append(p)

	products.append([name, price])
print(products)

products[0][0]

for p in products:
	print(p[0], '的價格是', p[1])


#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'

# 1. 字串可以做+跟*
# 2. 寫到檔案的程式碼
# 3. 改成存CSV格式
# 4. with解釋複習 open 之後自動close

with open('products.csv', 'w') as f:

	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')