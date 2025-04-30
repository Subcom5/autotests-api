"""
{
  "id": "string",
  "title": "string",
  "maxScore": 0,
  "minScore": 0,
  "description": "string",
  "previewFile": {
    "id": "string",
    "filename": "string",
    "directory": "string",
    "url": "https://example.com/"
  },
  "estimatedTime": "string",
  "createdByUser": {
    "id": "string",
    "email": "user@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
  }
}
"""
import uuid
from pydantic import BaseModel, Field, ConfigDict, EmailStr, HttpUrl, ValidationError, computed_field
from pydantic.alias_generators import to_camel

# Добавили модель FileSchema
class FileSchema(BaseModel):
    id: str = "test_id_1234"
    url: HttpUrl = "test@mail.com" # Используем HttpUrl вместо str
    filename: str = "test.png"
    directory: str = "./download"

# Добавили модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    # Создание динамического поля
    @computed_field
    def username(self) ->str:
        return f"{self.first_name} {self.last_name}"

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"

class CourseSchema(BaseModel):
    # alias_generator=to_camel автоматически превращает snake_case в camelCase
    # populate_by_name=True позволяет передавать как camelCase, так и snake_case без ошибок
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    # default_factory принимает функцию, которая вызывается при создании объекта.
    # В данном случае используется uuid.uuid4(), который генерирует уникальный идентификатор.
    # Каждый новый объект получает новый id, даже если его не передавать вручную
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    # Вложенный объект для файла-превью
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 week")
    # Вложенный объект для пользователя, создавшего курс
    created_by_user: UserSchema = Field(alias="createdByUser")

# Инициализируем модель CourseSchema через передачу аргументов
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    # Добавили инициализацию вложенной модели FileSchema
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses",
    ),
    estimatedTime="1 week",
    # Добавили инициализацию вложенной модели UserSchema
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alise"
    )
)
print('Course default model:', course_default_model)

# Инициализируем модель CourseSchema через распаковку словаря
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    # Добавили ключ previewFile
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    # Добавили ключ createdByUser
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)

# Инициализируем модель CourseSchema через JSON
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON model:', course_json_model)

# сериализуем Pydantic-модель в dict()
print(course_json_model.model_dump())
# model_dump(by_alias=True) Pydantic сам приводит имена полей в camelCase
print(course_json_model.model_dump(by_alias=True))   # Возвращаем camelCase

# сериализуем Pydantic-модель в json()
print(course_json_model.model_dump_json())
# model_dump(by_alias=True) Pydantic сам приводит имена полей в camelCase
print(course_json_model.model_dump_json(by_alias=True)) # Возвращаем camelCase

# Создадим объект модели без передачи параметров
file = FileSchema()
print("course: ", file)


# Инициализируем FileSchema c некорректным url
try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses",
    )
except ValidationError as error:
    print(error)
    print(error.errors())









