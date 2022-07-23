from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/item/<uuid>', methods=['GET'])
def show_item(uuid):
    if uuid == "-1":
        result = {'SUCCESS': 'show all'}
    else:
        result = {'SUCCESS': f'{uuid}'}
    return jsonify(result)


if __name__ == '__main__':
    app.run()