import grpc
import time
import myservice_pb2
import myservice_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = myservice_pb2_grpc.ItemServiceStub(channel)

    # Create an item
    item = myservice_pb2.Item(id='1', name='Item 1')
    start_time = time.time()
    response = stub.CreateItem(item)
    print(f"CreateItem: {response}")
    print(f"CreateItem Time: {time.time() - start_time} seconds")

    # Get the item
    item_id = myservice_pb2.ItemId(id='1')
    start_time = time.time()
    response = stub.GetItem(item_id)
    print(f"GetItem: {response}")
    print(f"GetItem Time: {time.time() - start_time} seconds")

    # Update the item
    item = myservice_pb2.Item(id='1', name='Updated Item 1')
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
