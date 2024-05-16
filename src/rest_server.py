from flask import Flask, request, jsonify

app = Flask(__name__)
items = {}
next_id : int = 0


@app.route('/item', methods=['POST'])
def create_item():
    global next_id
    item = request.json
    item['id'] = next_id
    items[next_id] = item
    next_id += 1
    return jsonify(item), 201


@app.route('/item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = items.get(item_id)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404


@app.route('/item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = request.json
    if item_id in items:
        items[item_id] = item
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404


@app.route('/item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return jsonify({'success': True})
    return jsonify({'error': 'Item not found'}), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)
