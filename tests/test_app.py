import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from abacus import Abacus  # noqa: E402
from web import app  # noqa: E402


def client():
    return app.test_client()


def test_healthz():
    r = client().get('/healthz')
    assert r.status_code == 200
    assert b'up and running' in r.data


def test_index():
    r = client().get('/abacus')
    assert r.status_code == 200
    assert b'Abacus as a Service' in r.data


def test_abacus_endpoint():
    r = client().get('/abacus/rest/api/v1/get/7')
    assert r.status_code == 200
    assert r.data.startswith(b'<pre>|0-0|00-000|\n')


def test_abacus_rows():
    rows = Abacus(1234567890).get_abacus().splitlines()
    assert len(rows) == 10
    # Least significant digit is printed first.
    assert rows[0] == '|00-|-00000|'   # 0
    assert rows[-1] == '|00-|0-0000|'  # 1


def test_non_integer_is_404():
    assert client().get('/abacus/rest/api/v1/get/abc').status_code == 404
