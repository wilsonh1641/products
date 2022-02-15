products = []

# 增加讀取檔案程式碼
# 用.split(',')來用逗點做分割
# 用.strip()來除掉換行符號
# spilt完會變清單
# 把讀到的內容裝進清單

# continue教學
# continue通常寫在迴圈很高的位置

with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

# 建立記帳城市專案(+二維清單)
# 清單內存清單 = 二維清單
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

# 加入程式碼寫欄位
# 解決亂碼問題(編碼encoding)


with open('products.csv', 'w', encoding = 'utf-8') as f:

	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')