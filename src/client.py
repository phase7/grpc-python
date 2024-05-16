import grpc
import time
import my_service_pb2
import my_service_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = my_service_pb2_grpc.ItemServiceStub(channel)

    # Create an item
    item = my_service_pb2.Item(id='1', name='Item 1')
    start_time = time.time()
    response = stub.CreateItem(item)
    print(f"CreateItem: {response}")
    print(f"CreateItem Time: {time.time() - start_time} seconds")

    # Get the item
    item_id = my_service_pb2.ItemId(id='1')
    start_time = time.time()
    response = stub.GetItem(item_id)
    print(f"GetItem: {response}")
    print(f"GetItem Time: {time.time() - start_time} seconds")

    # Update the item
    item = my_service_pb2.Item(id='1', name='Updated Item 1')
    start_time = time.time()
    response = stub.UpdateItem(item)
    print(f"UpdateItem: {response}")
    print(f"UpdateItem Time: {time.time() - start_time} seconds")

    # Delete the item
    start_time = time.time()
    response = stub.DeleteItem(item_id)
    print(f"DeleteItem: {response}")
    print(f"DeleteItem Time: {time.time() - start_time} seconds")

if __name__ == '__main__':
    run()
