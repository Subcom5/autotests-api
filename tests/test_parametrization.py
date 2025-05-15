import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize("number", [2, 1, 4, -1])
def test_number(number: int):
    assert number > 0


@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_number(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com",
])
def test_multiplication_of_numbers(os: str, host: str):
    assert len(os + host) > 0


# Параметризация фикстур

@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
# Фикстура будет возвращать три разных хоста
# Соотвественно все автотесты использующие данную фикстуру будут запускаться три раза
def host(request: SubRequest) -> str:
    # Внутри атрибута param находится одно из значений "https://dev.company.com",
    # "https://stable.company.com", "https://prod.company.com"
    return request.param

# В самом автотесте уже не нужно добавлять параметризацию, он будет автоматически параметризован из фикстуры
def test_host(host: str):
    # Используем фикстуру в автотесте, она вернет нам хост в виде строки
    print(f"Running test on host: {host}")


# Параметризация классов

# Для тестовых классов параметризация указывается для самого класса
@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    # Параметр "user" передается в качестве аргумента в каждый тестовый метод класса
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    # Аналогично тут передается "user"
    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")




@pytest.mark.parametrize(
    "phone_number",
    ["+79317894561", "+79524567895", "+79561475289"],
    # ids используется для задания читаемых имён параметров теста, которые отображаются в выводе
    # Pytest, когда выполняются тесты
    ids=[
        "User with money on bank account",
        "User without money on bank account",
        "User with operation on bank account"
    ]
)
def test_identifiers(phone_number: str):
    pass

# Делаем вывод более читаемым за счет вывода параметров и их имен
users = {
    "79317894561": "User with money on bank account",
    "79524567895": "User without money on bank account",
    "79561475289": "User with operation on bank account",
}

@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers2(phone_number: str):
    pass