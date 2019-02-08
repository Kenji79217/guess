import random

r = random.randint(1, 100)
conut = 0
while True:
	conut += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('YA! 你猜中了! ')
		print('這是你猜的第', conut, '次')
		break
	elif num < r:
		print('在大一點~ ')
	elif num > r:
		print('在小一點~ ')
	print('這是你猜的第', conut, '次')