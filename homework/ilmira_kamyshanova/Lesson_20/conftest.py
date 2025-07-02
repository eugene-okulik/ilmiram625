import pytest
import requests


@pytest.fixture(scope='session')
def message():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(scope='function')
def message_for_tests():
    print("before test")
    yield
    print("after test")


@pytest.fixture()
def new_object_id():
    body = {
        "data": {
            "color": "purple",
            "size": "small"
        },
        "name": "New object"
    }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')
