from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/start')
def start():
    return 'start'


@app.route('/select/<name>')
def select(name):
    return 'hi %s' % name


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1><input type="textbox"/>'


@app.route('/history/add', methods=["POST", "GET"])
def test_get_json():
    json_data = request.get_json()
    print(json_data)
    return "hello test json"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="7070")