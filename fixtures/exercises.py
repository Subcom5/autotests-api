import pytest
from pydantic import BaseModel

from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema
from clients.exercises.exercises_client import ExercisesClient, get_exercise_client
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercise_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercise_client(function_user.authentication_user)

@pytest.fixture
def function_exercise(
        exercise_client: ExercisesClient,
        function_course: CourseFixture
) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(
        course_id=function_course.response.course.id
    )
    response = exercise_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
