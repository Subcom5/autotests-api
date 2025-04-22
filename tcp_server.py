# socket — стандартная библиотека Python, позволяющая работать с TCP и UDP-сокетами
import socket


def server():
    """Функция, реализующая TCP - server"""

    # Создаем TCP-сокет
    # SOCK_STREAM — задаем тип сокета как TCP
    # AF_INET — используем IPv4
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем его к адресу и порту
    # localhost (127.0.0.1) означает, что сервер работает только на локальном компьютере
    server_address = ('localhost', 12345)
    # bind() связывает сокет с определенным IP-адресом и портом
    server_socket.bind(server_address)

    # Начинаем слушать входящие подключения (максимум 5 в очереди)
    # Если к серверу обратится более 5 клиентов одновременно, они будут ждать
    server_socket.listen(5)
    print("Сервер запущен и ждет подключений...")

    # Запускаем бесконечный цикл, чтобы сервер всегда ждал новые подключения
    # Сервер будет работать до ручного завершения (Ctrl + C)
    while True:
        # Принимаем соединение от клиента
        # accept() останавливает выполнение и ждет подключения клиента.
        # Возвращается новый сокет client_socket для общения с этим клиентом
        # client_address содержит IP и порт клиента
        client_socket, client_address = server_socket.accept()
        print(f"Подключение от {client_address}")

        # Получаем данные от клиента
        # recv(1024) ждет и получает данные от клиента, максимум 1024 байта
        # .decode() — преобразует байты в строку (обычно в UTF-8)
        data = client_socket.recv(1024).decode()
        print(f"Получено сообщение: {data}")

        # Отправляем ответ клиенту
        response = f"Сервер получил: {data}"
        # encode() — преобразует строку в байты, так как send() принимает только байты
        client_socket.send(response.encode())

        # Закрываем соединение с клиентом
        client_socket.close()

# Запуск TCP-сервера
if __name__ == '__main__':
    server()