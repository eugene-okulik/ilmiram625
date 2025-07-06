import allure
import requests

from endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):
    @allure.step('Update object')
    def update_object(self, id, body):
        self.response = requests.patch(f'{self.url}/{id}', json=body)
        self.json = self.response.json()
        return self.response