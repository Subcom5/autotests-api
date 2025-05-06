from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema
from clients.users.users_schema import GetUserResponseSchema
from tools.fakers import fake
from tools.assertions.schema import validate_json_schema


# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
# Инициализируем клиент PrivateUsersClient
private_users_client = get_private_users_client(authentication_user)

# Отправляем GET запрос на получение данных пользователя
get_user_response = private_users_client.get_user_api(create_user_response.user.id)
# Получаем JSON-схему из Pydantic-модели ответа
get_user_response_schema = GetUserResponseSchema.model_json_schema()

print(get_user_response.json(), "\n")
print(get_user_response_schema)

# Проверяем, что JSON-ответ от API соответствует ожидаемой JSON-схеме
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)

