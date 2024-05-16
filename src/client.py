import grpc
import time
import my_service_pb2
import my_service_pb2_grpc

def benchmark_operation(stub, operation, *args):
    start_time = time.time()
    for _ in range(10000):
        operation(stub, *args)
    end_time = time.time()
    return (end_time - start_time) * 1000 / 10000  # Convert seconds to milliseconds

def create_item(stub, item):
    response = stub.CreateItem(item)
    return response

def get_item(stub, item_id):
    response = stub.GetItem(item_id)
    return response

def update_item(stub, item):
    response = stub.UpdateItem(item)
    return response

def delete_item(stub, item_id):
    response = stub.DeleteItem(item_id)
    return response

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = my_service_pb2_grpc.ItemServiceStub(channel)

    # Create an item
    item = my_service_pb2.Item(id='1', name='Item 1')
    avg_create_time = benchmark_operation(stub, create_item, item)
    print(f"Average CreateItem Time: {avg_create_time} milliseconds")

    # Get the item
    item_id = my_service_pb2.ItemId(id='1')
    avg_get_time = benchmark_operation(stub, get_item, item_id)
    print(f"Average GetItem Time: {avg_get_time} milliseconds")

    # Update the item
    item = my_service_pb2.Item(id='1', name='Updated Item 1')
    avg_update_time = benchmark_operation(stub, update_item, item)
    print(f"Average UpdateItem Time: {avg_update_time} milliseconds")

    # Delete the item separately to ensure it exists before each deletion
    def benchmark_delete_operation():
        for _ in range(10000):
            # Create item before deletion
            create_item(stub, item)
            # Delete item
            delete_item(stub, item_id)

    start_time = time.time()
    benchmark_delete_operation()
    end_time = time.time()
    avg_delete_time = (end_time - start_time) * 1000 / 10000  # Convert seconds to milliseconds
    print(f"Average DeleteItem Time: {avg_delete_time} milliseconds")

if __name__ == '__main__':
    run()
