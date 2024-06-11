# grpc-python (without docker)

1. run init_db.py to create the database
2. run server.py to start the server
3. run client.py to query db for data

# grpc-python (with docker)

1. build image `docker build --no-cache -t data-guild-grpc .`
2. run server with dummy db `docker run -it --rm -p 50051:50051 data-guild-grpc server`
3. run benchmark client `docker run -it --rm --network="host" data-guild-grpc client --iterations 10000`
