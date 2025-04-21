import asyncio
import  websockets
from websockets import ServerConnection

async def incoming_message_handler(websocket: ServerConnection):
    """Функция обработчик входящих сообщений от клиента"""
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        count = 0
        for _ in range(5):
            count += 1
            response = f"{count} Сообщение пользователя: {message}"
            await websocket.send(response)

async def main():
    """Функция создает и запускает websocket-сервер"""

    server = await websockets.serve(incoming_message_handler, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())



