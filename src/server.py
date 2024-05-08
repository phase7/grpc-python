import grpc
from concurrent import futures
import simple_service_pb2
import simple_service_pb2_grpc

class GreetingService(simple_service_pb2_grpc.GreetingServiceServicer):

    def SayHello(self, request, context):
        return simple_service_pb2.HelloResponse(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    simple_service_pb2_grpc.add_GreetingServiceServicer_to_server(GreetingService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

# Uncomment the following line when running the script
# serve()
