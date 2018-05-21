#!usr/bin/env python3

import cgi

print("Content-type:text/html\n\n")
print("<title>Калькулятор</title>")
form = cgi.FieldStorage()
a = form.getlist("num")
operation = form.getvalue("operator")
result = 0
if a and operation:
	if operation == "+":
		for i in range(len(a)-1):
			result = result + int(a[i])
			print(a[i], "+")
		result = result + int(a[-1])
		print(a[-1], "=", result)
	elif operation == "-":
		z = a[0]
		for i in range(len(a)-2):
			result = int(z) - int(a[i + 1])
			z = result
		for i in range(len(a)-1):
			print(a[i], "-")
		result = result - int(a[-1])
		print(a[-1], "=", result)
	elif operation == "*":
		result = 1;
		for i in range(len(a)-1):
			result = result * int(a[i])
			print(a[i], "*")
		result = result * int(a[-1])
		print(a[-1], "=", result)
	elif operation == "/":
		z = a[0]
		for i in range(len(a)-2):
			result = int(z) / int(a[i + 1])
			z = result
		for i in range(len(a)-1):
			print(a[i], "/")
		result = result / int(a[-1])
		print(a[-1], "=", result)
	else:
		print("Введите оператор +, -, * или /")	
else:
	print("Введите числа или оператор")

