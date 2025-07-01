import requests
import pytest


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


bodies = [{
    "data": {
        "color": "purple",
        "size": "small"
    },
    "name": "New object-1"
}, {
    "data": {
        "color": "white",
        "size": "big"
    },
    "name": "New object-2"
}, {
    "data": {
        "color": "pink",
        "size": "medium"
    },
    "name": "New object-3"
}]


@pytest.mark.critical
@pytest.mark.parametrize('body', bodies)
def test_post_object(message, message_for_tests, body):
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    assert response.status_code == 200, f'Status code is "{response.status_code}", not 201!'
    assert 'id' in response.json()
    assert response.json()['id']
    assert response.json()['name'] == body['name']
    assert response.json()['data'] == body['data']


@pytest.mark.medium
def test_put_object(new_object_id, message_for_tests):
    body = {
        "data": {
            "color": "purple-UPD",
            "size": "small-UPD"
        },
        "name": "New object"
    }
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{new_object_id}', json=body)
    assert response.status_code == 200, f'Status code is "{response.status_code}", not 200!'
    assert response.json()['name'] == body['name']
    assert response.json()['data'] == body['data']


def test_patch_object(new_object_id, message_for_tests):
    body = {
        "data": {
            "color": "purple-UPD-2",
            "size": "small-UPD-2"
        }
    }
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{new_object_id}', json=body)
    assert response.status_code == 200, f'Status code is "{response.status_code}", not 200!'
    assert response.json()['data'] == body['data']


def test_delete_object(new_object_id, message_for_tests):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object_id}')
    assert response.status_code == 200, f'Status code is "{response.status_code}", not 200!'
