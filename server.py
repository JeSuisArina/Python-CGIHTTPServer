#!usr/bin/env python3

# подключение необходимых библиотек
# веб-сервер,обработчик запросов
from http.server import HTTPServer, CGIHTTPRequestHandler

# отчеты об ошибках CGI
import cgitb
cgitb.enable()

# создание сервера и обработчика запросов
server = HTTPServer
handler = CGIHTTPRequestHandler

# определение адреса для сервера
# "" = localhost
# 8000 = порт
server_address = ("", 8000)

# создание сервера с передачей ему адреса сервера, номера порта и обработчика
httpd = server(server_address, handler)

# помещение программы в бесконечный цикл
# чтобы сервер работал, пока я его не остановлю (Ctrl+C)
httpd.serve_forever()
