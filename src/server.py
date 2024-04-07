from concurrent import futures
import grpc
import sqlite3
import my_service_pb2
import my_service_pb2_grpc

class ItemService(my_service_pb2_grpc.ItemServiceServicer):
    def __init__(self):
        self.conn = sqlite3.connect('items.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def CreateItem(self, request, context):
        self.cursor.execute("INSERT INTO items VALUES (?, ?)", (request.id, request.name))
        self.conn.commit()
        return request

    def GetItem(self, request, context):
        self.cursor.execute("SELECT * FROM items WHERE id = ?", (request.id,))
        item = self.cursor.fetchone()
        if item:
            return my_service_pb2.Item(id=item[0], name=item[1])
        return my_service_pb2.Item()

    def UpdateItem(self, request, context):
        self.cursor.execute("UPDATE items SET name = ? WHERE id = ?", (request.name, request.id))
        self.conn.commit()
        return request

    def DeleteItem(self, request, context):
        self.cursor.execute("DELETE FROM items WHERE id = ?", (request.id,))
        self.conn.commit()
        return my_service_pb2.Item()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_service_pb2_grpc.add_ItemServiceServicer_to_server(ItemService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
