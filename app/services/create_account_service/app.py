from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def create_func(username, password):
    if username and password:
        return {'SUCCESS': 'Create Successful',
                f'{username}': f'{password}'}
    else:
        return {'FAILED': 'Create Failed'}

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    result = create_func(username, password)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=4000, host='0.0.0.0')