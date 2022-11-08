from unittest import result
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def item_func(uuid):
    if uuid == "-1":
        return {'SUCCESS': 'wrong item!'}
    else:
        return {'SUCCESS': f'{uuid}'}

@app.route('/item/<uuid>', methods=['GET'])
def show_item(uuid):
    result = item_func(uuid)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')
