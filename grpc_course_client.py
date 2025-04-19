import grpc
import course_service_pb2
import course_service_pb2_grpc


channel = grpc.insecure_channel('localhost:50052')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="Alice"))
print("Ответ от сервера:")
print(f"course_id: {response.course_id}")
print(f"title: {response.title}")
print(f"description: {response.description}")

