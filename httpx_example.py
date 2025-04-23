import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)
print(response.json())


data = {
    "title": "New issue",
    "completed": False,
    "userId": 1
}
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)
#print(response.request.headers)
print(response.json())

data = { "username": "test_user", "password": "123456"}
response = httpx.post("https://httpbin.org/post", data=data)

print(response.status_code)
#print(response.request.headers)
print(response.json())

headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.status_code)
print(response.request.headers)
print(response.json())

# response1 = httpx.get("https://jsonplaceholder.typicode.com/todos?userId=1") # вместо ?userId=1
params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.status_code)
print(response.url)
print(response.json())

files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.status_code)
print(response.json())

"""Использование httpx.Client"""

# Использование httpx.Client позволяет не устанавливать новое соединение для каждого запроса.
with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/1")

print(response1.json())
print(response2.json())

"""Добавление базовых заголовков в Client."""

# Чтобы передавать заголовки во всех запросах, можно задать их при создании Client

client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response = client.get("https://httpbin.org/get")
print(response.json())  # Заголовки включены в ответ
client.close()


"""Работа с ошибками
Проверка статуса ответа (raise_for_status)"""

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")


"""Обработка таймаутов"""

# Здесь, если сервер отвечает более 2 секунд, запрос прервется.
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")