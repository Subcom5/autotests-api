from concurrent import futures
import grpc
import course_service_pb2
import course_service_pb2_grpc


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    """Реализация методов gRPC-сервиса CourseSerice"""

    def GetCourse(self, request, context):
        """Метод GetCourse обрабатывает входящий запрос"""
        print(f"Получен запрос к методу GetCourse: {request.course_id}")

        if request.course_id == "Alice":
            title = "Автотесты API"
            description = "Будем изучать написание API автотестов"
        elif request.course_id == "1":
            title = "Автоматизация тестирования API с Python. Расширенный."
            description = "Этот курс — руководство по построению масштабируемого\n \
             и поддерживаемого тестового фреймворка."
        elif request.course_id == "2":
            title = "Автоматизация тестирования UI с Python и Playwright. Расширенный."
            description = "Этот курс — не только про инструменты, такие как Selenium или Playwright.\n \
            Он ориентирован на освоение профессии QA Automation Engineer в полном смысле этого слова."
        else:
            title = "Курс не найден"
            description = "Курс с таким ID отсутствует."

        return course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title=title,
            description=description
        )

def serve():
    """Функция создает и запускает gRPC-сервер"""

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)
    server.add_insecure_port('[::]:50052')

    server.start()
    print("gRPC сервер запущен на порту 50052...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()