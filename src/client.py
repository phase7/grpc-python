import grpc
import simple_service_pb2
import simple_service_pb2_grpc

def run_grpc_client():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = simple_service_pb2_grpc.GreetingServiceStub(channel)
        response = stub.SayHello(simple_service_pb2.HelloRequest(name='Alice'))
        print("gRPC client received: " + response.message)

# Uncomment the following line when running the script
# run_grpc_client()
