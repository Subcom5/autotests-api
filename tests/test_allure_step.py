import allure

# Использование контекстного менеджера with allure.step(...)

def test_feature1():
    with allure.step("Building API client"):
        ...  # Тут код инициализации API клиента

    with allure.step("Creating course"):
        ...  # Тут код создания курса

    with allure.step("Deleting course"):
        ...  # Тут код удаления курса


# Использование декоратора @allure.step

@allure.step("Building API client")
def build_api_client():
    ...


@allure.step("Creating course")
def create_course():
    ...


@allure.step("Deleting course")
def delete_course():
    ...


def test_feature2():
    build_api_client()
    create_course()
    delete_course()

# Пример использования вложенных шагов:

@allure.step("Building API client")
def build_api_client2():
    with allure.step("Get user authentication tokens"):
        ...

    with allure.step("Create new API client"):
        ...


def test_feature3():
    build_api_client()

# Использование шаблонов в шагах

@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    pass


def test_feature():
    create_course(title="Locust")
    create_course(title="Pytest")
    create_course(title="Python")
    create_course(title="Playwright")
