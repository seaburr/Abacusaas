from flask import Flask
from abacus import Abacus

app = Flask(__name__)


@app.route('/')
def index():
    return '<pre>This is AaaS - Abacus as a Service.\n\n' \
           'Please use GET /rest/api/v1/get/{integer} to get an abacus.</pre>'


@app.route('/hc')
def health_check():
    return '<pre>Abacus as a Service is up and running.</pre>'


@app.route('/rest/api/v1/get/<int:value>')
def add_value(value):
    return f'<pre>{Abacus(value).get_abacus()}</pre>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

