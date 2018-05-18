#!usr/bin/env python3

import cgi

print("Content-type:text/html\n\n")
print("<title>Сумма</title>")
form = cgi.FieldStorage()
a = form.getlist("num")
sum = 0
if a:
    for i in range(len(a)-1):
        sum = sum + int(a[i])
        print(a[i], "+")
else:
	print("Введите числа")
sum = sum + int(a[-1])
print(a[-1], "=", sum)
