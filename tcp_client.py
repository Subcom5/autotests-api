# socket — стандартная библиотека Python, позволяющая работать с TCP и UDP-сокетами.
import socket

# Создаем TCP-сокет
# AF_INET — используем IPv4
# SOCK_STREAM — используем TCP (потоковый протокол)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
# server_address = ('localhost', 12345) — указываем IP-адрес и порт сервера
server_address = ('localhost', 12345)
# connect(server_address) — устанавливаем TCP-соединение с сервером
# Если сервер не запущен, клиент получит ошибку
client_socket.connect(server_address)

# Отправляем сообщение серверу
message = "Привет, сервер!"
# .encode() — преобразует строку в байты, так как send() принимает только байты
# client_socket.send() — отправляет данные по TCP-соединению
client_socket.send(message.encode())

# Получаем ответ от сервера
# recv(1024) — получает максимум 1024 байта данных от сервера
# .decode() — преобразует байты в строку (обычно UTF-8)
response = client_socket.recv(1024).decode()
print(f"Ответ от сервера: {response}")

# Закрываем соединение
client_socket.close()