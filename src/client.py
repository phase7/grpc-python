import grpc
import my_service_pb2
import my_service_pb2_grpc
import typer

def get_item(item_id: str):
    with grpc.insecure_channel('localhost:50051', compression=grpc.Compression.Deflate) as channel:
        stub = my_service_pb2_grpc.ItemServiceStub(channel)
        response = stub.GetItem(my_service_pb2.ItemId(id=item_id))
        if response.id:
            print(f"Retrieved item: {response.name}")
        else:
            print("Item not found.")

if __name__ == '__main__':
    typer.run(get_item)
