#!C:/Users/Арина/AppData/Local/Programs/Python/Python37/python

print("Content-type:text/html\n\n")
print('<title>Сумма</title>')
a = []
if a:
	for i in range(len(a)-1):
		print(a[i], '+')
	print(a[-1], '=', sum(a))  
else: print("Введите числа")