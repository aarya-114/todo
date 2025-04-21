# test_app.py

import pytest
from app import app  # Assuming your Flask app is in app.py

@pytest.fixture
def client():
    """Fixture to set up Flask app for testing."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_todos(client):
    """Test the GET /todos endpoint"""
    response = client.get('/todos')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Check if the response is a list

def test_create_todo(client):
    """Test the POST /todos endpoint"""
    new_todo = {'task': 'Test a new task'}
    response = client.post('/todos', json=new_todo)
    assert response.status_code == 201
    assert 'task' in response.json  # Check if the task was added to the response

def test_get_todo_by_id(client):
    """Test GET /todos/{id}"""
    # Let's assume you already have a todo with ID 1
    response = client.get('/todos/1')
    assert response.status_code == 200
    assert response.json['id'] == 1

def test_delete_todo_by_id(client):
    """Test DELETE /todos/{id}"""
    # Assuming a todo with ID 1 exists
    response = client.delete('/todos/1')
    assert response.status_code == 204  # No Content (success)
