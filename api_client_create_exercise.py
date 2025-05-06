from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercise_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, GetExercisesQuerySchema, \
    UpdateExerciseRequestSchema
from clients.files.files_client import get_files_client, CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema


public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestSchema()
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиенты
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercise_client = get_exercise_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestSchema(upload_file="./testdata/files/server_image.png")
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestSchema(
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# Создаем упражнение
create_exercise_request = CreateExerciseRequestSchema(courseId=create_course_response.course.id,)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)

#------------------------------------------
# Проверка остальных методов.

# Создаем упражнение
create_exercise_request = CreateExerciseRequestSchema(courseId=create_course_response.course.id,)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)

# Запрашиваем данные по упражнению
get_exercise_response = exercise_client.get_exercise(
    create_exercise_response.exercise.id
)
print('Get exercise data:', get_exercise_response)

# Запрашиваем список всех упражнений в курсе
get_exercises_response = exercise_client.get_exercises(
    GetExercisesQuerySchema(courseId=create_course_response.course.id)
)
print('Get list exercise data:', get_exercises_response)

# Обновляем упражнение "Упражнение 1".
update_exercise_response = exercise_client.update_exercise(
    create_exercise_response.exercise.id,
    UpdateExerciseRequestSchema()
)
print("Updated exercise:", update_exercise_response)
