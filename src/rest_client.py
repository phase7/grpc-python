import requests
import time


def run():
    base_url = 'http://localhost:5000/item'

    # Create an item
    start = time.time()
    response = requests.post(
        base_url, json={'name': 'Item1', 'description': 'Description1'})
    end = time.time()
    item = response.json()
    print('CreateItem:', item)
    print('Average CreateItem Time:', (end - start) * 1000, 'milliseconds')

    # Get the item
    start = time.time()
    response = requests.get(f'{base_url}/{item["id"]}')
    end = time.time()
    item = response.json()
    print('GetItem:', item)
    print('Average GetItem Time:', (end - start) * 1000, 'milliseconds')

    # Update the item
    start = time.time()
    response = requests.put(f'{base_url}/{item["id"]}', json={
                            'id': item['id'], 'name': 'Item1', 'description': 'Updated Description'})
    end = time.time()
    item = response.json()
    print('UpdateItem:', item)
    print('Average UpdateItem Time:', (end - start) * 1000, 'milliseconds')

    # Delete the item
    start = time.time()
    response = requests.delete(f'{base_url}/{item["id"]}')
    end = time.time()
    success = response.json().get('success', False)
    print('DeleteItem:', success)
    print('Average DeleteItem Time:', (end - start) * 1000, 'milliseconds')


if __name__ == '__main__':
    run()
