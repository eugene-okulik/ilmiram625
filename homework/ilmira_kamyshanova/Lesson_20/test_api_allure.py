import requests
import pytest
import allure

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


@allure.title('Post new object')
@allure.feature('Create/update objects')
@allure.story('Create objects')
@pytest.mark.critical
@pytest.mark.parametrize('body', bodies)
def test_post_object(message, message_for_tests, body):
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    assert response.status_code == 200, f'Status code is "{response.status_code}", not 201!'
    assert 'id' in response.json()
    assert response.json()['id']
    assert response.json()['name'] == body['name']
    assert response.json()['data'] == body['data']


@allure.title('Update all in object')
@allure.feature('Create/update objects')
@allure.story('Update objects')
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


@allure.title('Update object')
@allure.feature('Create/update objects')
@allure.story('Update objects')
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


@allure.title('Update object')
@allure.feature('Delete objects')
@allure.story('Delete objects')
def test_delete_object(new_object_id, message_for_tests):
    with allure.step(f'Get object by id = {new_object_id}'):
        response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object_id}')
        allure.attach(response.text, name='Response body', attachment_type=allure.attachment_type.TEXT)
    with allure.step('Check status code equal 200'):
        assert response.status_code == 200, f'Status code is "{response.status_code}", not 200!'
