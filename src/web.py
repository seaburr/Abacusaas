from flask import Flask
from abacus import Abacus

app = Flask(__name__)


@app.route('/abacus')
def index():
    return '<pre>This is AaaS - Abacus as a Service.\n\n' \
           'Please use GET /abacus/rest/api/v1/get/{integer} to get an abacus.</pre>'


@app.route('/healthz')
def hc():
    return '<pre>Abacus as a Service is up and running.</pre>', 200


@app.route('/abacus/rest/api/v1/get/<int:value>')
def add_value(value):
    return f'<pre>{Abacus(value).get_abacus()}</pre>', 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
