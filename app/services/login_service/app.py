from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def login_func(username, password):
    if username == 'admin' and password == 'admin':
        return {'SUCCESS': 'Login Successful',
                f'{username}': f'{password}'}
    else:
        return {'FAILED': 'Login Failed'}

@app.route('/login/<username>/<password>', methods = ['GET'])
def login(username, password):
    result = login_func(username, password)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')