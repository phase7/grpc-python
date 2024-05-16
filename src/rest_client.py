import requests
import time
import json

ITER_NUMBER = 1000
def calculate_transfer_rate(total_bytes, total_time_seconds):
    # Transfer rate in bytes per second
    return total_bytes / total_time_seconds

def run():
    base_url = 'http://localhost:5000/item'
    
    total_bytes_transferred = 0
    total_time_spent = 0

    # Perform CreateItem ITER_NUMBER times
    total_create_time = 0
    for _ in range(ITER_NUMBER):
        start = time.time()
        response = requests.post(base_url, json={'name': 'Item1', 'description': 'Description1'})
        end = time.time()
        
        item = response.json()
        total_create_time += (end - start)
        total_bytes_transferred += len(response.content) + len(json.dumps({'name': 'Item1', 'description': 'Description1'}))

    avg_create_time = (total_create_time / ITER_NUMBER) * 1000  # Convert to milliseconds
    print('Average CreateItem Time:', avg_create_time, 'milliseconds')
    total_time_spent += total_create_time

    # Perform GetItem ITER_NUMBER times
    total_get_time = 0
    for _ in range(ITER_NUMBER):
        start = time.time()
        response = requests.get(f'{base_url}/{item["id"]}')
        end = time.time()
        
        item = response.json()
        total_get_time += (end - start)
        total_bytes_transferred += len(response.content) + len(json.dumps({'id': item['id']}))

    avg_get_time = (total_get_time / ITER_NUMBER) * 1000  # Convert to milliseconds
    print('Average GetItem Time:', avg_get_time, 'milliseconds')
    total_time_spent += total_get_time

    # Perform UpdateItem ITER_NUMBER times
    total_update_time = 0
    for _ in range(ITER_NUMBER):
        start = time.time()
        response = requests.put(f'{base_url}/{item["id"]}', json={'id': item['id'], 'name': 'Item1', 'description': 'Updated Description'})
        end = time.time()
        
        item = response.json()
        total_update_time += (end - start)
        total_bytes_transferred += len(response.content) + len(json.dumps({'id': item['id'], 'name': 'Item1', 'description': 'Updated Description'}))

    avg_update_time = (total_update_time / ITER_NUMBER) * 1000  # Convert to milliseconds
    print('Average UpdateItem Time:', avg_update_time, 'milliseconds')
    total_time_spent += total_update_time

    # Perform DeleteItem ITER_NUMBER times
    total_delete_time = 0
    for _ in range(ITER_NUMBER):
        start = time.time()
        response = requests.delete(f'{base_url}/{item["id"]}')
        end = time.time()
        
        success = response.json().get('success', False)
        total_delete_time += (end - start)
        total_bytes_transferred += len(response.content) + len(json.dumps({'id': item['id']}))

    avg_delete_time = (total_delete_time / ITER_NUMBER) * 1000  # Convert to milliseconds
    print('Average DeleteItem Time:', avg_delete_time, 'milliseconds')
    total_time_spent += total_delete_time

    transfer_rate = calculate_transfer_rate(total_bytes_transferred, total_time_spent)
    print('Total Bytes Transferred:', total_bytes_transferred)
    print('Total Time Spent (seconds):', total_time_spent)
    print('Transfer Rate (bytes/second):', transfer_rate)

if __name__ == '__main__':
    run()
