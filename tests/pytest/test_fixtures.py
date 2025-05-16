# import pytest
#
# ####### Определение фикстуры
# @pytest.fixture
# def sample_fixture():
#     return {"key": "value"}
#
# # Использование фикстуры в тесте
# def test_using_fixture(sample_fixture):
#     assert sample_fixture["key"] == "value"
#
# ##### Подготовка данных
# @pytest.fixture
# def user_data():
#     return {"username": "test_user", "email": "test@example.com"}
#
# def test_user_email(user_data):
#     assert user_data["email"] == "test@example.com"
#
# def test_user_username(user_data):
#     assert user_data["username"] == "test_user"
#
#  # Инициализация ресурсов
# @pytest.fixture
# def users_client():
#     client = new_users_client()  # Создаем новый API клиент (setup)
#     yield client
#     client.close()  # Закрываем сетевое соедниение (teardown)
#
#
# def test_create_user(users_client):  # Внутри автотеста уже работает с готовым объектом API клиента
#     users_client.create_user()
#
# # Фоновые действия
# @pytest.fixture(autouse=True)
# def send_analytics_data():
#     print("Данная фикстура будет запущена автоматически перед каждым автотестом")
#
#
# def test_1():  # При этом такую фикстуру не нужно передавать в тест
#     pass
#
#
# def test_2():
#     pass
#
#
# def test_3():
#     pass
#
#
# # Уровни фикстур
# @pytest.fixture(scope="function")
# def function_users_client():
#     print("Данная фикстура будет запущена на каждый автотест")
#
# @pytest.fixture(scope="class")
# def class_users_client():
#     print("Данная фикстура будет запущена на каждый тестовый класс")
#
# @pytest.fixture(scope="module")
# def module_users_client():
#     print("Данная фикстура будет запущена на каждый модуль python")
#
# @pytest.fixture(scope="session")
# def session_users_client():
#     print("Данная фикстура будет запущена один раз на всю тестовую сессию")
#
# # Использование yield для teardown
# @pytest.fixture
# def setup_and_teardown():
#     # Подготовка — данный код будет выполнен до начала автотеста
#     resource = "some resource"
#     yield resource # Выполняется автотест
#     # Очистка — данный код будет выполнен полсе завершения автотеста
#     print("Teardown: освобождение ресурса")
#
# # Фикстуры с зависимостями
# @pytest.fixture
# def settings(): # Инициализируем фикстуру с настройками
#     return new_settings()
#
# @pytest.fixture
# def users_client(settings): # Передаем фикстуру settings
#     return new_users_client(settings.host)
#
# def test_create_user(users_client):
#     users_client.create_user()
