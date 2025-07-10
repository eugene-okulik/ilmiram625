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
def test_post_object(post_endpoint, body):
    post_endpoint.create_new_object(body)
    post_endpoint.check_status_code_is_200()
    post_endpoint.check_data(body['data'], body['name'])


@allure.title('Update all in object')
@allure.feature('Create/update objects')
@allure.story('Update objects')
@pytest.mark.medium
def test_put_object(new_object_id, put_endpoint):
    body = {
        "data": {
            "color": "purple-UPD",
            "size": "small-UPD"
        },
        "name": "New object"
    }
    put_endpoint.update_all_in_object(new_object_id, body)
    put_endpoint.check_status_code_is_200()
    put_endpoint.check_data(body['data'], body['name'])


@allure.title('Update object')
@allure.feature('Create/update objects')
@allure.story('Update objects')
def test_patch_object(new_object_id, patch_endpoint):
    body = {
        "data": {
            "color": "purple-UPD-2",
            "size": "small-UPD-2"
        }
    }
    patch_endpoint.update_object(new_object_id, body)
    patch_endpoint.check_status_code_is_200()
    patch_endpoint.check_data(data=body['data'])


@allure.title('Delete object')
@allure.feature('Delete objects')
@allure.story('Delete objects')
def test_delete_object(new_object_id, delete_endpoint):
    delete_endpoint.delete_object(new_object_id)
    delete_endpoint.check_status_code_is_200()
