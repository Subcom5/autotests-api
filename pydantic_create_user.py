"""
UserSchema — модель данных пользователя
{
  "id": "string",
  "email": "user@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

CreateUserRequestSchema — запрос на создание пользователя
{
  "email": "user@example.com",
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

CreateUserResponseSchema — ответ с данными созданного пользователя
{
  "user": {
    "id": "string",
    "email": "user@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
  }
}
"""
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr, Field, constr


class UserSchema(BaseModel):
    """
    Модель данных пользователя

    Включает поля: id, email, last_name, first_name, middle_name
    """
    id: UUID = Field(default_factory=uuid4)
    email: EmailStr = Field(max_length=250)
    last_name: str = Field(alias="lastName", min_length=1, max_length=50)
    first_name: str = Field(alias="firstName", min_length=1, max_length=50)
    middle_name: str = Field(alias="middleName", min_length=1, max_length=50)

class CreateUserRequestSchema(BaseModel):
    """
    Модель создания пользователя

    Включает поля: email, password,  last_name, first_name, middle_name
    """
    email: EmailStr = Field(max_length=250)
    password: constr(min_length=1, max_length=250)
    last_name: str = Field(alias="lastName", min_length=1, max_length=50)
    first_name: str = Field(alias="firstName", min_length=1, max_length=50)
    middle_name: str = Field(alias="middleName", min_length=1, max_length=50)

class CreateUserResponseSchema(BaseModel):
    """
    Ответ на создание пользователя

    Включает поле: user
    """
    user: UserSchema


user = UserSchema(
    id="9a227569-0d7d-4cca-aeca-a4cce2747bee",
    email="test@example.com",
    lastName= "Alex",
    firstName="Artem",
    middleName="Ship"
)
response = CreateUserResponseSchema(user=user)
print(response.model_dump(by_alias=True))