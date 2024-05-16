import requests
import time

ITER_NUMBER = 1000
def run():
    base_url = 'http://localhost:5000/item'
    
    # Perform CreateItem ITER_NUMBER times
    total_create_time = 0
    for _ in range(ITER_NUMBER):
        start = time.time()
        response = requests.post(base_url, json={'name': 'Item1', 'description': 'Description1'})
        end = time.time()
        total_create_time += (end - start)
        item = response.json()

    avg_create_time = (total_create_time / ITER_NUMBER) * 1000  # Convert to milliseconds
    print('Average CreateItem Time:', avg_create_time, 'milliseconds')

    # Perform GetItem ITER_NUMBER times
    total_get_time = 0
    for _ in range(ITER_NUMBER):
        start = time.time()
        response = requests.get(f'{base_url}/{item["id"]}')
        end = time.time()
        total_get_time += (end - start)
        item = response.json()

    avg_get_time = (total_get_time / ITER_NUMBER) * 1000  # Convert to milliseconds
    print('Average GetItem Time:', avg_get_time, 'milliseconds')

    # Perform UpdateItem ITER_NUMBER times
    total_update_time = 0
    for _ in range(ITER_NUMBER):
        start = time.time()
        response = requests.put(f'{base_url}/{item["id"]}', json={'id': item['id'], 'name': 'Item1', 'description': 'Updated Description'})
        end = time.time()
        total_update_time += (end - start)
        item = response.json()

    avg_update_time = (total_update_time / ITER_NUMBER) * 1000  # Convert to milliseconds
    print('Average UpdateItem Time:', avg_update_time, 'milliseconds')

    # Perform DeleteItem ITER_NUMBER times
    total_delete_time = 0
    for _ in range(ITER_NUMBER):
        start = time.time()
        response = requests.delete(f'{base_url}/{item["id"]}')
        end = time.time()
        total_delete_time += (end - start)
        success = response.json().get('success', False)

    avg_delete_time = (total_delete_time / ITER_NUMBER) * 1000  # Convert to milliseconds
    print('Average DeleteItem Time:', avg_delete_time, 'milliseconds')

if __name__ == '__main__':
    run()
