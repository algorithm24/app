from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    if username and password:
        result = {'SUCCESS': 'Create Successful',
                f'{username}': f'{password}'}
    else:
        result = {'FAILED': 'Create Failed'}
    return jsonify(result)

if __name__ == '__main__':
    app.run()