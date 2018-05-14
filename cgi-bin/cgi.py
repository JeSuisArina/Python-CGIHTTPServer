#!C:/Users/Арина/AppData/Local/Programs/Python/Python37/python

import cgi

print("Content-type:text/html\n\n")
print('<title>Сумма</title>')
form = cgi.FieldStorage()
a = form.getlist('num')
if a:
	for i in range(len(a)-1):
		print(a[i], '+')
	print(a[-1], '=', sum(a))  
else: print("Введите числа")
