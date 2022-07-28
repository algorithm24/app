from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/login/<username>/<password>', methods = ['GET'])
def login(username, password):
    result = {}
    if username == 'admin' and password == 'admin':
        result = {'SUCCESS': 'Login Successful',
                f'{username}': f'{password}'}
    else:
        result = {'FAILED': 'Login Failed'}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')