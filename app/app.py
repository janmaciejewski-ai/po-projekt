from flask import Flask, jsonify, request, abort
from app.storage import storage

app = Flask(__name__)

def validate_user_data(data, partial=False):
    if not isinstance(data, dict):
        return "Payload must be a JSON object"
    
    allowed_keys = {"name", "lastname"}
    
    if any(k not in allowed_keys for k in data.keys()):
        return "Unknown fields in payload"

    if partial:
        if not data:
             return "Empty body"
    else:
        if "name" not in data or "lastname" not in data:
            return "Missing 'name' or 'lastname'"

    if "name" in data and not isinstance(data["name"], str):
        return "'name' must be a string"
    if "lastname" in data and not isinstance(data["lastname"], str):
        return "'lastname' must be a string"
        
    return None

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(storage.get_all()), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = storage.get_by_id(user_id)
    if not user:
        abort(404)
    return jsonify(user), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json(silent=True)
    error = validate_user_data(data, partial=False)
    if error:
        abort(400, description=error)
    
    user = storage.add(data['name'], data['lastname'])
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    user = storage.get_by_id(user_id)
    if not user:
        abort(400)

    data = request.get_json(silent=True)
    error = validate_user_data(data, partial=True)
    if error:
        abort(400)

    storage.update(user_id, data)
    return '', 204

@app.route('/users/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    data = request.get_json(silent=True)
    error = validate_user_data(data, partial=False)
    if error:
        abort(400)
        
    storage.put(user_id, data['name'], data['lastname'])
    return '', 204

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted = storage.delete(user_id)
    if not deleted:
        abort(400)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
