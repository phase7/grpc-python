import grpc
from concurrent import futures
import time
import my_service_pb2
import my_service_pb2_grpc

class ItemServiceServicer(my_service_pb2_grpc.ItemServiceServicer):
    def __init__(self):
        self.items = {}

    def CreateItem(self, request, context):
        self.items[request.id] = request
        return request

    def GetItem(self, request, context):
        item = self.items.get(request.id, None)
        if item is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "Item not found")
        return item

    def UpdateItem(self, request, context):
        if request.id not in self.items:
            context.abort(grpc.StatusCode.NOT_FOUND, "Item not found")
        self.items[request.id] = request
        return request

    def DeleteItem(self, request, context):
        item = self.items.pop(request.id, None)
        if item is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "Item not found")
        return item

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_service_pb2_grpc.add_ItemServiceServicer_to_server(ItemServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
