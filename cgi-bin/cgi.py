#!C:/Users/Арина/AppData/Local/Programs/Python/Python37/python

print("Content-type:text/html\n\n")
print('<title>Сумма</title>')
a = [4, 8, 15, 16, 23, 42]
for i in range(len(a)-1):
	print(a[i], '+')
print(a[-1], '=', sum(a))  