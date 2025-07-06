import allure
import requests

from endpoints.endpoint import Endpoint


class UpdateAll(Endpoint):
    @allure.step('Update all in object')
    def update_all_in_object(self, id, body):
        self.response = requests.put(f'{self.url}/{id}', json=body)
        self.json = self.response.json()
        return self.response
