#!C:/Users/Арина/AppData/Local/Programs/Python/Python37/python

print("Content-type:text/html\n\n")
print('<title>Сумма</title>')
def a(numb):
	
   if len(numb) == 1:
        return numb[0]
   else:
        return numb[0] + a(numb[1:])

print(a([4, 8, 15, 16, 23, 42]))