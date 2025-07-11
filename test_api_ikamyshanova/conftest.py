import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.update_all import UpdateAll
from endpoints.update_object import UpdateObject


@pytest.fixture()
def post_endpoint():
    return CreateObject()


@pytest.fixture()
def put_endpoint():
    return UpdateAll()


@pytest.fixture()
def patch_endpoint():
    return UpdateObject()


@pytest.fixture()
def delete_endpoint():
    return DeleteObject()


@pytest.fixture()
def new_object_id(post_endpoint, delete_endpoint):
    body = {
        "data": {
            "color": "purple",
            "size": "small"
        },
        "name": "New object"
    }
    obj_id = post_endpoint.create_new_object(body).json()['id']
    yield obj_id
    delete_endpoint.delete_object(obj_id)
