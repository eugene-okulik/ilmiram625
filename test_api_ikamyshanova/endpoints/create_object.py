import requests
import allure

from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    @allure.step('Create new object')
    def create_new_object(self, body):
        self.response = requests.post(self.url, json=body)
        self.json = self.response.json()
        return self.response

    @allure.step('Status code is 201')
    def check_status_code(self):
        assert self.response.status_code == 201, f'Status code is "{self.response.status_code}", not 201!'
