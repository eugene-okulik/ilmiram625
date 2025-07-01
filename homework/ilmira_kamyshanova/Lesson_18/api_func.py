import requests


def new_object():
    body = {
        "data": {
            "color": "purple",
            "size": "small"
        },
        "name": "New object"
    }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    return response.json()['id']


def clear(delete_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{delete_id}')


def post_object():
    body = {
        "data": {
            "color": "purple",
            "size": "small"
        },
        "name": "New object"
    }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    assert response.status_code == 201, f'Status code is "{response.status_code}", not 201!'
    assert 'id' in response.json()
    assert response.json()['id']
    assert response.json()['name'] == body['name']
    assert response.json()['data'] == body['data']
    clear(response.json()['id'])


def put_object():
    put_id = new_object()
    body = {
        "data": {
            "color": "purple-UPD",
            "size": "small-UPD"
        },
        "name": "New object"
    }
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{put_id}', json=body)
    assert response.status_code == 200, f'Status code is "{response.status_code}", not 200!'
    assert response.json()['name'] == body['name']
    assert response.json()['data'] == body['data']
    clear(put_id)


def patch_object():
    patch_id = new_object()
    body = {
        "data": {
            "color": "purple-UPD-2",
            "size": "small-UPD-2"
        }
    }
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{patch_id}', json=body)
    assert response.status_code == 200, f'Status code is "{response.status_code}", not 200!'
    assert response.json()['data'] == body['data']
    clear(patch_id)


def delete_object():
    delete_id = new_object()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{delete_id}')
    assert response.status_code == 200, f'Status code is "{response.status_code}", not 200!'


post_object()
put_object()
patch_object()
delete_object()
