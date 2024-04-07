import grpc
import my_service_pb2
import my_service_pb2_grpc

def get_item(item_id):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = my_service_pb2_grpc.ItemServiceStub(channel)
        response = stub.GetItem(my_service_pb2.ItemId(id=item_id))
        if response.id:
            print(f"Retrieved item: {response.name}")
        else:
            print("Item not found.")

if __name__ == '__main__':
    # Test getting an item (Assume the item with id '1' does not exist yet)
    get_item('1')
