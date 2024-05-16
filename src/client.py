import time

import grpc
import typer

import my_service_pb2
import my_service_pb2_grpc

ITER_NUMBER = 10000


def benchmark_operation(stub, operation, *args, iterations=ITER_NUMBER):
    start_time = time.monotonic()
    total_request_bytes = 0
    total_response_bytes = 0

    for _ in range(iterations):
        request_size, response_size = operation(stub, *args)
        total_request_bytes += request_size
        total_response_bytes += response_size

    end_time = time.monotonic()
    avg_time = (end_time - start_time) / iterations * 1000  # milliseconds
    avg_request_bytes = total_request_bytes / iterations
    avg_response_bytes = total_response_bytes / iterations

    return avg_time, avg_request_bytes, avg_response_bytes, total_request_bytes + total_response_bytes, (end_time - start_time)


def create_item(stub, item):
    request_bytes = item.SerializeToString()
    response = stub.CreateItem(item)
    response_bytes = response.SerializeToString()
    return len(request_bytes), len(response_bytes)


def get_item(stub, item_id):
    request_bytes = item_id.SerializeToString()
    response = stub.GetItem(item_id)
    response_bytes = response.SerializeToString()
    return len(request_bytes), len(response_bytes)


def update_item(stub, item):
    request_bytes = item.SerializeToString()
    response = stub.UpdateItem(item)
    response_bytes = response.SerializeToString()
    return len(request_bytes), len(response_bytes)


def delete_item(stub, item_id):
    request_bytes = item_id.SerializeToString()
    response = stub.DeleteItem(item_id)
    response_bytes = response.SerializeToString()
    return len(request_bytes), len(response_bytes)


def run(iterations: int = ITER_NUMBER):
    channel = grpc.insecure_channel('localhost:50051')
    stub = my_service_pb2_grpc.ItemServiceStub(channel)

    total_bytes_transferred = 0
    total_time_spent = 0

    # Create an item
    item = my_service_pb2.Item(id='1', name='Item 1')
    avg_create_time, _, _, create_bytes_transferred, create_time_spent = benchmark_operation(
        stub, create_item, item, iterations=iterations)
    total_bytes_transferred += create_bytes_transferred
    total_time_spent += create_time_spent
    print(f"Average CreateItem Time: {avg_create_time} milliseconds")

    # Get the item
    item_id = my_service_pb2.ItemId(id='1')
    avg_get_time, _, _, get_bytes_transferred, get_time_spent = benchmark_operation(
        stub, get_item, item_id, iterations=iterations)
    total_bytes_transferred += get_bytes_transferred
    total_time_spent += get_time_spent
    print(f"Average GetItem Time: {avg_get_time} milliseconds")

    # Update the item
    item = my_service_pb2.Item(id='1', name='Updated Item 1')
    avg_update_time, _, _, update_bytes_transferred, update_time_spent = benchmark_operation(
        stub, update_item, item, iterations=iterations)
    total_bytes_transferred += update_bytes_transferred
    total_time_spent += update_time_spent
    print(f"Average UpdateItem Time: {avg_update_time} milliseconds")

    # Delete the item separately to ensure it exists before each deletion
    total_delete_time = 0
    total_delete_req_bytes = 0
    total_delete_res_bytes = 0

    for _ in range(iterations):
        # Create item before deletion
        create_item(stub, item)
        start_time = time.monotonic()
        # Delete item
        req_bytes, res_bytes = delete_item(stub, item_id)
        end_time = time.monotonic()
        total_delete_time += (end_time - start_time)
        total_delete_req_bytes += req_bytes
        total_delete_res_bytes += res_bytes

    avg_delete_time = total_delete_time / iterations * 1000  # milliseconds
    total_delete_bytes_transferred = total_delete_req_bytes + total_delete_res_bytes
    total_bytes_transferred += total_delete_bytes_transferred
    total_time_spent += total_delete_time
    print(f"Average DeleteItem Time: {avg_delete_time} milliseconds")

    # Summary
    print(f"Total Bytes Transferred: {total_bytes_transferred}")
    print(f"Total Time Spent (seconds): {total_time_spent}")
    transfer_rate = total_bytes_transferred / total_time_spent
    print(f"Transfer Rate (bytes/second): {transfer_rate}")


if __name__ == '__main__':
    typer.run(run)
