from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    id: str
    title: str = Field(min_length=1, max_length=250)
    max_sore: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str = Field(min_length=1)
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str | None = Field(alias="estimatedTime", min_length=1, max_length=50)
    created_by_user: UserSchema = Field(alias="createdByUser")


class GetCursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    user_id: str = Field(alias="userId")

class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(min_length=1, max_length=250)
    max_sore: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str = Field(min_length=1)
    estimated_time: str | None = Field(alias="estimatedTime", min_length=1, max_length=50)
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")

class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(min_length=1, max_length=250)
    max_sore: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str = Field(min_length=1)
    estimated_time: str | None = Field(alias="estimatedTime", min_length=1, max_length=50)
