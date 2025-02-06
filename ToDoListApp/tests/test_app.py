import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'ToDo List' in rv.data

def test_add_task(client):
    rv = client.post('/', data={'task': 'Test Task'})
    assert rv.status_code == 200
    assert b'Test Task' in rv.data

def test_delete_task(client):
    client.post('/', data={'task': 'Test Task'})
    rv = client.get('/delete/0')
    assert rv.status_code == 302  # Redirect after deletion
    rv = client.get('/')
    assert b'Test Task' not in rv.data