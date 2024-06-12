import pytest
import sys
#sys.path.append('C:\\Desktop\\demo')
from demo1.app import app 

@pytest.fixture
def client():
    #hell.hello['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.data == b'Hello World'
    assert response.status_code == 200
