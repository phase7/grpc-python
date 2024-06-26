import requests
import time
import json

import typer

ITER_NUMBER = 1000


def calculate_transfer_rate(total_bytes, total_time_seconds):
    """
    Calculates the transfer rate in bytes per second.

    Args:
        total_bytes (int): The total number of bytes transferred.
        total_time_seconds (float): The total time taken for the transfer in seconds.

    Returns:
        float: The transfer rate in bytes per second.
    """
    return total_bytes / total_time_seconds


def run(iterations: int = ITER_NUMBER):
    """
    Runs a series of HTTP requests to create, get, update, and delete items.

    Args:
        iterations (int): The number of iterations to perform for each request. 
                          Default is ITER_NUMBER.
    """

    base_url = 'http://localhost:5000/item'

    total_bytes_transferred = 0
    total_time_spent = 0

    # Perform CreateItem iterations
    total_create_time = 0
    for i in range(iterations):
        start = time.time()
        response = requests.post(base_url,
                                 json={'name': f'Item{i}',
                                       'description': f'Description{i}'},
                                 timeout=200)
        end = time.time()

        total_create_time += (end - start)
        total_bytes_transferred += len(response.content) + len(
            json.dumps({'name': 'Item1', 'description': 'Description1'}))

    avg_create_time = (total_create_time / iterations) * \
        1000  # Convert to milliseconds
    print('Average CreateItem Time:', avg_create_time, 'milliseconds')
    total_time_spent += total_create_time

    # Perform GetItem iterations
    total_get_time = 0
    for i in range(iterations):
        start = time.time()
        response = requests.get(f'{base_url}/{i}', timeout=200)
        end = time.time()

        total_get_time += (end - start)
        total_bytes_transferred += len(response.content) + \
            len(json.dumps({'id': i}))

    avg_get_time = (total_get_time / iterations) * \
        1000  # Convert to milliseconds
    print('Average GetItem Time:', avg_get_time, 'milliseconds')
    total_time_spent += total_get_time

    # Perform UpdateItem iterations
    total_update_time = 0
    for i in range(iterations):
        start = time.time()
        response = requests.put(f'{base_url}/{i}', json={'id': i, 'name': 'Item1',
                                'description': 'Updated Description'}, timeout=200)
        end = time.time()

        total_update_time += (end - start)
        total_bytes_transferred += len(response.content) + len(json.dumps(
            {'id': i, 'name': 'Item1', 'description': 'Updated Description'}))

    avg_update_time = (total_update_time / iterations) * \
        1000  # Convert to milliseconds
    print('Average UpdateItem Time:', avg_update_time, 'milliseconds')
    total_time_spent += total_update_time

    # Perform DeleteItem iterations
    total_delete_time = 0
    for i in range(iterations):
        start = time.time()
        response = requests.delete(f'{base_url}/{i}', timeout=200)
        end = time.time()

        total_delete_time += (end - start)
        total_bytes_transferred += len(response.content) + \
            len(json.dumps({'id': i}))

    avg_delete_time = (total_delete_time / iterations) * \
        1000  # Convert to milliseconds
    print('Average DeleteItem Time:', avg_delete_time, 'milliseconds')
    total_time_spent += total_delete_time

    transfer_rate = calculate_transfer_rate(
        total_bytes_transferred, total_time_spent)
    print('Total Bytes Transferred:', total_bytes_transferred)
    print('Total Time Spent (seconds):', total_time_spent)
    print('Transfer Rate (bytes/second):', transfer_rate)


if __name__ == '__main__':
    typer.run(run)
