from pydantic import BaseModel, Field, ConfigDict


class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str = Field(min_length=1, max_length=250)
    course_id: str = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex", default=0)
    description: str = Field(min_length=1)
    estimated_time: str | None = Field(alias="estimatedTime", min_length=1, max_length=50)

class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    course_id: str = Field(alias="courseId")

class GetExerciseQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение информации об упражнении.
    """
    exercise_id: str

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры списка упражнений.
    """
    exercises: list[ExerciseSchema]

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(min_length=1, max_length=250)
    course_id: str = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex", default=0)
    description: str = Field(min_length=1)
    estimated_time: str | None = Field(alias="estimatedTime", min_length=1, max_length=50)

class ExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа упражнения
    """
    exercise: ExerciseSchema

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(min_length=1, max_length=250)
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None = Field(min_length=1)
    estimated_time: str | None = Field(alias="estimatedTime", min_length=1, max_length=50)
